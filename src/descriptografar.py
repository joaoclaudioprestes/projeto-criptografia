from src import rotacionar
from src import config

def cesar_decript(cesar2, key):
    text_decript = ''
    for i in cesar2: 
        if i in config.alfabeto:
            index = config.alfabeto.find(i)
            new_index = (index - int(key)) % len(config.alfabeto)
            rotacionar.novo_index(new_index)
            text_decript += config.alfabeto[new_index]
        else:
            text_decript += i 

    return text_decript

def cesar_decript2(text_cripto, key):
    text_decript = ''
    for i in text_cripto:
        if i in config.alphabet:
            index = config.alphabet.find(i)
            new_index = (index - int(key)) % len(config.alphabet)
            rotacionar.novo_index(new_index)
            text_decript += config.alphabet[new_index]
        else:
            text_decript += i

    return text_decript

def palavra_hex(text_cripto):
    hex_palavra = ''.join(f'{ord(letra):02x}' for letra in text_cripto)

    return hex_palavra

def descriptografar(text_cripto, key):
    # binario = palavra_hex(text_cripto)
    cesar2 = cesar_decript2(text_cripto, key)
    cesar = cesar_decript(cesar2, key)

    return cesar
