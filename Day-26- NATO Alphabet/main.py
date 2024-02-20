import warnings
import pandas
# Suppress DeprecationWarning related to PyArrow
warnings.filterwarnings("ignore", category=DeprecationWarning)


data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_to_dict = data.to_dict()

new_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(new_dict)

word = input("Enter a word: ").upper()

# Method 01
# word_list = []
# for letter in word:
#     letter_c = letter
#     for n in new_dict:
#         if letter_c == n:
#             word_list.append(new_dict[n])
# print(word_list)

# Method 02
output = [new_dict[letter] for letter in word]
print(output)
