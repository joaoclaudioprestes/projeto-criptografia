from src import rotacionar
from src import config

def cesar_encript(mensagem, key):
    text_cripto = ''

    for i in mensagem:
        if i in config.alfabeto:
            index = config.alfabeto.find(i)  # Encontra o índice do caractere no alfabeto.
            new_index = (index + int(key)) % len(config.alfabeto)
            # Calcula o novo índice com base na chave e no tamanho do alfabeto.
            rotacionar.novo_index(new_index)
            # Chama uma função "new_index" do módulo "rotacionar".
            text_cripto += config.alfabeto[new_index]
        else:
            text_cripto += i

    return text_cripto

def cesar_encript2(cesar, key):
    text_cripto = ''  
    for i in cesar:
        if i in config.alphabet:
            index = config.alphabet.find(i)
            new_index = (index + int(key)) % len(config.alphabet)
            rotacionar.novo_index(new_index)
            text_cripto += config.alphabet[new_index]

        else:
            text_cripto += i

    return text_cripto

def criptografar(mensagem, key):
    cesar = cesar_encript(mensagem, key)
    cesar2 = cesar_encript2(cesar, key)

    return cesar2
