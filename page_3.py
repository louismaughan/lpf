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

with col1:
    st.subheader("Goals per game")
    gpg = df[['Player','Apps','GpG']]
    gpg_fil = gpg[gpg['Apps'] > 10]
    gpg_fil = gpg_fil.sort_values('GpG',ascending=False).head(10)[['Player','GpG']]
    st.write(gpg_fil)

with col2:
    st.subheader("Assists")
    ac = df[['Player','Assists']]
    ac = ac.sort_values('Assists', ascending=False).head(10)[['Player', 'Assists']]
    st.write(ac)

with col2:
    st.subheader("Assists per game")
    apg = df[['Player','Apps','ApG']]
    apg_fil = apg[apg['Apps'] > 10]
    apg_fil = apg_fil.sort_values('ApG',ascending=False).head(10)[['Player','ApG']]
    st.write(apg_fil)

with col3:
    st.subheader("Goal + assists")
    ga = df[['Player','G+A']]
    ga = ga.sort_values('G+A', ascending=False).head(10)[['Player', 'G+A']]
    st.write(ga)

with col3:
    st.subheader("G+A per game")
    gapg = df[['Player','Apps','GApG']]
    gapg_fil = gapg[gapg['Apps'] > 10]
    gapg_fil = gapg_fil.sort_values('GApG',ascending=False).head(10)[['Player','GApG']]
    st.write(gapg_fil)
    



