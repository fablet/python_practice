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

#assign available letters to unique variable
unique = set([c for c in poem if c.isalpha()])

#creates mapping with code as key
code_into_letter = {poem.count(c): c for c in unique}

#creates mapping with letter as key
letter_into_code = {c: poem.count(c) for c in unique}

#load unix words dictionary into words variable
with open('c:/cygwin64/usr/share/dict/words') as w:
    words = w.read().splitlines()


# given numeric list, solve the riddle
def riddle_me_this(riddle, mapping):
    return [mapping[key] for key in riddle]


# returns all words that can be used in a door riddle
def riddle_words(all_words, available_letters):
    return [riddle for riddle in all_words if set(riddle).issubset(available_letters)]


# returns all riddle codes for potential door riddles
def coded_riddles(all_words, mapping):
    return [riddle_me_this(word, mapping) for word in all_words]


def print_to_file(file_name, list_to_print):
    fo = open(file_name, "w")
    for item in list_to_print:
        fo.write(str(item) + "\n")
    fo.close()


def print_dict(file_name, dict_to_print):
    fo = open(file_name, "w")
    for key, value in dict_to_print.items():
        fo.write(str(key) + ": " + str(value) + "\n")
    fo.close()


def check_decoding(real_words, code, mapping):
    decode = ''.join(riddle_me_this(code, mapping))
    if decode in real_words:
        return decode
    else:
        check_decoding(real_words, code, mapping)


# relevant solutions saved to variables
word_list = riddle_words(words, unique)
riddle_codes = coded_riddles(word_list, letter_into_code)
answer_key = {word: riddle_me_this(word, letter_into_code) for word in word_list}
longest_word = max(word_list, key=len)


#print outputs
print("Available letters are: {}".format(', '.join(unique)))
print("Letter mapping is: {}".format(letter_into_code))

print("The answer to the riddle: [56,38,44,56,29] is '{}'".format(check_decoding(word_list, [56, 38, 44, 56, 29], code_into_letter)))
print("The longest riddle is {}".format(riddle_me_this(longest_word, letter_into_code)))

print_to_file("word_list.txt", word_list)
print_to_file("riddle_list.txt", riddle_codes)
print_dict("answer_key.txt", answer_key)
