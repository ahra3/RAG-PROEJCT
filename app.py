from data.employees import generate_employee_data
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# ONLY LOCAL EMBEDDINGS (NO OPENAI)
from langchain_community.embeddings import SentenceTransformerEmbeddings
LOCAL_EMBEDDING_MODEL = "all-MiniLM-L6-v2"

from langchain_community.vectorstores import Chroma

from gui import AssistantGUI
from prompts import SYSTEM_PROMPT, WELCOME_MESSAGE
from langchain_groq import ChatGroq
from assistant import Assistant

import streamlit as st
import logging
import os


# Disable LangSmith + Chroma telemetry
os.environ["LANGCHAIN_TRACING_V2"] = "false"
os.environ["LANGCHAIN_ENDPOINT"] = ""
os.environ["LANGCHAIN_API_KEY"] = ""
os.environ["ANONYMIZED_TELEMETRY"] = "false"
os.environ["CHROMA_TELEMETRY_ENABLED"] = "false"


if __name__ == "__main__":

    load_dotenv()
    logging.basicConfig(level=logging.INFO)
    st.set_page_config(
        page_title="Umbrella Onboarding",
        page_icon=":guardsman:",
        layout="wide"
    )

    @st.cache_data(ttl=3600, show_spinner="Loading user data...")
    def get_user_data():
        return generate_employee_data(1)[0]

    @st.cache_resource(ttl=3600, show_spinner="Initializing vector store...")
    def init_vector_store(pdf_path):

        try:
            loader = PyPDFLoader(pdf_path)
            docs = loader.load()

            splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000, chunk_overlap=200
            )
            chunks = splitter.split_documents(docs)

            embedding_function = SentenceTransformerEmbeddings(
                model_name=LOCAL_EMBEDDING_MODEL
            )
            logging.info("Using LOCAL embeddings (MiniLM). No OpenAI required.")

            vector_store = Chroma.from_documents(
                documents=chunks,
                embedding=embedding_function,
                persist_directory="./data/vector_store"
            )
            return vector_store

        except Exception as e:
            st.error(f"Vector store could not be initialized: {e}")
            logging.error(e)
            return None

    user_data = get_user_data()
    vector_store = init_vector_store("./data/umbrella_corp_policies.pdf")

    if vector_store is None:
        st.error("❌ Vector store unavailable → running WITHOUT RAG.")
    else:
        st.success("✅ Vector store loaded successfully!")

    if "customer" not in st.session_state:
        st.session_state.customer = user_data

    if "message_history" not in st.session_state:
        st.session_state.message_history = [
            {"role": "assistant", "content": WELCOME_MESSAGE}
        ]

    # FIX → must specify model for Groq
    assistant = Assistant(
        system_prompt=SYSTEM_PROMPT,
        llm = ChatGroq(model="llama-3.1-8b-instant"),
        message_history=st.session_state.message_history,
        vector_store=vector_store,
        employee_data=st.session_state.customer
    )

    gui = AssistantGUI(assistant)
    gui.render()
