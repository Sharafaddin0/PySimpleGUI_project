import streamlit as st
import functions

list = functions.get_list()


st.title("Simple To-Do app")
st.subheader("This is my todo app")
st.write("Increase your productivity")

for todo in list:
    st.checkbox(todo)

st.text_input(label = " ", placeholder = "Add a new todo...")

