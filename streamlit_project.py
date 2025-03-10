import streamlit as st
import pandas as pd


st.image('Bears3.png')
st.title("Wood Street Bears FC")
st.header("Current tournament champions")
st.markdown("Dav's yellow peril (Feb 2025): Dav, Steve, Felipe, Liam, Alwyn, Joe, Leo, Aiden")
st.markdown("Player of the tournament - Steve")


df = pd.read_csv('lpf.csv')
print(df.head())

st.header("Sunday football stats 2025")
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Top scorers")
    gc = df[['Player','Goals']]
    gc = gc.sort_values('Goals', ascending=False).head(5)[['Player', 'Goals']]
    st.write(gc)


with col2:
    st.subheader("Most assists")
    ac = df[['Player','Assists']]
    ac = ac.sort_values('Assists', ascending=False).head(5)[['Player', 'Assists']]
    st.write(ac)

with col3:
    st.subheader("Goal and assists")
    ga = df[['Player','G+A']]
    ga = ga.sort_values('G+A', ascending=False).head(5)[['Player', 'G+A']]
    st.write(ga)


col1, col2 = st.columns(2)

with col1:
   st.subheader("Win percentage")
   win = df[['Player','Apps','Win %']]
   win_fil = win[win['Apps'] > 4]
   win_fil = win_fil.sort_values('Win %',ascending=False).head(5)[['Player','Win %']]
   st.write(win_fil)

with col2:   
   st.subheader("Most apps")
   app = df[['Player','Apps']]
   app = app.sort_values('Apps',ascending=False).head(5)[['Player','Apps']]
   st.write(app)



st.header("Fixtures")
st.markdown("Sat 26 April 2025 - tournament or 11-aside")


























