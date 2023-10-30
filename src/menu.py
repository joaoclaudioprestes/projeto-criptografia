# Importa o modulo "textwrap", ele é usado nesse algoritmo para ajustar o texto do menu removendo a indentação e tornando-o mais legível
import textwrap

def menu():
    menu_text = """\n
    ================ MENU ================
    [c]\tCriptografar
    [d]\tDescriptografar
    [h]\tHistórico
    [f]\tFinalizar
    => """
    
    return input(textwrap.dedent(menu_text))
    # Utiliza a função "textwrap.dedent" para remover a indentação da string do menu.