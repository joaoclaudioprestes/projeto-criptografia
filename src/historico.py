from src import gerar_id 
from src import config
import os
from tabulate import tabulate  # Importa a função tabulate para criar tabelas

def salvar_cripto(mensagem, key, text):
    salvar_operacao = input('Deseja salvar essa operação: [S] ou [N]: ')

    if salvar_operacao.lower() == 's':
        new_id = gerar_id.gerar_id()  # Gera um novo ID único para a operação
        update = {
            'id': new_id,
            'mensagem': mensagem,
            'criptografada': text,
            'key': key,
            'descriptografada': None
        }
        config.banco_historico.append(update)  # Adiciona os detalhes da operação ao histórico
        os.system('cls')
        print(f'{" OPERAÇÃO SALVA! ":=^40}')
    else:
        os.system('cls')
        print(f'{" OPERAÇÃO FINALIZADA! ":=^40}')

def salvar_decript(mensagem, key, text):
    salvar_operacao = input('Deseja salvar essa operação: [S] ou [N]: ')

    if salvar_operacao.lower() == 's':
        new_id = gerar_id.gerar_id()
        update = {
            'id': new_id,
            'mensagem': text,
            'criptografada': mensagem,
            'key': key,
            'descriptografada': text
        }
        config.banco_historico.append(update)
        os.system('cls')
        print(f'{" OPERAÇÃO SALVA! ":=^40}')
    else:
        os.system('cls')
        print(f'{" OPERAÇÃO FINALIZADA! ":=^40}')

def historico():
    print(f'{" HISTÓRICO ":=^40}')

    data_list = []

    for item in config.banco_historico:  # Itera sobre as operações no histórico
        row = [item['id'], item['mensagem'], item['criptografada'], item['key'], item['descriptografada']]
        data_list.append(row)

    header = ["Id", "Mensagem", "Criptografada", "Chave", "Descriptografada"]

    # Cria uma tabela a partir dos detalhes do histórico
    table = tabulate(data_list, headers=header, tablefmt="grid")

    print(table)
