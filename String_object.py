# Import the 're' module to work with regular expressions
import re

# Store the original text in a multiline string variable
homework_text = """  
tHis iz your homeWork, copy these Text to variable.

You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

# Convert the entire text to lowercase for normalization
normalized_text = homework_text.lower()

# Replace the word "iz" with "is" only when it appears as a whole word
corrected_text = re.sub(r'\biz\b', 'is', normalized_text)

# Split the text into sentences using the period as a delimiter
sentences = corrected_text.split('.')

# Create an empty list to store cleaned sentences
clean_sentences = []

# Iterate through each sentence
for sentence in sentences:
    # Remove leading and trailing whitespace
    sentence = sentence.strip()
    # Check if the sentence is not empty
    if sentence:
        # Add the cleaned sentence to the list
        clean_sentences.append(sentence)

# Create a list to store the last word of each sentence
last_words = []

# Iterate through each cleaned sentence
for sentence in clean_sentences:
    # Split the sentence into words
    words = sentence.split()
    # Append the last word of the sentence to the list
    last_words.append(words[-1])

# Create a new sentence by joining the last words with spaces
new_sentence = ' '.join(last_words) + '.'

# Append the new sentence to the end of the corrected text
final_text = corrected_text.strip() + ' ' + new_sentence

# Initialize a counter for whitespace characters
whitespace_count = 0

# Iterate through each character in the final text
for char in final_text:
    # Check if the character is any type of whitespace (space, tab, newline, etc.)
    if char.isspace():
        # Increment the counter
        whitespace_count += 1

# Print the final processed text
print("Final text:\n")
print(final_text)

# Print the total number of whitespace characters
print("\nNumber of whitespace characters:", whitespace_count)