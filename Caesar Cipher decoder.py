from flexx import flx

all_programs_dict = {
    'caesar full': 'caesar_cipher_full_decoder',
    'caesar single': 'caesar_cipher_single_decoder',

}
keys_list = all_programs_dict.keys()


class Ciphers(flx.Widget):

    @flx.action
    def launcher(self):
        return flx.create_element('span', {},
                                  'Hello and welcome to this mess of a program.'),
        cipher_decoder()

    def cipher_decoder(self):
        return flx.create_element('span', {},
                                  'Options:'),
        flx.create_element('button', {'onclick': self.caesar_cipher_full_decoder},
                           'Caesar full')
        flx.create_element('button', {'onclick': self.caesar_cipher_single_decoder},
                           'Caesar single')

    def caesar_cipher_full_decoder(self):
        cipher = input("Input your cipher: ")
        for abc in range(1, 26):
            translated_word = [str(abc), ": "]
            caesar_cipher_translator(self, abc, cipher, translated_word)
            translated_word.clear()
        cipher_decoder()

    def caesar_cipher_translator(self, abc, cipher, translated_word):
        translated_printout = ""
        letter = 3
        for letters in cipher:
            if ord(letters) != 95:
                ascii_numbers = ord(letters)
                ascii_numbers += int(abc)
                if ascii_numbers >= 123:
                    ascii_numbers -= 26
                translated_word.append(chr(int(ascii_numbers)))
            else:
                translated_word.append(" ")

        for translated_converter in translated_word:
            translated_printout += '%s' % translated_converter
        letter += 1
        return flx.create_element('span', {},
                                  translated_printout),

    def caesar_cipher_single_decoder(self):
        cipher = input("Input your cipher: ")
        abc = input("Input positive offset: ")
        translated_word = [str(abc), ": "]
        caesar_cipher_translator(self, abc, cipher, translated_word)
        translated_word.clear()
        cipher_decoder()


app = flx.App(Ciphers)
app.export('Ciphers.html', link=0)
