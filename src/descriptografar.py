from src import rotacionar
from src import config

def cesar_decript(cesar2, key):
    text_decript = ''
    for i in cesar2:
        if i in config.alfabeto:  # Verifica se o caractere está no alfabeto
            index = config.alfabeto.find(i)  # Encontra o índice do caractere no alfabeto
            new_index = (index - int(key)) % len(config.alfabeto)  # Calcula o novo índice após a descriptografia
            rotacionar.novo_index(new_index)  # Realiza a rotação para o novo índice
            text_decript += config.alfabeto[new_index]  # Adiciona o caractere descriptografado ao texto
        else:
            text_decript += i  # Se não estiver no alfabeto, mantém o caractere original

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

def descriptografar(text_cripto, key):
    cesar2 = cesar_decript2(text_cripto, key)
    cesar = cesar_decript(cesar2, key)

    return cesar

