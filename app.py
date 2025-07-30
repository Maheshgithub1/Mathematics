import streamlit as st
from math_agent import ask_math_agent

st.set_page_config(page_title="AI Math Tutor", page_icon="➗")
st.title("🧠 AI Math Tutor")

user_input = st.text_input("Enter your math question (e.g., Solve 3x + 2 = 11):", key="math_query")

if user_input:
    with st.spinner("Crunching numbers..."):
        response = ask_math_agent(user_input)
        st.success("Here's the solution:")
        st.markdown(response)
