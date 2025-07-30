import openai
import os

try:
    import streamlit as st
    api_key = st.secrets["OPENAI_API_KEY"]
except Exception:
    api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OpenAI API key not found. Please set it via Streamlit secrets or environment variables.")

openai.api_key = api_key

def ask_math_agent(question):
    prompt = (
        "You are a helpful AI math tutor. Solve math problems step-by-step and explain clearly.\n"
        f"Question: {question}\nAnswer:"
    )
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a friendly math tutor."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            max_tokens=500
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"⚠️ Error: {str(e)}"
