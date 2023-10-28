from src import rotacionar
from src import config

def cesar_encript(mensagem, key):
    text_cripto = ''
    for i in mensagem: 
        if i in config.alfabeto:
            index = config.alfabeto.find(i)
            new_index = (index + key) % len(config.alfabeto)
            rotacionar.novo_index(new_index)
            text_cripto += config.alfabeto[new_index]
        else:
            text_cripto += i 
    
    return text_cripto

def cesar_encript2(cesar, key):
    text_cripto = ''
    for i in cesar:
        if i in config.alphabet:
            index = config.alphabet.find(i)
            new_index = (index + key) % len(config.alphabet)
            rotacionar.novo_index(new_index)
            text_cripto += config.alphabet[new_index]
        else:
            text_cripto += i

    return text_cripto

def palavra_hex(cesar2):
    palavra_hex = ''.join(f'{ord(letra):02x}' for letra in cesar2)

    return palavra_hex

def criptografar(mensagem, key):
    cesar = cesar_encript(mensagem, key)
    cesar2 = cesar_encript2(cesar, key)
    # binario = palavra_hex(cesar2)

    return cesar2
