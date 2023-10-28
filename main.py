from src import criptografar 
from src import descriptografar 
from src import historico
from src import menu
from src import config
import os


if __name__ == '__main__':
        print('======== CRIPTOGRAFIA DE CESAR ========')
        while True:
            opcao = menu.menu()
            if opcao.lower() == 'c':
                os.system('cls')
                print('========= CRIPTOGRAFAR ========')

                mensagem = input('\nDigite a mensagem a ser criptografada: ')
                
                if len(mensagem) < 130:
                    while True:
                        key = int(input(f'Digite sua chave (entre 1 e {len(config.alfabeto) - 1}): '))
                        if 1 <= key <= len(config.alfabeto) - 1:
                            break
                        else:
                            print('Chave inválida! A chave deve estar no intervalo de 1 a', len(config.alfabeto) - 1)

                text = criptografar.criptografar(mensagem, key)
                print(f'\nMensagem criptografada: {text}')
                historico.salvar_cripto(mensagem, key, text)

            elif opcao.lower() == 'd':
                os.system('cls')
                print('================ DESCRIPTOGRAFAR ================')

                text_cripto = input('\nDigite a mensagem a ser descriptografada: ')
                
                if len(text_cripto) < 130:
                    while True:
                        key = int(input(f'Digite sua chave (entre 1 e {len(config.alfabeto) - 1}): '))
                        if 1 <= key <= len(config.alfabeto) - 1:
                            break
                        else:
                            print('Chave inválida!')

                text = descriptografar.descriptografar(text_cripto, key)
                print(f'\nMensagem descriptografada: {text}')
                historico.salvar_decript(text_cripto, key, text)

            elif opcao.lower() == 'h':
                os.system('cls')
                historico.historico()
                
            elif opcao.lower() == 'f':
                print('Obrigado por utilizar nosso software!')
                break
