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