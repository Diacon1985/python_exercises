import PySimpleGUI as sg
import os.path

file_list_column = [
    [
        sg.Text("Image Folder"),
        sg.In(size=(25,1),enable_events = True,key = "-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values = [],
            enable_events = True,
            size = (40,20),
            key = "-FILE LIST-"
        )
    ],
]
image_viewer_column = [
    [sg.Text("Choose an image from list on the left")],
    [sg.Text(size=(40,1),key="-TOUT-")],
    [sg.Image(key="-IMAGE-")],
]

layout = [
    [
        sg.Column(file_list_column),
        sg.VSeparator(),
        sg.Column(image_viewer_column),
    ]
]

window = sg.Window("image viewer",layout)

while True:
    event,values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break