import vertexai
import streamlit as st
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel, Part, Content, ChatSession

# Initialize Vertex AI with your project
project_id  = "euphoric-axiom-423422-g3"
vertexai.init(project=project_id)

# Configure the generation settings
config = generative_models.GenerationConfig(temperature=0.4)

# Initialize the generative model
model = GenerativeModel("gemini-pro", generation_config=config)
chat = model.start_chat()

# Helper function to send and display messages
def llm_function(chat: ChatSession, query):
    try:
        response = chat.send_message(query)
        output = response.candidates[0].content.parts[0].text
        
        with st.chat_message("model"):
            st.markdown(output)
        
        st.session_state.messages.append({"role": "user", "content": query})
        st.session_state.messages.append({"role": "model", "content": output})
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Title of the Streamlit app
st.title("Gemini Explorer")

# Initialize session state if not already done
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display and load chat history
for index, message in enumerate(st.session_state.messages):
    content = Content(role=message["role"], parts=[Part.from_text(message["content"])])
    if index != 0:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    chat.history.append(content)

if len(st.session_state.messages) == 0:
    initial_prompt = "Introduce yourself as ReX, an assistant powered by Google Gemini. You use emojis to be interactive"
    llm_function(chat, initial_prompt)

# Capture user input
query = st.chat_input("Ask something ...")

if query:
    with st.chat_message("user"):
        st.markdown(query)
    llm_function(chat, query)


