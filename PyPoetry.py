# load poem or phrase from file into variable
with open('poem.txt') as f:
    poem = f.read()

# load unix words dictionary into words variable
with open('c:/cygwin64/usr/share/dict/words') as w:
    words = w.read().splitlines()


# pick out all letters with unique, non-zero counts
def unique_letters(key_phrase):
    available_letters = set([c for c in key_phrase if c.isalpha()])
    letter_counts = [key_phrase.count(c) for c in available_letters]
    return [c for c in available_letters if letter_counts.count(key_phrase.count(c)) == 1]


# creates mapping with code as key for decoding
code_into_letter = {poem.count(c): c for c in unique_letters(poem)}

# creates mapping with letter as key for encoding
letter_into_code = {c: poem.count(c) for c in unique_letters(poem)}


# encode or decode the riddle
def riddle_me_this(riddle, mapping):
    return [mapping[key] for key in riddle]


# returns all words that can be used in a door riddle
def riddle_words(all_words, available_letters):
    return [riddle for riddle in all_words if set(riddle).issubset(available_letters)]


# returns all riddle codes for potential door riddles
def coded_riddles(all_words, mapping):
    return [riddle_me_this(word, mapping) for word in all_words]


# print list items to file, one item per line
def print_to_file(file_name, list_to_print):
    fo = open(file_name, "w")
    for item in list_to_print:
        fo.write(str(item) + "\n")
    fo.close()


# print dictionary to file, one key/value pair per line
def print_dict(file_name, dict_to_print):
    fo = open(file_name, "w")
    for key, value in dict_to_print.items():
        fo.write(str(key) + ": " + str(value) + "\n")
    fo.close()


# relevant solutions saved to variables
all_letters = unique_letters(poem)
word_list = riddle_words(words, all_letters)
riddle_codes = coded_riddles(word_list, letter_into_code)
answer_key = {tuple(code): ''.join(riddle_me_this(code, code_into_letter)) for code in riddle_codes}
longest_word = max(word_list, key=len)

#print comprehensive lists to files
print_to_file("word_list.txt", word_list)
print_to_file("riddle_list.txt", riddle_codes)
print_dict("answer_key.txt", answer_key)

if __name__ == '__main__':
    print("Available letters are: {}".format(', '.join(unique_letters(poem))))
    print("Letter mapping is: {}".format(letter_into_code))

    print("\nThe answer to the riddle: [56,38,44,56,29] is '{}'".format(''.join(riddle_me_this([56, 38, 44, 56, 29], code_into_letter))))
    print("\nThe longest riddle is {}".format(riddle_me_this(longest_word, letter_into_code)))
    print("Its solution is '{}'".format(longest_word))
    print("\nSee the text files for a complete riddle list, a complete word list, or an answer key with riddles and their solutions")
