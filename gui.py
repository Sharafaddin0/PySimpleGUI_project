import PySimpleGUI as sg
import functions
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button("Add")


window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button]],
                   font = ('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            list = functions.get_list()
            new_list = values['todo'] + '\n'
            list.append(new_list)
            functions.write_list(list)
        case sg.WIN_CLOSED():
            break

window.close()