import streamlit as st
st.title("Resturant Name Generator")

picked = st.sidebar.selectbox("Pick one", ["Italian", "Chinese", "Indian", "Mexican"])
