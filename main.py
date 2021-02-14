from MinhashTool.mh_tool import MinHashTool
import numpy as np
from scipy.spatial.distance import cosine

if __name__ == "__main__":
    mhtool=MinHashTool()

    mhtool.combine_csv_files(dir_csvs_path="C:\PycharmProjects\TestWheel\data_files")



    #function_init()
    #print_age(45)

# specify some input sets


#data1=set(['skoda', 'octavia', 'ro', '##c', '##z', '##n', '##i', '##k', '2010', 'hatchback'])
#data2=set(['skoda', 'octavia', 'ro', '##c', '##z', '##n', '##i', '##k', '2011', 'hatchback'])



"""
# get the minhash vectors for each input set
vec1 = minhash_from_set(data1)
vec2 = minhash_from_set(data2)


# divide both vectors by their max values to scale values {0:1}
vec1 = np.array(vec1) / max(vec1)
vec2 = np.array(vec2) / max(vec2)

#print("vec1=",vec1)

# measure the similarity between the vectors using cosine similarity
print( ' * similarity:', 1 - cosine(vec1, vec2) )

print('similarity:',calculate_similarity(data1, data2))
"""