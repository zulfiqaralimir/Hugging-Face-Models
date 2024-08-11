import streamlit as st
import requests

# API_URL = "https://api-inference.huggingface.co/models/openai-community/gpt2"
API_URL = "https://api-inference.huggingface.co/models/openai-community/gpt2"
# API_TOKEN = "your_hugging_face_api_token"
API_TOKEN = "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"

headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

data = {"inputs": "Once upon a time,"}
output = query(data)

# Print the output to see what is being returned
st.write(output)

# Safely attempt to access the generated text
if isinstance(output, list) and len(output) > 0 and "generated_text" in output[0]:
    st.write(output[0]["generated_text"])
else:
    st.write("No generated text found in the response.")



st.title("Hugging Face LLM Endpoint with Streamlit")

user_input = st.text_input("Enter a prompt:")

if user_input:
    # Query the model via the API
    output = query({"inputs": user_input})

    # Display the generated text
    st.write("Generated text:")
    st.write(output[0]["generated_text"])