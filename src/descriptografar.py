from src import rotacionar
from src import config

def descriptografar(mensagem, key):
    text_decript = ''
    for i in mensagem: 
        if i in config.alfabeto:
            index = config.alfabeto.find(i)
            new_index = (index - key) % len(config.alfabeto)
            rotacionar.novo_index(new_index)
            text_decript += config.alfabeto[new_index]
        else:
            text_decript += i 
            
    return text_decript
