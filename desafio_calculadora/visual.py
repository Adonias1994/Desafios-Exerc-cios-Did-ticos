# Design do programa
from PySimpleGUI import PySimpleGUI as sg
# Layout
sg.theme('Default1')
layout = [
    [sg.Text('Valor 1: '), sg.Input(key = 'v1')],
    [sg.Text('Escolha uma operação matemática (+, -, *, /, p para potência): '), sg.Input(key = 'o')],
    [sg.Text('Valor 2: '), sg.Input(key = 'v2')],
    [sg.Button('Calcular')],
]
# Janela
janela = sg.Window('Tela', layout)
# Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Calcular':
        if valores['o'] == '+':
            print('O resultado é: ', 'v1' + 'v2', '\n')
