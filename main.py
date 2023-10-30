# Importar as funções/módulos necessários do pacote 'src'
from src import criptografar
from src import descriptografar
from src import historico
from src import menu
from src import config
import os

# Verifica se este script é o ponto de entrada principal do programa
if __name__ == '__main__':
    os.system('cls')
    print(f'{" CRIPTOGRAFIA DE CESAR ":=^40}')

    # Inicia um loop para exibir o menu e lidar com as escolhas do usuário
    while True:
        # Obtém a escolha do usuário a partir do menu
        opcao = menu.menu()

        # Criptografar uma mensagem
        if opcao.lower() == 'c':
            os.system('cls')
            print(f'{" CRIPTOGRAFIA ":=^40}')

            # Solicita ao usuário que insira uma mensagem a ser criptografada
            mensagem = input('\nDigite a mensagem a ser criptografada: ')

            # Verifica se o tamanho da mensagem é inferior a 128 caracteres
            if len(mensagem) < 128:
                while True:
                    key = input(f'Digite sua chave (entre 1 e {len(config.alfabeto) - 1}): ')
                    if key.isnumeric():  # Verifica se a entrada é numérica
                        key = int(key)
                        if key <= len(config.alfabeto) - 1:  # Verifica se a chave está dentro do intervalo válido
                            break 
                        else:
                            print('Chave inválida! A chave deve estar no intervalo de 1 a', len(config.alfabeto) - 1)
                    else:
                        print('Digite um número!')

            # Criptografa a mensagem usando a chave fornecida
            text = criptografar.criptografar(mensagem, key)
            print(f'\nMensagem criptografada: {text}')
            historico.salvar_cripto(mensagem, key, text)

        # Descriptografar uma mensagem
        elif opcao.lower() == 'd':
            os.system('cls')
            print(f'{" DESCRIPTOGRAFAR ":=^40}')

            # Solicita ao usuário que insira uma mensagem criptografada a ser descriptografada
            text_cripto = input('\nDigite a mensagem a ser descriptografada: ')

            if len(text_cripto) < 128:
                while True:
                    key = input(f'Digite sua chave (entre 1 e {len(config.alfabeto) - 1}): ')
                    if key.isnumeric():  # Verifica se a entrada é numérica
                        key = int(key)
                        if key <= len(config.alfabeto) - 1:  # Verifica se a chave está dentro do intervalo válido
                            break  # Interrompe o loop se as condições forem atendidas
                        else:
                            print('Chave inválida! A chave deve estar no intervalo de 1 a', len(config.alfabeto) - 1)
                    else:
                        print('Digite um número!')

            # Descriptografa a mensagem usando a chave fornecida
            text = descriptografar.descriptografar(text_cripto, key)
            print(f'\nMensagem descriptografada: {text}')
            historico.salvar_decript(text_cripto, key, text)

        # Ver histórico
        elif opcao.lower() == 'h':
            os.system('cls')
            historico.historico()

        # Sair do programa
        elif opcao.lower() == 'f':
            os.system('cls')
            print('Obrigado por utilizar nosso software!')
            break




