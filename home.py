import streamlit as st
# Pages Navigation
main_page = st.Page("todo_web_app.py", title="Todo App", icon=":material/home:")
create_page = st.Page("create.py", title="Create Entry", icon=":material/add_circle:")
delete_page = st.Page("delete.py", title="Delete Entry", icon=":material/delete:")
gray_img = st.Page("grey_image.py", title="Gray Image", icon=":material/browse_gallery:")
test_page = st.Page("reserved_pages/pages/tests.py", title="Test Page", icon=":material/analytics:")

pg = st.navigation([main_page, create_page, delete_page, gray_img, test_page])
st.set_page_config(page_title="Todo Application", page_icon=":material/edit:")
pg.run()