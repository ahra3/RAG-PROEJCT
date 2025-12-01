# 🧬 **Onboarding Assistant — RAG System for Umbrella Corporation**

*A Retrieval-Augmented Generation (RAG) onboarding chatbot built with LangChain, ChromaDB, and Streamlit*

<img src="https://upload.wikimedia.org/wikipedia/commons/0/0e/Umbrella_Corporation_logo.svg" alt="Umbrella Corporation Logo" width="110"/>

---

## 📘 **Overview**

This project implements a **Retrieval-Augmented Generation (RAG)** onboarding assistant for the fictional **Umbrella Corporation** from the *Resident Evil* universe. The goal is to simulate a modern AI-powered internal onboarding tool that helps new employees navigate corporate policies, internal procedures, and company regulations.

The system combines:

- **Generative AI** for natural, context-aware responses  
- **Vector-based retrieval** to ground answers in real internal documents  
- **Synthetic employee profiles** to personalize the onboarding experience  
- **A user-friendly UI** built with Streamlit  

The result is a realistic AI assistant capable of answering questions about policies, work guidelines, safety protocols, and employee benefits using both **document-augmented knowledge** and **user-specific attributes**.

---

## 🧠 **Project Architecture & Technical Stack**

The assistant is designed using a modern modular AI architecture centered around the **RAG pipeline**, consisting of the following components:

### 🔗 **1. LangChain**

LangChain orchestrates the entire workflow by:

- Managing the LLM interaction  
- Handling prompt templates for personalization  
- Linking the LLM with the vector store retriever  
- Providing tools for document loading, splitting, and retrieval chains  

This ensures the application is **scalable, maintainable, and extendable** for real-world use cases.

### 🗃️ **2. Chroma Vector Database**

Company policies extracted from a PDF are embedded and stored in a **Chroma vector database**:

- Text is chunked and embedded using an embedding model  
- Chroma stores and indexes these embeddings  
- Queries retrieve the most relevant context chunks  

This allows the assistant to provide **fact-grounded answers** with high relevance and minimal hallucination.

### 🤖 **3. Large Language Model (LLM)**

The selected LLM (OpenAI, HuggingFace, or other configured providers) is responsible for:

- Understanding user queries  
- Integrating retrieved corporate policy context  
- Personalizing responses using employee data  

### 👤 **4. Synthetic Employee Database**

A synthetic employee generator provides realistic profiles including:

- Employment status  
- Department  
- Clearance level  
- Role-specific responsibilities  
- Training progress  

This ensures responses are **dynamic and tailored** to each employee.

### 🖥️ **5. Streamlit Interface**

A clean and interactive web interface built with **Streamlit**:

- Allows employees to chat with the onboarding assistant  
- Displays retrieved context when necessary  
- Provides a smooth and intuitive user experience  

---

## 🏢 **Business Context**

The **Umbrella Corporation** is a large multinational biotech and pharmaceutical conglomerate known for its advanced research and strict internal governance. New employees must quickly understand:

- Safety protocols  
- Corporate compliance  
- Research facility guidelines  
- Biohazard procedures  
- Human resources policies  

This onboarding assistant helps new hires navigate these regulations efficiently, providing:

- Instant answers to onboarding questions  
- Guidance tailored to their employee profile  
- Summaries of complex internal policies  
- A faster and more engaging onboarding experience  

Although fictional, the system design reflects **real enterprise AI onboarding tools**.

---

## 🚀 **Features**

### **RAG-Enhanced Querying**
Answers are grounded in the Umbrella regulations PDF using Chroma vector search.

### **Fully Personalized Responses**
Employee-specific metadata is used to provide highly contextualized answers.

### **Interactive Chat Interface**
Built with Streamlit for smooth two-way conversation.

### **Searchable Regulatory Database**
All policy documents are indexed and retrievable through LangChain + Chroma.

### **Modular & Extensible Design**
Easily add more documents, new models, or data sources.

---

