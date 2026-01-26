import streamlit as st
from streamlit import session_state

from functions import get_todos, write_todos

todos = get_todos()
def add_todo():
        todo= st.session_state["new_todo"] + '\n'
        todos.append(todo)
        write_todos(todos)


st.title("Web Based To-do Application")
st.subheader("To-do Application")
st.write("Use this app to record all daily task. Ensure to complete all.")

for idx, todo in enumerate(todos):
        checkbox = st.checkbox(todo, key=todo)
        if checkbox:
            todos.pop(idx)
            write_todos(todos)
            del st.session_state[todo]
            st.rerun()

st.text_input(label="", placeholder="Add to-do...", on_change=add_todo, key="new_todo")























st.text("Zion Technologies. All rights reserved 2026.")

