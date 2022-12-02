import streamlit as st
import functions

list = functions.get_list()


st.title("Simple To-Do app")
st.subheader("This is my todo app")
st.write("Increase your productivity")

