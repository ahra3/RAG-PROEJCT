🧬 Onboarding Assistant — RAG System for Umbrella Corporation

A Retrieval-Augmented Generation (RAG) onboarding chatbot built with LangChain, ChromaDB, and Streamlit

<img src="https://upload.wikimedia.org/wikipedia/commons/0/0e/Umbrella_Corporation_logo.svg" alt="Umbrella Corporation Logo" width="110"/>
📘 Overview

This project implements a Retrieval-Augmented Generation (RAG) onboarding assistant for the fictional Umbrella Corporation from the Resident Evil universe. The goal is to simulate a modern AI-powered internal onboarding tool that helps new employees navigate corporate policies, internal procedures, and company regulations.

The system combines:

Generative AI for natural, context-aware responses

Vector-based retrieval to ground answers on real internal documents

Synthetic employee profiles to personalize the onboarding experience

A user-friendly UI built with Streamlit

The result is a realistic AI assistant capable of answering questions about policies, work guidelines, safety protocols, and employee benefits using both document-augmented knowledge and user-specific attributes.

🧠 Project Architecture & Technical Stack

The assistant is designed using modern modular AI architecture, centered around the RAG pipeline:

🔗 1. LangChain

LangChain orchestrates the entire workflow:

Manages the LLM interaction

Handles prompt templates for personalization

Connects the LLM with the vector store retriever

Provides tools for document loading, splitting, and retrieval chains

Using LangChain ensures the application is scalable, maintainable, and easily extendable for real-world use.

🗃️ 2. Chroma Vector Database

Company policies (PDF) are embedded and stored in a Chroma vector database:

Text is chunked and embedded (using an embedding model)

Chroma stores and indexes the documents

Queries retrieve the most relevant context passages

This enables the assistant to provide fact-grounded answers with high relevance and low hallucination.

🤖 3. Large Language Model (LLM)

The LLM (e.g., OpenAI, HuggingFace, or any configured provider) is responsible for:

Understanding user queries

Integrating retrieved corporate policy context

Personalizing responses using employee metadata

👤 4. Synthetic Employee Database

A synthetic employee generator provides realistic employee profiles containing:

Employment status

Department

Clearance level

Role-specific responsibilities

Training progress

This allows the assistant to produce dynamic and personalized answers tailored to each employee.

🖥️ 5. Streamlit Interface

A clean and interactive UI built with Streamlit:

Lets employees chat with the onboarding assistant

Displays retrieved context when needed

Provides a smooth user experience in web application form

🏢 Business Context

The Umbrella Corporation is a vast, multinational biotech and pharmaceutical conglomerate known for its advanced research and strict internal governance. New employees must quickly understand:

Safety protocols

Corporate compliance

Research facility guidelines

Biohazard procedures

Human resources policies

This onboarding assistant helps new hires navigate these regulations efficiently, providing:

Instant answers to onboarding questions

Guidance based on their employee profile

Summaries of complex internal policies

A faster, more engaging onboarding experience

Although fictional, the system design reflects real enterprise AI onboarding tools.

🚀 Features

RAG-Enhanced Querying
Answers are grounded in the Umbrella regulations PDF.

Fully Personalized Responses
Using employee-specific data for contextualized answers.

Interactive Chat Interface
Built with Streamlit for seamless communication.

Searchable Regulatory Database
Powered by Chroma and integrated through LangChain.

Modular Design
Easy to extend with more documents, new models, or other data sources.
