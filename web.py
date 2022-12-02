import streamlit as st
import functions

list = functions.get_list()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    list.append(todo)
    functions.write_list(list)

st.title("Simple To-Do app")
st.subheader("This is my todo app")
st.write("Increase your productivity")

for index, todo in enumerate(list):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        print(checkbox)
        list.pop(index)
        functions.write_list(list)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label = "", placeholder = "Add a new todo...",
              on_change=add_todo, key = 'new_todo')

