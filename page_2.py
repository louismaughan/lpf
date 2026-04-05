import streamlit as st
import pandas as pd

st.header("Apps and wins 2026")
st.sidebar.markdown("Apps and wins")
st.markdown("Who has made the most appearances this year, who has the best win percentage and who has won the most defensive player of the match awards.")
st.markdown("Win percentage only counts players who've played more than 5 games.")

df = pd.read_csv('lpf.csv')

col1, col2, col3 = st.columns(3)

with col1:
   st.subheader("Win percentage")
   win = df[['Player','Apps','Win %']]
   win_fil = win[win['Apps'] > 3]
   win_fil = win_fil.sort_values('Win %',ascending=False).head(10)[['Player','Win %']]
   st.write(win_fil)

#with col1:
   st.subheader("Ratings")
   rat = df[['Player','Apps','Rating']]
   rat_fil = rat[rat['Apps'] > 10]
   rat_fil = rat_fil.sort_values('Rating',ascending=False).head(10)[['Player','Rating']]
   st.write(rat_fil)   


with col2:   
   st.subheader("Most apps")
   app = df[['Player','Apps']]
   app = app.sort_values('Apps',ascending=False).head(10)[['Player','Apps']]
   st.write(app)

with col3:   
   st.subheader("DPOTM")
   dpotm = df[['Player','Votes']]
   dpotm = dpotm.sort_values('Votes',ascending=False).head(10)[['Player','DPOTM']]
   st.write(dpotm)
   







