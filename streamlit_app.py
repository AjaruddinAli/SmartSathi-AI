import os
import streamlit as st
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-15-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")

st.set_page_config(
    page_title="SmartSathi AI",
    page_icon="🤖"
)

st.title("🤖 SmartSathi AI")

with st.sidebar:
    st.markdown("## 👨‍💻 About Developer")
    st.markdown("**Sk Ajaruddin Ali**")
    st.markdown("📧 skajaruddin.ali@gmail.com")
    st.markdown("📱 +91-7386386436")
    st.markdown("---")
    st.markdown("🌍 *Let's change the world by helping each other*")
st.caption("Your AI-powered daily assistant for smarter living")
# Initialize session state for memory
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

# Display chat history
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    # Show user message
    with st.chat_message("user"):
        st.write(user_input)

    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get response
    response = client.chat.completions.create(
        model=deployment,
        messages=st.session_state.messages
    )

    answer = response.choices[0].message.content

    # Show bot message
    with st.chat_message("assistant"):
        st.write(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})

    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; font-size: 14px;'>
        👨‍💻 Built by <b>Sk Ajaruddin Ali</b> | 
        📧 skajaruddin.ali@gmail.com | 
        📱 +91-7386386436 <br>
        🌍 <i>Let's change the world by helping each other</i>
        </div>
        """,
        unsafe_allow_html=True
)
