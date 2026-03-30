############## COLLECTIONS FUNCTIONS ##############

# Import random module to generate random numbers
import random

# Import string module to get alphabet letters
import string


# Function to generate a random dictionary
def generate_random_dict():
    # Generate random number of keys (from 1 to 10)
    num_keys = random.randint(1, 10)
    
    # Randomly select unique letters as keys
    keys = random.sample(string.ascii_lowercase, num_keys)
    
    # Create dictionary with random values (0-100)
    return {key: random.randint(0, 100) for key in keys}


# Function to generate a list of random dictionaries
def generate_dict_list():
    # Generate random number of dictionaries (from 2 to 10)
    num_dicts = random.randint(2, 10)
    
    # Create list of dictionaries
    return [generate_random_dict() for _ in range(num_dicts)]


# Function to merge dictionaries based on given rules
def merge_dicts(dict_list):
    # Create a dictionary to track all values by key
    temp_storage = {}
    
    # Iterate over dictionaries with index
    for idx, dictionary in enumerate(dict_list):
        # Iterate over each key-value pair in dictionary
        for key, value in dictionary.items():
            # If key not in storage, initialize list
            if key not in temp_storage:
                temp_storage[key] = []
            # Append tuple of (value, dictionary index)
            temp_storage[key].append((value, idx))
    
    # Create final result dictionary
    result = {}
    
    # Iterate over collected keys
    for key, values in temp_storage.items():
        # If key appears only once
        if len(values) == 1:
            # Add key as is
            result[key] = values[0][0]
        else:
            # Find max value and its dictionary index
            max_value, max_index = max(values, key=lambda x: x[0])
            # Rename key with dictionary index (1-based index)
            new_key = f"{key}_{max_index + 1}"
            # Store in result
            result[new_key] = max_value
    
    # Return merged dictionary
    return result


# Main execution block
if __name__ == "__main__":
    
    # Generate list of random dictionaries
    dict_list = generate_dict_list()
    
    # Print generated dictionaries
    print("Generated list of dictionaries:")
    print(dict_list)
    
    # Merge dictionaries based on rules
    merged_dict = merge_dicts(dict_list)
    
    # Print final merged dictionary
    print("\nMerged dictionary:")
    print(merged_dict)




########### STRING FUNCTIONS ##############

# Import regex module
import re

# Main function to process the text
def process_text(text):
    # Convert text to lowercase
    text = text.lower()
    
    # Replace "iz" with "is" only when it is a standalone word
    text = re.sub(r'\biz\b', 'is', text)
    
    # Split text into sentences
    sentences = [s.strip() for s in text.split('.') if s.strip()]
    
    # Extract last word from each sentence
    last_words = [sentence.split()[-1] for sentence in sentences]
    
    # Create new sentence from last words
    new_sentence = ' '.join(last_words) + '.'
    
    # Append new sentence to original text
    final_text = text.strip() + ' ' + new_sentence
    
    # Count whitespace characters
    whitespace_count = sum(1 for char in final_text if char.isspace())
    
    # Return results
    return final_text, whitespace_count






homework_text = """  
tHis iz your homeWork, copy these Text to variable.

You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

result_text, spaces = process_text(homework_text)

print(result_text)
print(spaces)