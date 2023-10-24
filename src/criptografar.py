from src import rotacionar
from src import config

def criptografar(mensagem, key):
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
    