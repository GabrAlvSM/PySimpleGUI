import PySimpleGUI as sg


# All the stuff inside your window.
layout = [[sg.Text("Hello World!!")],
          [sg.Text('Type something: '), sg.InputText()],
          [sg.Button('Ok'), sg.Button('Cancel')],
          [sg.Text("You typed: ")],[sg.Text("", key='-res-')]
        #   [sg.Text(f"You typed: {x}")]
          ]
# layout = [[sg.In( disabled=True, key='-DISPLAY-')]]

# Create the Window
window = sg.Window('Janela Exemplo', layout)

# Event Loop to process "events" and get the "values" of the inputs
x = ""
while True:
    event, values = window.read()
    x = str(values[0])
    # if user closes window or clicks cancel

    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    elif event == "Ok":
        layout+="You typed: {x}"
        window['-res-'].update(x)

window.close()
