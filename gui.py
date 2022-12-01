import PySimpleGUI as sg
import functions
import time
import os

if not os.path.exists("operation.txt"):
    with open("operation.txt", "w") as file:
        pass

sg.theme("DarkAmber")

clock = sg.Text('',key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_list(), key='list',
                      enable_events=True, size =[60, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

layout = [[clock], [label], [input_box, add_button], [list_box, edit_button, complete_button], [exit_button]]

window = sg.Window('My To-Do App',
                   layout=layout,
                   font=('Helvetica', 10))


while True:
    event, values = window.read(timeout = 200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(2, values)
    print(3, values['list'])
    match event:
        case "Add":
            list = functions.get_list()
            new_list = values['todo'] + '\n'
            list.append(new_list)
            functions.write_list(list)

        case "Edit":
            try:
                todo = values['list'][0]
                new_todo = values['todo']

                list = functions.get_list()
                index = list.index(todo)
                list[index] = new_todo
                functions.write_list(list)
                window['list'].update(values=list)
            except IndexError:
                sg.popup("Please choose an item first", font=('Helvetica', 20))

        case "Complete":
            try:
                todo_to_complete = values['list'][0]
                list = functions.get_list()
                list.remove(todo_to_complete)
                functions.write_list(list)
                window['list'].update(values=list)
                window['todo'].update(values='')
            except IndexError:
                sg.popup("Please choose an item first", font = ('Helvetica', 20))

        case "Exit":
            break

        case 'list':
            window['todo'].update(value = values['list'][0])

        case sg.WIN_CLOSED:
            break

window.close()