import streamlit as st
import pandas as pd

st.header("Attack and defensive performance 2026")
st.sidebar.markdown("Defence and attack")

df = pd.read_csv('lpf.csv')

col1, col2, col3 = st.columns(3)

with col1:   
   st.subheader("Goals for per game")
   gf = df[['Player','Apps','GF/g']]
   gf90 = gf[gf['Apps'] > 4]
   gf90 = gf90.sort_values('GF/g',ascending=False).head(10)[['Player','GF/g']]
   st.write(gf90)

with col2:   
   st.subheader("Goals against per game")
   ga = df[['Player','Apps','GA/g']]
   ga90 = ga[ga['Apps'] > 4]
   ga90 = ga90.sort_values('GA/g',ascending=False).head(10)[['Player','GA/g']]
   st.write(ga90)

with col3:   
   st.subheader("GD per game")
   gd = df[['Player','Apps','GD']]
   gd90 = gd[gd['Apps'] > 4]
   gd90 = gd90.sort_values('GD',ascending=False).head(10)[['Player','GD']]
   st.write(gd90)