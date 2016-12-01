import Codigo_morse

class morse:
    def seta_texto(self, texto):
        self.x = texto

    def imprime_texto(self):
        print self.x

    def imprime_morse(self):
        self.morsetext =  Codigo_morse.codmorse(self.x)
        print self.morsetext

    def toca_som(self):
        Codigo_morse.morsesound(self.morsetext)

texto = raw_input()
meu_morse = morse()

meu_morse.seta_texto(texto)
meu_morse.imprime_texto()
meu_morse.imprime_morse()
meu_morse.toca_som()