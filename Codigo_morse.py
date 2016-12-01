import subprocess
import time

def play(time):
    subprocess.call(['afplay', '-t', str(time), 'beep.wav'])

def playlong():
    play(0.3)

def playshort():
    play(0.1)

def pause():
    time.sleep(0.3)

def codmorse(texto):
    morse = ''
    for i in range(len(texto)):
        if texto[i] == 'a':
            morse = morse + '._'
        elif texto[i] == 'b':
            morse = morse + '_...'
        elif texto[i] == 'c':
            morse = morse + '_._.'
        elif texto[i] == 'd':
            morse = morse + '_..'
        elif texto[i] == 'e':
            morse = morse + '.'
        elif texto[i] == 'f':
            morse = morse + '.._.'
        elif texto[i] == 'g':
            morse = morse + '__.'
        elif texto[i] == 'h':
            morse = morse + '....'
        elif texto[i] == 'i':
            morse = morse + '..'
        elif texto[i] == 'j':
            morse = morse + '.___'
        elif texto[i] == 'k':
            morse = morse + '_._'
        elif texto[i] == 'l':
            morse = morse + '._..'
        elif texto[i] == 'm':
            morse = morse + '__'
        elif texto[i] == 'n':
            morse = morse + '_.'
        elif texto[i] == 'o':
            morse = morse + '___'
        elif texto[i] == 'p':
            morse = morse + '.__.'
        elif texto[i] == 'q':
            morse = morse + '__._'
        elif texto[i] == 'r':
            morse = morse + '._.'
        elif texto[i] == 's':
            morse = morse + '...'
        elif texto[i] == 't':
            morse = morse + '_'
        elif texto[i] == 'u':
            morse = morse + '.._'
        elif texto[i] == 'v':
            morse = morse + '..._'
        elif texto[i] == 'w':
            morse = morse + '.__'
        elif texto[i] == 'x':
            morse = morse + '_.._'
        elif texto[i] == 'y':
            morse = morse + '_.__'
        elif texto[i] == 'z':
            morse = morse + '__..'
        elif texto[i] == '0':
            morse = morse + '_____'
        elif texto[i] == '1':
            morse = morse + '.____'
        elif texto[i] == '2':
            morse = morse + '..___'
        elif texto[i] == '3':
            morse = morse + '...__'
        elif texto[i] == '4':
            morse = morse + '...._'
        elif texto[i] == '5':
            morse = morse + '.....'
        elif texto[i] == '6':
            morse = morse + '_....'
        elif texto[i] == '7':
            morse = morse + '__...'
        elif texto[i] == '8':
            morse = morse + '___..'
        elif texto[i] == '9':
            morse = morse + '____.'
        elif texto[i] == ',':
            morse = morse + '__..__'
        elif texto[i] == '.':
            morse = morse + '._._._'
        elif texto[i] == '?':
            morse = morse + '..__..'
        elif texto[i] == ';':
            morse = morse + '_._._.'
        elif texto[i] == ':':
            morse = morse + '___...'
        elif texto[i] == '\'':
            morse = morse + '.____.'
        elif texto[i] == '-':
            morse = morse + '_...._'
        elif texto[i] == '/':
            morse = morse + '_.._.'
        elif texto[i] == '(':
            morse = morse + '_.__.'
        elif texto[i] == ')':
            morse = morse + '_.__._'
        elif texto[i] == ' ':
            morse = morse + ' '
        else:
            print 'Seu texto possui caracteres invalidos. Por favor, digite apenas letras minusculas sem acento, numeros, virgula, ponto, interrogacao, ponto e virgula, dois pontos, apostrofo, hifen, barra, parenteses ou espaco.'
            break
        if texto[i] != ' ':
            morse = morse + ' '
    return morse

def morseToText(morsetext):
    texto = ''
    letra = ''
    morsetext = morsetext + ' '
    for i in range(len(morsetext)):
        if i != len(morsetext):
            if morsetext[i] != ' ':
                letra = letra + morsetext[i]
            elif morsetext[i] == ' ' and morsetext[i-1] != ' ':
                if letra == '._':
                    texto = texto + 'a'
                elif letra == '_...':
                    texto = texto + 'b'
                elif letra == '_._.':
                    texto = texto + 'c'
                elif letra == '_..':
                    texto = texto + 'd'
                elif letra == '.':
                    texto = texto + 'e'
                elif letra == '.._.':
                    texto = texto + 'f'
                elif letra == '__.':
                    texto = texto + 'g'
                elif letra == '....':
                    texto = texto + 'h'
                elif letra == '..':
                    texto = texto + 'i'
                elif letra == '.___':
                    texto = texto + 'j'
                elif letra == '_._':
                    texto = texto + 'k'
                elif letra == '._..':
                    texto = texto + 'l'
                elif letra == '__':
                    texto = texto + 'm'
                elif letra == '_.':
                    texto = texto + 'n'
                elif letra == '___':
                    texto = texto + 'o'
                elif letra == '.__.':
                    texto = texto + 'p'
                elif letra == '__._':
                    texto = texto + 'q'
                elif letra == '._.':
                    texto = texto + 'r'
                elif letra == '...':
                    texto = texto + 's'
                elif letra == '_':
                    texto = texto + 't'
                elif letra == '.._':
                    texto = texto + 'u'
                elif letra == '..._':
                    texto = texto + 'v'
                elif letra == '.__':
                    texto = texto + 'w'
                elif letra == '_.._':
                    texto = texto + 'x'
                elif letra == '_.__':
                    texto = texto + 'y'
                elif letra == '__..':
                    texto = texto + 'z'
                elif letra == '_____':
                    texto = texto + '0'
                elif letra == '.____':
                    texto = texto + '1'
                elif letra == '..___':
                    texto = texto + '2'
                elif letra == '...__':
                    texto = texto + '3'
                elif letra == '...._':
                    texto = texto + '4'
                elif letra == '.....':
                    texto = texto + '5'
                elif letra == '_....':
                    texto = texto + '6'
                elif letra == '__...':
                    texto = texto + '7'
                elif letra == '___..':
                    texto = texto + '8'
                elif letra == '____.':
                    texto = texto + '9'
                elif letra == '__..__':
                    texto = texto + ','
                elif letra == '._._._':
                    texto = texto + '.'
                elif letra == '..__..':
                    texto = texto + '?'
                elif letra == '_._._.':
                    texto = texto + ';'
                elif letra == '___...':
                    texto = texto + ':'
                elif letra == '.____.':
                    texto = texto + '\''
                elif letra == '_...._':
                    texto = texto + '-'
                elif letra == '_.._.':
                    texto = texto + '/'
                elif letra == '_.__.':
                    texto = texto + '('
                elif letra == '_.__._':
                    texto = texto + ')'
                else:
                    print 'Seu texto possui caracteres invalidos. Por favor, digite apenas letras minusculas sem acento, numeros, virgula, ponto, interrogacao, ponto e virgula, dois pontos, apostrofo, hifen, barra, parenteses ou espaco.'
                    break
                letra = ''
            elif morsetext[i] == ' ' and morsetext[i - 1] == ' ':
                texto = texto + ' '
    return texto

def morsesound(morsetext):
    for i in range(len(morsetext)):
        if morsetext[i] == '.':
            playshort()
        elif morsetext[i] == '_':
            playlong()
        elif morsetext[i] == ' ':
            pause()
        else:
            print 'Seu texto possui caracteres invalidos. Por favor, digite apenas letras minusculas sem acento, numeros, virgula, ponto, interrogacao, ponto e virgula, dois pontos, apostrofo, hifen, barra, parenteses ou espaco.'

# texto = 'ana elisa'
# morsetext = codmorse(texto)
# print morsetext
print morseToText('._ _. ._  . ._.. .. ... ._')