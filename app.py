import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
# for creating chunks
from langchain.text_splitter import CharacterTextSplitter
# for embeddings
from langchain.embeddings import OpenAIEmbeddings
# for vectorstore
from langchain.vectorstores import FAISS
# llm
from langchain.chat_models import ChatOpenAI
# for continuity of conversations
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
# for designing
from htmlTemplates import css, user_template, bot_template


# To get the text from the pdf file
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# To create the chunks from the text
def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator = "\n",
        chunk_size = 1000,
        chunk_overlap = 200
    )
    chunks = text_splitter.split_text(text)
    return chunks

# To initialize the vectorstore
def get_vectorestore(text_chunks):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(
        texts = text_chunks, 
        embedding = embeddings
    )
    return vectorstore

# Initialising the ConversationalChain
def get_conversation_chain(vectorstore):
    llm = ChatOpenAI()

    memory = ConversationBufferMemory(
        memory_key = "chat_history",
        return_messages = True
    )
    chain = ConversationalRetrievalChain.from_llm(
        llm = llm,
        retriever = vectorstore.as_retriever(),
        memory = memory
    )
    return chain

# Handling the user Input
def handle_user_input(user_question):
    response = st.session_state.conversation(
        {"question": user_question}
    )
    st.session_state.chat_history = response["chat_history"]

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html = True)
        else:
            st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html = True)

def main():
    load_dotenv()
    st.set_page_config(
        page_title = "Multiple PDF ChatBot",
        page_icon = ":books:"
    )
    st.write(css, unsafe_allow_html = True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("Multiple PDF ChatBot :books:")
    user_question = st.text_input("Ask a question about the documents: ")

    if user_question:
        handle_user_input(user_question)

    with st.sidebar:
        st.subheader("Your Documents")
        pdf_docs = st.file_uploader(
            "Upload your pdf's and click on the process button",
            accept_multiple_files = True
        )
        if st.button("Process"):
            with st.spinner("Processing..."):
                # get the pdf text
                raw_text = get_pdf_text(pdf_docs)

                # get the chunks from the text
                text_chunks = get_text_chunks(raw_text)

                # initialize the vectorstore
                vectorstore = get_vectorestore(text_chunks)

                # initialize the conversation chain
                st.session_state.conversation = get_conversation_chain(vectorstore)

if __name__ == "__main__":
    main()