from src import gerar_id 
from src import config
from tabulate import tabulate

def salvar_cripto(mensagem, key, text):
    salvar_operacao = input('Deseja salvar essa operação: [S] ou [N]: ')

    if salvar_operacao.lower() == 's':
        new_id = gerar_id.gerar_id()
        update = {'id': new_id, 'mensagem': mensagem, 'criptografada': text, 'key': key, 'descriptografada': None}
        config.banco_historico.append(update)
        print('Operação salva!')

    else:
        print('Operação finalizada!')

def salvar_decript(text_cripto, key, text):
    salvar_operacao = input('Deseja salvar essa operação: [S] ou [N]: ')

    if salvar_operacao.lower() == 's':
        new_id = gerar_id.gerar_id()
        update = {'id': new_id, 'mensagem': text, 'criptografada': text_cripto, 'key': key, 'descriptografada': text}
        config.banco_historico.append(update)
        print('Operação salva!')

    else:
        print('Operação finalizada!')

def historico():
    print('============== HISTÓRICO ==============')
    
    data_list = []
    for item in config.banco_historico:
        row = [item['id'], item['mensagem'], item['criptografada'], item['key'], item['descriptografada']]
        data_list.append(row)

    header = ["Id", "Mensagem", "Criptografada", "Chave", "Descriptografada"]

    table = tabulate(data_list, headers=header, tablefmt="grid")

    print(table)
