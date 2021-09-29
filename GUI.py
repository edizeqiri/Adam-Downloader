from os import write
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import InputText
import codecs
import sys
import os
import webbrowser

def logIn(__location__,pathD):

    sg.theme('DarkAmber')   # Add a touch of color

    menu_def = [['Help', 'About...']]

    # All the stuff inside your window.
    layout = [  [sg.Text('Geben Sie hier ihre Daten an. Sie können nur Ok drücken wenn alles ausgefüllt ist.')],
                [sg.Text('Email:      '), sg.InputText(key='-EMAIL-')],
                [sg.Text('Password:'), sg.InputText(key='-PASSWORD-')],
                [sg.Text('Anzahl Vorlesungen:'), sg.InputText(key='-VOR-')],
                [sg.Ok(), sg.Cancel()],
                [sg.Menu(menu_def)] ]

    # Create the Window
    window = sg.Window('Adam Download', layout)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            sys.exit(0)
            break
        if event == "About...":
            webbrowser.open('https://github.com/edizeqiri/Adam-Downloader')

        # saves email, pass and lectures
        if event == 'Ok' and values['-EMAIL-'] != '' and values['-PASSWORD-'] != '' and values['-VOR-'] != '':
            print('You entered ', values['-EMAIL-'] , values['-PASSWORD-'], values['-VOR-']) #TODO: if VOR isnt a number
            file = codecs.open(os.path.join(__location__, 'Data.txt'),'a','utf-8')
            file.write(values['-EMAIL-'] + '\n' + values['-PASSWORD-'] + '\n' + 'https://adam.unibas.ch/login.php?target=&client_id=adam&cmd=force_login&lang=de'+ '\n' + pathD)
            file.close()
            window.close()
            VorlesungenList(values['-VOR-'],__location__)
            break

    window.close()
    
def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text + '\n'
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

def VorlesungenList(anzahl,__location__):
    sg.theme('DarkAmber')   # Add a touch of color

    menu_def = [['Help', 'About...']]

    layout = [[sg.Text('Geben Sie hier ihre Vorlesungen nur in diesem Foramt an!')],
              [sg.Text('Bsp: 10915-01 – Software Engineering')],
              [sg.Menu(menu_def)]]
    if anzahl == 1:
        layout = [
                [sg.Text('1. '), sg.In(key=1)],
                [sg.Button('Save'), sg.Button('Exit')]
            ]
    else:
        for i in range(1,int(anzahl)+1):
            
            layout.append([sg.Text(str(i) +'. '), sg.In(key=i)])
        layout.append([sg.Button('Save'), sg.Button('Exit')])    

    window = sg.Window('To Do List Example', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            sys.exit(0)
            break
        if event == "About...":
            webbrowser.open('https://github.com/edizeqiri/Adam-Downloader')
        if event == 'Save':
            print('You entered ', values)
            file = codecs.open(os.path.join(__location__, 'Data.txt'),'a','utf-8')
            for i in range (1,int(anzahl)+1):
                file.write('\n' + values[i])
            file.close()
            break    
    window.close()
        
def Progressloader():
    for i in range(1,10000):
        sg.one_line_progress_meter('My Meter', i+1, 10000, 'key','Optional message')
        #TODO Progressbar

