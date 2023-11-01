'''
Calculadora com interface grafica simples em python
Autor: João Adriano de Ornellas
Bibliotecas:
    PySimpleGUI
'''
import PySimpleGUI as sg

layout = [
    [sg.Text('Calculadora em PYTHON')],
    [sg.Text('Primeiro valor:'),sg.Input(key='val1')],
    [sg.Text('Segundo  valor:'),sg.Input(key='val2')],
    [sg.Button('SOMAR', key= 'soma'),sg.Button('SUBTRAIR', key= 'sub'),sg.Button('MULTIPLICAR', key= 'multi'),sg.Button('DIVIDIR', key= 'div')]
]

window = sg.Window('Calculadora em PYTHON', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'soma':
        resultado = float(values['val1']) + float(values['val2'])
        sg.popup(f'''
O valor da soma de {values["val1"]} + {values['val2']} é:
{resultado}''')
        
    if event == 'sub':
        resultado = float(values['val1']) - float(values['val2'])
        sg.popup(f'''
O valor da subtração de {values["val1"]} - {values['val2']} é:
{resultado}''')
        
    if event == 'multi':
        resultado = float(values['val1']) * float(values['val2'])
        sg.popup(f'''
O valor do produto de {values["val1"]} X {values['val2']} é:
{resultado}''')

    if event == 'div':
        resultado = float(values['val1']) / float(values['val2'])
        sg.popup(f'''
O valor da soma de {values["val1"]} / {values['val2']} é:
{resultado}''')
        

window.close()