import random
from src import config

def gerar_chave():
    key = random.randint(1, len(config.alfabeto) - 1)
    return key