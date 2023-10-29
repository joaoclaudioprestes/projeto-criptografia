from PySimpleGUI import *
from src import criptografar, descriptografar

layout = [
    [Text('Criptografia de Cesar', justification='center', font=('Montserrat', 14, 'bold'), size=(40, 1))],
    [Text('Sobre:', background_color="#000000", text_color="#ffffff", font=('Montserrat', 11, 'bold'))],
    [
        Text(
            'A Criptografia de César é uma das técnicas mais simples e conhecidas de criptografia. '
            'Recebe esse nome por causa de Júlio César, que supostamente a teria utilizado para '
            'comunicações secretas durante suas campanhas militares.\n\nA técnica consiste em um tipo de '
            'cifra de substituição, onde cada letra do texto original é substituída por uma letra fixa à '
            'frente no alfabeto. Por exemplo, se o deslocamento (conhecido como chave) for 3, "A" se tornaria '
            '"D", "B" se tornaria "E" e assim por diante. Ao atingir o final do alfabeto, o processo volta ao começo.',
            size=(60, 10), auto_size_text=True, background_color="#000000", text_color="#ffffff", font=('Montserrat', 10)
        )
    ],
    [Text('Criptografar ou Descriptografar', background_color="#3CB955", text_color="#ffffff", font=('Montserrat', 11, 'bold'), size=(53, 1), justification='center')],
    [
        Text('Digite sua mensagem:', background_color="#000000", text_color="#ffffff", font=('Montserrat', 10, 'bold')),
        InputText(background_color='#fff', border_width=0, size=(46, 1), key='mensagem')
    ],
    [
        Text('Digite a sua chave:', background_color="#000000", text_color="#ffffff", font=('Montserrat', 10, 'bold')),
        InputText(background_color='#fff', border_width=0, size=(49, 1), key='chave')
    ],
    [
        Button('Criptografar', button_color=('#fff', '#3CB955'), font=('Montserrat', 10, 'bold')),
        Button('Descriptografar', button_color=('#fff', '#3CB955'), font=('Montserrat', 10, 'bold')),
        Button('Limpar', button_color=('#fff', '#3CB955'), font=('Montserrat', 10, 'bold')),
    ],
    [Text('Resultados', justification='center', font=('Montserrat', 12, 'bold'), size=(60, 1))],
    [Output(size=(70,4), key='Result')]
]

window = Window('Criptografia de Cesar', layout, size=(500, 450))
while True:
    event, values = window.read()

    if event == 'Criptografar':
        window['Result'].update(value='') 
        mensagem = values['mensagem']
        key = values['chave']
        texto = criptografar.criptografar(mensagem, key)
        window['Result'].update(value=f'Mensagem: {mensagem}\nCriptografado: {texto}\nChave: {key}\nDescriptografado: --')

    elif event == 'Descriptografar':
        window['Result'].update(value='') 
        mensagem = values['mensagem']
        key = values['chave']
        texto = descriptografar.descriptografar(mensagem, key)
        window['Result'].update(value=f'Mensagem: {texto}\nCriptografado: {mensagem}\nChave: {key}\nDescriptografado: {texto}')

    elif event == 'Limpar':
        window['mensagem'].update(value='')
        window['chave'].update(value='') 
        window['Result'].update(value='')    

    elif event == WINDOW_CLOSED:
        break

window.close()
