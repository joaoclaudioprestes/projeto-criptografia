from src import config

def novo_index(new_index):
    if new_index >= len(config.alfabeto):
        # Ajusta o índice para dentro do alcance subtraindo o tamanho do alfabeto do índice fornecido
        new_index = new_index - len(config.alfabeto)
        return new_index 
    
    elif new_index <= 0:
        # Ajusta o índice somando o tamanho do alfabeto ao índice fornecido para trazê-lo para dentro do intervalo válido
        new_index = new_index + len(config.alfabeto)
        return new_index
