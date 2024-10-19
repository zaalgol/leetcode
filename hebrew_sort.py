import re

def sort_paragraph_hebrew_alphabet(paragraph: str) -> str:
    hebrew_order = 'ABGDHVZJTYKLMNSIPXQRWUCEFO'

    # Create a dictionary that maps each character to its position in the Hebrew alphabet
    hebrew_index = {char: index for index, char in enumerate(hebrew_order)}

    # Remove punctuation from the paragraph and convert it to lowercase.
    words = re.findall(r'\b\w+\b', paragraph.lower())

    def hebrew_sort_key(word):
        # Convert each letter in the word to its corresponding index in the Hebrew alphabet
        # If the letter is not in the hebrew_index (Like numbers), it's treated as a large value to push it to the end
        return [hebrew_index.get(char.upper(), float('inf')) for char in word]

    sorted_words = sorted(words, key=hebrew_sort_key)
    
    return ' '.join(sorted_words)

# Usage Examples :

# 1.
paragraph = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
hebrew_sorted_paragraph = sort_paragraph_hebrew_alphabet(paragraph)
print(hebrew_sorted_paragraph)
# output: "adipiscing aliqua amet do dolor dolore tempor labore lorem magna sit sed incididunt ipsum ut consectetur et elit eiusmod"

# 2.
paragraph = "adipiscing aliqua amet do dolor dolore tempor labore lorem magna sit sed incididunt ipsum ut consectetur et elit eiusmod"
hebrew_sorted_paragraph = sort_paragraph_hebrew_alphabet(paragraph)
print(hebrew_sorted_paragraph)
# Output: The same of the input, because the the input was already sorted in a hebrew oredr.

# 3.
paragraph = "Add adg bdf ag bcf bcz. Aggg ad aga eaa xpi cfrty? "
hebrew_sorted_paragraph = sort_paragraph_hebrew_alphabet(paragraph)
print(hebrew_sorted_paragraph)
# Output: "ag aga aggg ad adg add bdf bcz bcf xpi cfrty eaa". If 2 words start with the same letter, it will sort by the next letter, and so on...


