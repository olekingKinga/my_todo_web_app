import pandas as pd
import streamlit as st
from streamlit import session_state
from functions import get_todos, write_todos

todos = get_todos()
st.set_page_config(layout="wide")

def add_todo():
        todo= st.session_state["new_todo"] + '\n'
        todos.append(todo)
        write_todos(todos)

st.title(":rainbow[Web Based To-do Application.] 🎈")
st.subheader("Record your daily activities here.")
# Test Samples
df = pd.DataFrame({"num": [112, 112, 2, 3], "str": ["be", "a", "be", "c"]})
df = df['num'].unique()
st.table(df)
st.button("Re-run")

st.markdown("""
    First simple Streamlit Application.\n
    ***There's :rainbow[so much we can build].***\n
    Experimental App for all the widgets available.\n
    Cool playground for displaying data analytics output.
    """)
st.write("Use this app to record all daily task. <b>It Increases Productivity.</b> "
         "Ensure to complete all.", unsafe_allow_html=True)

for idx, todo in enumerate(todos):
        checkbox = st.checkbox(todo, key=todo)
        if checkbox:
            todos.pop(idx)
            write_todos(todos)
            del st.session_state[todo]
            st.rerun()

st.text_input(label="", placeholder="Add to-do...", on_change=add_todo, key="new_todo")

if st.button("Abby | Tirzah Ballons!"):
    st.balloons()

# Displaying an image: Create static dir and place the images there.
# Adding a url link on the image
st.markdown("[![Click Me](./my_todo_web_app/static/st.png)](https://www.royalpawsafaris.com/)")

























st.text("Zion Technologies. All rights reserved 2026.")

