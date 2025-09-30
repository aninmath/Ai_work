import streamlit as st
st.title("test app")
st.write("### this is a test")

col1, col2 = st.columns(2)

x = col1.number_input("home value", min_value=0, max_value= 1000)

if st.button("calculate"):
    st.write(f"the square is {x**2}")
