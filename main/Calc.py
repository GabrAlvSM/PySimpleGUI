import PySimpleGUI as sg

DISPLAY_FONT = 'Arial 25'
BUTTON_FONT = 'Arial 12'
SMALL_BUTTON_COLOR = ('black', 'Gray92')
BIG_BUTTON_COLOR = ('black', 'LightGrey')
BUTTONS = ((('7','8', '9', '÷', 'CE', '←'), ('sin',)),
            (('4','5','6','×','(',')'), ('tan',)),
            (('1','2','3','-','√','^'), ('cos',)),
            (('0','.','%','+'), ('=',)),)

def cbut(text, color=SMALL_BUTTON_COLOR, size=(6,3)):
    return sg.Button(text, size=size, font=BUTTON_FONT, button_color=color, border_width=2)

layout = [[sg.In(font = DISPLAY_FONT, size=(21,1), disabled=True, key='-DISPLAY-')]]
for row in BUTTONS:
    layout += [[cbut(text) for text in row[0]] + [cbut(text, size=(13,3), color=BIG_BUTTON_COLOR) for text in row[1]]]

window = sg.Window('GUI Calculator', layout, element_padding=(0,0), return_keyboard_events=True, margins=(0,0))

display = ''
while True:             # Event Loop
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    if event in '01234567890':
        display += event
    elif event == 'CE':
        display = ''
    window['-DISPLAY-'].update(display)
window.close()
