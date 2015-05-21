poem = '''a narrow fellow in the grass
occasionally rides;
you may have met him, did you not,
his notice sudden is.

the grass divides as with a comb,
a spotted shaft is seen;
and then it closes at your feet
and opens further on.

he likes a boggy acre,
a floor too cool for corn.
yet when a child, and barefoot,
i more than once, at morn,

have passed, i thought, a whip-lash
unbraiding in the sun,
when, stooping to secure it,
it wrinkled, and was gone.

several of nature's people
i know, and they know me;
i feel for them a transport
of cordiality;

but never met this fellow,
attended or alone,
without a tighter breathing,
and zero at the bone.'''

#load unix words dictionary into words variable
with open('c:/cygwin64/usr/share/dict/words') as w:
    words = w.read().splitlines()


# pick out all unique, non-zero count letters
def unique_letters(key_phrase):
    available_letters = set([c for c in key_phrase if c.isalpha()])
    letter_counts = [key_phrase.count(c) for c in available_letters]
    return [c for c in available_letters if letter_counts.count(key_phrase.count(c)) == 1]


#creates mapping with code as key
code_into_letter = {poem.count(c): c for c in unique_letters(poem)}

#creates mapping with letter as key
letter_into_code = {c: poem.count(c) for c in unique_letters(poem)}


# encode (with letter_into_code mapping) or decode (with code_into_letter mapping) the riddle
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


# def check_decoding(real_words, code, mapping):
#     decode = ''.join(riddle_me_this(code, mapping))
#     if decode in real_words:
#         return decode
#     else:
#         check_decoding(real_words, code, mapping)


# relevant solutions saved to variables
all_letters = unique_letters(poem)
word_list = riddle_words(words, all_letters)
riddle_codes = coded_riddles(word_list, letter_into_code)
answer_key = {tuple(code): ''.join(riddle_me_this(code, code_into_letter)) for code in riddle_codes}
longest_word = max(word_list, key=len)


#print outputs
print("Available letters are: {}".format(', '.join(unique_letters(poem))))
print("Letter mapping is: {}".format(letter_into_code))

print("The answer to the riddle: [56,38,44,56,29] is '{}'".format(''.join(riddle_me_this([56, 38, 44, 56, 29], code_into_letter))))
print("The longest riddle is {}".format(riddle_me_this(longest_word, letter_into_code)))


print_to_file("word_list.txt", word_list)
print_to_file("riddle_list.txt", riddle_codes)
print_dict("answer_key.txt", answer_key)
