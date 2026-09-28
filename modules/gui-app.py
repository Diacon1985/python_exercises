import PySimpleGUI as sg
import os.path


close_button = sg.Button("Close")
layout = [[sg.Text("Hello from Pythoon module")],[sg.Button("OK")],[close_button]]

window = sg.Window("Demo", layout)

while True:
    event,values = window.read()
    if event == "OK" or event == "Close" or event == sg.WIN_CLOSED:
        break

window.close()