# https://stackoverflow.com/questions/14533420/can-you-suggest-a-good-minhash-implementation
# http://ekzhu.com/datasketch/lsh.html
# https://mccormickml.com/2015/06/12/minhash-tutorial-with-python-code/
from scipy.spatial.distance import cosine, jaccard

import numpy as np
import random
from random import randint


# print('perms=',perms)
# initialize a sample minhash vector of length N
# each record will be represented by its own vec
# vec = [float('inf') for i in range(N)]

def minhash(s, N=20, prime=4294967311):
    '''
  Given a set `s`, pass each member of the set through all permutation
  functions, and set the `ith` position of `vec` to the `ith` permutation
  function's output if that output is smaller than `vec[i]`.
  '''
    # specify the length of each minhash vector
    random.seed(42)
    max_val = (2 ** 32) - 1  # value connected with dictionary size

    # create N tuples that will serve as permutation functions
    # these permutation values are used to hash all input sets
    perms = [(randint(0, max_val), randint(0, max_val)) for i in range(N)]
    print('perms=', perms)

    # initialize a minhash of length N with positive infinity values
    vec = [float('inf') for i in range(N)]

    for val in s:

        # ensure s is composed of integers
        if not isinstance(val, int):
            val = hash(val)

        # loop over each "permutation function"
        for perm_idx, perm_vals in enumerate(perms):
            print(f'perm_idx: {perm_idx}, perm_vals {perm_vals}')
            a, b = perm_vals

            # pass `val` through the `ith` permutation function
            output = (a * val + b) % prime

            # conditionally update the `ith` value of vec
            if vec[perm_idx] > output:
                vec[perm_idx] = output

    # the returned vector represents the minimum hash of the set s
    return vec


import numpy as np

# specify some input sets


data1 = set(['skoda', 'octavia', 'ro', '##c', '##z', '##n', '##i', '##k', '2010', 'hatchback'])
data2 = set(['skoda', 'octavia', 'ro', '##c', '##z', '##n', '##i', '##k', '2011', 'hatchback'])

data1 = set([1, 2, 3, 4, 7, 8, 9, 20])
data2 = set([10, 11, 12, 13, 14, 20, 1])  # 2,3,9,20,145

# get the minhash vectors for each input set
prime = 37
vec1 = minhash(data1, prime=prime)
vec2 = minhash(data2, prime=prime)
print("vec1=", vec1)
print("vec2=", vec2)

print(' jacard:', jaccard(vec1, vec2))
# divide both vectors by their max values to scale values {0:1}
vec1 = np.array(vec1) / max(vec1)
vec2 = np.array(vec2) / max(vec2)

# print("vec1=",vec1)

# measure the similarity between the vectors using cosine similarity
print(' * similarity:', 1 - cosine(vec1, vec2))

"""
Encoded string: ['skoda', 'octavia', 'ro', '##c', '##z', '##n', '##i', '##k', '2010', 'hatchback']
Encoded string: [520, 569, 1186, 69, 76, 74, 73, 80, 302, 145]
Decoded string: skoda octavia rocznik 2010 hatchback
Encoded string: ['skoda', 'fabia', 'ro', '##c', '##z', '##n', '##i', '##k', '2011', 'hatchback']
Encoded string: [520, 592, 1186, 69, 76, 74, 73, 80, 354, 145]
Decoded string: skoda fabia rocznik 2011 hatchback

"""
