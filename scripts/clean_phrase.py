import re
import json
from fastDamerauLevenshtein import damerauLevenshtein #pip install fastDamerauLevenshtein


def create_dict_from_file(txt_file, dictionary_file='dictionary.json'):
    text = open(txt_file, "r")

    # Create an empty dictionary
    dictionary = dict()
    regex = re.compile('[^a-zA-Z]')

    # Loop through each line of the file
    for line in text:
        # Remove the leading spaces and newline character
        line = line.strip()

        # Convert the characters in line to
        # lowercase to avoid case mismatch
        line = line.lower()

        # Split the line into words
        words = re.split(';|,| ', line)

        # Iterate over each word in line
        for word in words:
            # Remove non-alpha numeric chars
            # word=regex.sub('',word)

            # Check if the word is already in dictionary
            if word in dictionary:
                # Increment count of word by 1
                dictionary[word] = dictionary[word] + 1
            else:
                # Add the word to dictionary with count 1
                dictionary[word] = 1
    # Save dictionary to json file
    with open(dictionary_file, 'w') as fp:
        json.dump(dictionary, fp)


##### TEST
def remove_errors(original_phrase, dictionary_file='dictionary.json'):
    # Read dictionary from file
    with open(dictionary_file) as f:
        dictionary = json.load(f)
    # Split original phrase into separate words
    words = re.split(' ', original_phrase)

    words_list = []
    for word in words:
        best_match = ''
        best_value = 0
        for key in dictionary:
            if word == key:
                words_list.append(word)
                break
            else:
                distance = damerauLevenshtein(word, key, similarity=False)

                if distance == 1:
                    if dictionary[key] > best_value:
                        best_value = dictionary[key]
                        best_match = key
        if best_value > 0: words_list.append(best_match)

    output_phrase = ' '.join(words_list)
    return output_phrase


if __name__ == "__main__":
    #Input data
    original_phrase = "volvo skoda hatchbacg qwerty"
    file = "napisy-w-cardb.txt"
    dictionary_file = 'dictionary.json'

    #Create dictionary from txt file
    create_dict_from_file(file, dictionary_file=dictionary_file)

    #Clean original phrase
    cleaned_phrase = remove_errors(original_phrase, dictionary_file=dictionary_file)

    print(f'The original phrase was: {original_phrase} ---- the cleaned phrase is: {cleaned_phrase}')
