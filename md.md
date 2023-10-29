import PySimpleGUI as sg
from PySimpleGUI import VSeparator, Column

# Elementos da primeira coluna
layout_esquerda = [
    [sg.Text('Criptografia de César', background_color="#000000", text_color="#ffffff", font=('Montserrat', 14, 'bold'), size=(1, 1), justification='center')],
    [sg.Text('Sobre:', background_color="#000000", text_color="#ffffff", font=('Montserrat', 11, 'bold'))],
    [sg.Text(
        'A Criptografia de César é uma das técnicas mais simples e conhecidas de criptografia. '
        'Recebe esse nome por causa de Júlio César, que supostamente a teria utilizado para '
        'comunicações secretas durante suas campanhas militares.\n\nA técnica consiste em um tipo de '
        'cifra de substituição, onde cada letra do texto original é substituída por uma letra fixa à '
        'frente no alfabeto. Por exemplo, se o deslocamento (conhecido como chave) for 3, "A" se tornaria '
        '"D", "B" se tornaria "E" e assim por diante. Ao atingir o final do alfabeto, o processo volta ao começo.',
        size=(50, 10), auto_size_text=True, background_color="#000000", text_color="#ffffff", font=('Montserrat', 10))
    ],
    [sg.Text('Criptografar ou Descriptografar', background_color="#3CB955", text_color="#ffffff", font=('Montserrat', 11, 'bold'), size=(45, 1), justification='center')],
    [sg.Text('Digite sua mensagem:', background_color="#000000", text_color="#ffffff", font=('Montserrat', 10, 'bold')), sg.InputText(background_color='#fff', border_width=0, size=(10, 1))],
    [sg.Text('Digite a sua chave:', background_color="#000000", text_color="#ffffff", font=('Montserrat', 10, 'bold')), sg.InputText(background_color='#fff', border_width=0, size=(10, 1))],
    [sg.Button('Criptografar', button_color=('#fff', '#3CB955'), font=('Montserrat', 10, 'bold')),
     sg.Button('Descriptografar', button_color=('#fff', '#3CB955'), font=('Montserrat', 10, 'bold')),
     sg.Button('Histórico', button_color=('#fff', '#3CB955'), font=('Montserrat', 10, 'bold')),
     sg.Button('Limpar', button_color=('#fff', '#3CB955'), font=('Montserrat', 10, 'bold')),
     sg.Text('', size=(50, 10), auto_size_text=True, background_color='#fff', font=('Montserrat', 10, 'bold'), justification='center')
    ]
]

layout_direita = [
    [sg.Text('Olá')]
]

layout = [
    [
        sg.Column(layout_esquerda, element_justification='r', size=(495, 500)),
        sg.VSeparator(),
        sg.Column(layout_direita, element_justification='l', background_color='#e12', size=(495, 500))
    ]
]

window = sg.Window('Criptografia de César', layout, background_color="#000000", size=(1000, 500))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()
