import streamlit as st
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
import os

# Configuração da página
st.set_page_config(page_title="Chatbot RAG - Verônica", page_icon="🤖")

st.title("🤖 Meu Assistente Pessoal de Projetos")
st.write("**Desenvolvido por Verônica Bergelino**")

st.info("""
Este é um chatbot inteligente que usa RAG (Retrieval-Augmented Generation) 
para responder perguntas sobre meus projetos e experiência profissional.
""")

# Simulação para demonstração (sem API key necessária)
st.write("---")
st.subheader("🚀 Projetos em Destaque:")
st.write("- **Chatbot RAG com IA**: Sistema de perguntas e respostas inteligente")
st.write("- **Sistema de Recomendação**: ML para recomendar projetos baseado em skills")
st.write("- **Dashboard Analytics**: Visualização de dados empresariais")

st.write("---")
st.write("📧 **Contato**: veronica.bergelino@hotmail.com")
st.write("💼 **LinkedIn**: linkedin.com/in/veronica-bergelino")
