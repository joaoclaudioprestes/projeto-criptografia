import random  # Importa a biblioteca random para geração de números aleatórios
from src import config  # Importa o arquivo de configuração

def gerar_chave():
    key = random.randint(1, len(config.alfabeto) - 1)
    
    return key 

