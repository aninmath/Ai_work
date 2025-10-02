import streamlit as st
st.title("square doing app")
# st.write("### this is a test")

# col1, col2 = st.columns(2)

# x = col1.number_input("home value", min_value=0, max_value= 1000)

x = st.number_input("give your prompt")

if st.button("summarize"):
    st.write(f"the square is {x**2}")
