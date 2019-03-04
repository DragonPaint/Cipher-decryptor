all_programs_dict = {
    'caesar full': 'caesar_cipher_full_decoder',
    'caesar single': 'caesar_cipher_single_decoder',

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
    for letters in cipher.lower():
        if ord(letters) != 95 or ord(letters) != 32:
            ascii_numbers = ord(letters)
            ascii_numbers += int(abc)
            if ascii_numbers >= 123:
                ascii_numbers -= 26
            translated_word.append(chr(int(ascii_numbers)))
        else:
            translated_word.append(" ")

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
    else:
        print("Error I shall send you back upp because, YOU SHALL NOT PASS!!!")
        cipher_decoder()


launcher()
