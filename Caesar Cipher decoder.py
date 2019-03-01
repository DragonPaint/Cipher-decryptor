def cipher_decoder():
    translated_printout = ""
    cipher = input("Input your cipher:")
    for abc in range(25):
        abc += 1
        letter = 3
        translated_word = [str(abc), ": "]
        for letters in cipher:
            if ord(letters) != 95:
                ascii_numbers = ord(letters)
                ascii_numbers += abc
                if ascii_numbers >= 123:
                    ascii_numbers -= 26
                translated_word.append(chr(int(ascii_numbers)))
            else:
                translated_word.append(" ")
            letter += 1
        for translated_converter in translated_word:
            translated_printout += '%s' %translated_converter
        print(translated_printout)
        translated_word.clear()
        translated_printout = ""

cipher_decoder()
