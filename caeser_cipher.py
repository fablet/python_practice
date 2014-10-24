def alphabet():
    alphabet_list = [" "]
    for c in xrange(ord('a'), ord('z')+1):
        alphabet_list.append(chr(c))

    return alphabet_list


def convert_to_num(phrase, alpha):
    phrase_list = list(phrase)
    numeric_phrase = []

    for letter in phrase_list:
        numeric_phrase.append(alpha.index(letter))

    return numeric_phrase


def convert_to_letter(phrase, alpha):
    letter_phrase = []

    for letter in phrase:
        letter_phrase.append(alpha[letter])

    phrase_output = ''.join(letter_phrase)

    return phrase_output


def crypt(code, shift):
    shifted_code = []

    for letter in code:
        if letter == 0:
            shifted_code.append(0)
        elif letter > 26:
            shifted_code.append((letter - 26) + shift)
        else:
            shifted_code.append(letter + shift)

    return shifted_code


alpha = alphabet()
encrypt_decrypt = ""
shift_value = 0

while True:
    encrypt_decrypt = raw_input("Would you like to encrypt or decrypt a message? >> ")
    if encrypt_decrypt == "encrypt" or "decrypt":
        break
    else:
        print("Sorry. I didn't get that.")

while True:
    raw_shift = raw_input("What is the shift amount for the cipher? >> ")
    try:
        shift_value = int(raw_shift)
        break
    except:
        continue

if encrypt_decrypt == 'encrypt':
    shift_value *= -1
raw_message = raw_input("What message would you like to {} >>  ".format("encrypt_decrypt"))
message = raw_message.strip().lower()
# shift_value = 3
# print(message)
coded_message = convert_to_num(message, alpha)
# print(coded_message)
apply_shift = crypt(coded_message, shift_value)
# print(apply_shift)
output_message = convert_to_letter(apply_shift, alpha)

print(output_message)