import streamlit as st
import pandas as pd

# Define the pages
main_page = st.Page("main_page.py", title="Home")
page_2 = st.Page("page_2.py", title="Apps and wins")
page_3 = st.Page("page_3.py", title="Goals and assists")
page_4 = st.Page("page_4.py", title="Attack and defence")

# Set up navigation
pg = st.navigation([main_page, page_2, page_3])

# Run the selected page
pg.run()



























