from src import config

def novo_index(new_index):
    if new_index >= len(config.alfabeto):
        new_index = new_index - len(config.alfabeto)
        return new_index
    elif new_index < 0:
        new_index = new_index + len(config.alfabeto)
        return new_index