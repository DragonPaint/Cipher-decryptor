import random
all_programs_dict = {
    'caesar full': 'caesar_cipher_full_decoder',
    'caesar single': 'caesar_cipher_single_decoder',
    '123 cipher': 'int_cipher_decoder',
    '-123 cipher': 'neg_int_cipher_decoder',
}


def caesar_cipher_full_decoder():
    cipher = input("Input your cipher: ")
    for abc in range(1, 26):
        translated_word = [str(abc), ": "]
        caesar_cipher_translator(abc, cipher, translated_word)
        translated_word.clear()

    cipher_decoder()


def caesar_cipher_translator(abc, cipher, translated_word):
    translated_printout = ""
    letter = 3
    for letters in cipher:
        if 96 <= ord(letters) <= 123:
            ascii_numbers = ord(letters)
            ascii_numbers += int(abc)
            if ascii_numbers >= 123:
                ascii_numbers -= 26
            translated_word.append(chr(int(ascii_numbers)))
        elif 64 <= ord(letters) <= 91:
            ascii_numbers = ord(letters)
            ascii_numbers += int(abc)
            if ascii_numbers >= 91:
                ascii_numbers -= 26
            translated_word.append(chr(int(ascii_numbers)))
        elif ord(letters) == 95 and ord(letters) == 32:
            translated_word.append(" ")
        else:
            translated_word.append(letters)

    for translated_converter in translated_word:
        translated_printout += '%s' % translated_converter
    print(translated_printout)
    letter += 1


def caesar_cipher_single_decoder():
    cipher = input("Input your cipher: ")
    abc = input("Input positive offset: ")
    translated_word = [str(abc), ": "]
    caesar_cipher_translator(abc, cipher, translated_word)
    translated_word.clear()
    cipher_decoder()


def int_cipher_decoder():
    cipher = input("Input your cipher: ")
    abc = input("Input positive offset number: ")
    abcd = abc
    if len(abc) <= len(cipher):
        diff = len(cipher) - len(abc)
        abcd = abc * int(diff/len(abc)) + 2*abc
    translated_word = [str(abc), ": "]
    translated_printout = ""
    abc_itteration = 1
    for letters in cipher:
        if 96 <= ord(letters) <= 123:
            ascii_numbers = ord(letters)
            ascii_numbers += int(abcd[int(abc_itteration)])
            if ascii_numbers >= 123:
                ascii_numbers -= 26
            translated_word.append(chr(int(ascii_numbers)))
        elif 64 <= ord(letters) <= 91:
            ascii_numbers = ord(letters)
            ascii_numbers += int(abcd[int(abc_itteration)])
            if ascii_numbers >= 91:
                ascii_numbers -= 26
            translated_word.append(chr(int(ascii_numbers)))
        elif ord(letters) == 95 and ord(letters) == 32:
            translated_word.append(" ")
        else:
            translated_word.append(letters)
        abc_itteration += 1

    for translated_converter in translated_word:
        translated_printout += '%s' % translated_converter
    print(translated_printout)

    translated_word.clear()
    cipher_decoder()


def neg_int_cipher_decoder():
    cipher = input("Input your cipher: ")
    abc = input("Input positive offset number: ")
    abcd = abc
    if len(abc) <= len(cipher):
        diff = len(cipher) - len(abc)
        abcd = abc * int(diff/len(abc)) + 2*abc
    translated_word = [str(abc), ": "]
    translated_printout = ""
    abc_itteration = 1
    for letters in cipher:
        if 96 <= ord(letters) <= 123:
            ascii_numbers = ord(letters)
            ascii_numbers += int(abcd[int(abc_itteration)])
            if ascii_numbers >= 123:
                ascii_numbers -= 26
            translated_word.append(chr(int(ascii_numbers)))
        elif 64 <= ord(letters) <= 91:
            ascii_numbers = ord(letters)
            ascii_numbers += int(abcd[int(abc_itteration)])
            if ascii_numbers >= 91:
                ascii_numbers -= 26
            translated_word.append(chr(int(ascii_numbers)))
        elif ord(letters) == 95 and ord(letters) == 32:
            translated_word.append(" ")
        else:
            translated_word.append(letters)
        abc_itteration += 1

    for translated_converter in translated_word:
        translated_printout += '%s' % translated_converter
    print(translated_printout)

    translated_word.clear()
    cipher_decoder()


def random_int_cipher_decoder():
    abc_printout = "The key: "
    cipher = input("Input your cipher: ")
    size = input("Do you want to go between: 1-25 or 1-9?")
    abc_length = input("Input length of key: ")
    abc = [int(abc_length)]
    if size == "1-25":
        while len(abc) < int(abc_length):
            abc.append(random.randint(1, 25))
    else:
        while len(abc) < int(abc_length):
            abc.append(random.randint(1, 9))
    translated_word = [str(abc), ": "]
    for abc_converter in abc:
        abc_printout += '%s, ' % abc_converter
    print(abc_printout)
    if len(abc) <= len(cipher):
        diff = len(cipher) - len(abc)
        abc = (abc * int(diff / len(abc)) + 2 * abc)
    translated_printout = ""
    abc_itteration = 0
    for letters in cipher:
        if 96 <= ord(letters) <= 123:
            ascii_numbers = ord(letters)
            ascii_numbers += abc[abc_itteration]
            if ascii_numbers >= 123:
                ascii_numbers -= 26
            translated_word.append(chr(int(ascii_numbers)))
        elif 64 <= ord(letters) <= 91:
            ascii_numbers = ord(letters)
            ascii_numbers += abc[abc_itteration]
            if ascii_numbers >= 91:
                ascii_numbers -= 26
            translated_word.append(chr(int(ascii_numbers)))
        elif ord(letters) == 95 and ord(letters) == 32:
            translated_word.append(" ")
        else:
            translated_word.append(letters)
        abc_itteration += 1

    for translated_converter in translated_word:
        translated_printout += '%s' % translated_converter
    print(translated_printout)

    translated_word.clear()
    abc.clear()
    cipher_decoder()


def launcher():
    print("Hello and welcome to this mess of a program.")
    cipher_decoder()


def cipher_decoder():
    decoder_programs = "Options: "
    keys_list = all_programs_dict.keys()
    for key in keys_list:
        decoder_programs += '%s, ' % key
    print(decoder_programs)
    choice = input("What option do you want?")
    if choice == 'caesar full':
        caesar_cipher_full_decoder()
    elif choice == 'caesar single':
        caesar_cipher_single_decoder()
    elif choice == '123 cipher':
        int_cipher_decoder()
    elif choice == '-123 cipher':
        neg_int_cipher_decoder()
    else:
        print("Error I shall send you back upp because, YOU SHALL NOT PASS!!!")
        cipher_decoder()


launcher()
