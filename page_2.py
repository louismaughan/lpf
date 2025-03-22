import streamlit as st
import pandas as pd

st.header("Apps and wins 2025")
st.sidebar.markdown("Apps and wins")
st.markdown("Who has made the most appearances this year and who has the best win percentage.")
st.markdown("Win percentage only counts players who've played more than 5 games.")

df = pd.read_csv('lpf.csv')

col1, col2 = st.columns(2)

with col1:
   st.subheader("Win percentage")
   win = df[['Player','Apps','Win %']]
   win_fil = win[win['Apps'] > 4]
   win_fil = win_fil.sort_values('Win %',ascending=False).head(10)[['Player','Win %']]
   st.write(win_fil)

with col2:   
   st.subheader("Most apps")
   app = df[['Player','Apps']]
   app = app.sort_values('Apps',ascending=False).head(10)[['Player','Apps']]
   st.write(app)

