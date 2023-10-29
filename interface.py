from PySimpleGUI import *
from src import criptografar, descriptografar

layout = [
    [Text('Criptografia de Cesar', justification='center', font=('Montserrat', 14, 'bold'), size=(40, 1), background_color='#3CB955')],
    [Text('Sobre:', background_color="#ffffff", text_color="#000000", font=('Montserrat', 11, 'bold'))],
    [
        Text(
            'A Criptografia de César é uma das técnicas mais simples e conhecidas de criptografia. '
            'Recebe esse nome por causa de Júlio César, que supostamente a teria utilizado para '
            'comunicações secretas durante suas campanhas militares.\n\nA técnica consiste em um tipo de '
            'cifra de substituição, onde cada letra do texto original é substituída por uma letra fixa à '
            'frente no alfabeto. Por exemplo, se o deslocamento (conhecido como chave) for 3, "A" se tornaria '
            '"D", "B" se tornaria "E" e assim por diante. Ao atingir o final do alfabeto, o processo volta ao começo.',
            size=(60, 10), auto_size_text=True, background_color="#ffffff", text_color="#000000", font=('Montserrat', 10)
        )
    ],
    [Text('Criptografar ou Descriptografar', background_color="#3CB955", text_color="#000000", font=('Montserrat', 11, 'bold'), size=(53, 1), justification='center')],
    [
        Text('Digite sua mensagem:', background_color="#ffffff", text_color="#000000", font=('Montserrat', 10, 'bold')),
        InputText(background_color='#ffffff', border_width=1, size=(46, 1), key='mensagem')
    ],
    [
        Text('Digite a sua chave:', background_color="#ffffff", text_color="#000000", font=('Montserrat', 10, 'bold')),
        InputText(background_color='#fff', border_width=1, size=(49, 1), key='chave')
    ],
    [
        Button('Criptografar', button_color=('#000000', '#3CB955'), font=('Montserrat', 10, 'bold')),
        Button('Descriptografar', button_color=('#000000', '#3CB955'), font=('Montserrat', 10, 'bold')),
        Button('Limpar', button_color=('#000000', '#3CB955'), font=('Montserrat', 10, 'bold')),
    ],
    [Text('Resultados', justification='center', font=('Montserrat', 12, 'bold'), size=(60, 1), background_color='#3CB955')],
    [Multiline(size=(70,5), key='Result', disabled=True)]
]

window = Window('Criptografia de Cesar', layout, size=(500, 460), background_color='#ffffff')
while True:
    event, values = window.read()

    if event == 'Criptografar':
        if len(values['mensagem']) > 130:
            Popup('Invalido! Mensagem maior que 130 caracteres...')
            window['mensagem'].update(value='')
            window['chave'].update(value='') 
            window['Result'].update(value='')

        window['Result'].update(value='') 
        mensagem = values['mensagem']
        key = values['chave']
        texto = criptografar.criptografar(mensagem, key)
        window['Result'].update(value=f'Mensagem: {mensagem}\nCriptografado: {texto}\nChave: {key}\nDescriptografado: --')

    elif event == 'Descriptografar':
        if len(values['mensagem']) > 130:
            Popup('Invalido! Mensagem maior que 130 caracteres...')
            window['mensagem'].update(value='')
            window['chave'].update(value='') 
            window['Result'].update(value='')

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
