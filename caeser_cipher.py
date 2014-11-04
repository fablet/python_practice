#because I am too lazy to type out the entire alphabet into an array 
#index 0 is set to " " to allow for spaces between words when decoding the phrase
def alphabet():
    alphabet_list = [" "]
    for c in xrange(ord('a'), ord('z')+1):
        alphabet_list.append(chr(c))

    return alphabet_list

#takes the original phrase (whether it is encrypted or not) 
#and returns an array of numbers based on their value/index in the original alphabet array
def convert_to_num(phrase, alpha):
    phrase_list = list(phrase)
    numeric_phrase = []

    for letter in phrase_list:
        numeric_phrase.append(alpha.index(letter))

    return numeric_phrase

#takes in an array of numbers and returns an array of letters 
#based on their index/value in the original alphabet array
def convert_to_letter(phrase, alpha):
    letter_phrase = []

    for letter in phrase:
        letter_phrase.append(alpha[letter])

    phrase_output = ''.join(letter_phrase)

    return phrase_output

#takes in an array of numbers created by convert_to_num
#and applies the shift value to encrypt or decrypt the cipher
#returns an array of numbers to be converted back to letters in convert_to_letter
def crypt(code, shift):
    shifted_code = []

    for letter in code:
        if letter == 0:
            shifted_code.append(0)
        elif (letter + shift) > 26:
            shifted_code.append((letter + shift) - 26)
        else:
            shifted_code.append(letter + shift)

    return shifted_code


#initialize variables to generate an alphabet array
#and set a default value for variables that will latter be set by user input
alpha = alphabet()
encrypt_decrypt = "decrypt"
shift_value = 0

#asks user input for whether we will be encrypting or decrypting a message
#loops until a valid response is input
while True:
    encrypt_decrypt = raw_input("Would you like to encrypt or decrypt a message? >> ")
    if encrypt_decrypt == "encrypt" or "decrypt":
        break
    else:
        print("Sorry. I didn't get that.")

#asks user input for the amount of shift to apply when encrypting or decrypting
#loops until user inputs an integer between 1 and 25
while True:
    raw_shift = raw_input("What is the shift amount for the cipher? >> ")
    try:
        shift_value = int(raw_shift)
        if shift_value >= 1 and shift_value <= 25:
            break
    except:
        print("Sorry. I didn't get that.")
        continue
    

#adds a negative value to shift for encryption
if encrypt_decrypt == 'encrypt':
    shift_value *= -1

#receives user input to encrypt or decrypt and sets it to lowercase 
raw_message = raw_input("What message would you like to {} >>  ".format(encrypt_decrypt))
message = raw_message.strip().lower()

#processes the caeser cipher
# shift_value = 3
# print(message)
coded_message = convert_to_num(message, alpha)
# print(coded_message)
apply_shift = crypt(coded_message, shift_value)
# print(apply_shift)
output_message = convert_to_letter(apply_shift, alpha)

print("Your {}ed message is:".format(encrypt_decrypt))
print(output_message)