import streamlit as st
import pandas as pd

st.header("Goals and assists 2025")
st.sidebar.markdown("Goals and assists")
st.markdown("The top scorers and assisters this year so far")

df = pd.read_csv('lpf.csv')

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Goals")
    gc = df[['Player','Goals']]
    gc = gc.sort_values('Goals', ascending=False).head(10)[['Player', 'Goals']]
    st.write(gc)


with col2:
    st.subheader("Assists")
    ac = df[['Player','Assists']]
    ac = ac.sort_values('Assists', ascending=False).head(10)[['Player', 'Assists']]
    st.write(ac)

with col3:
    st.subheader("Goal + assists")
    ga = df[['Player','G+A']]
    ga = ga.sort_values('G+A', ascending=False).head(10)[['Player', 'G+A']]
    st.write(ga)

