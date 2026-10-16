import streamlit as st
import pandas as pd

st.header("Attack and defensive performance 2026")
st.sidebar.markdown("Defence and attack")

df = pd.read_csv('lpf.csv')

col1, col2, col3 = st.columns(3)

with col1:   
   st.subheader("Goals for/90 ")
   gf = df[['Player','Apps','GF90']]
   gf90 = gf[gf['Apps'] > 6]
   gf90 = gf90.sort_values('GF90',ascending=False).head(10)[['Player','GF90']]
   st.write(gf90)

with col2:   
   st.subheader("Goals against/90")
   ga = df[['Player','Apps','GA90']]
   ga90 = ga[ga['Apps'] > 6]
   ga90 = ga90.sort_values('GA90',ascending=True).head(10)[['Player','GA90']]
   st.write(ga90)

with col3:   
   st.subheader("Goal difference/90")
   gd = df[['Player','Apps','GD']]
   gd90 = gd[gd['Apps'] > 6]
   gd90 = gd90.sort_values('GD',ascending=False).head(10)[['Player','GD']]
   st.write(gd90)