# llm-PDF-Chat

This application is a conversational assistant built with Streamlit, designed to process PDF documents, extract text, and interact with users through a language model. It leverages `langchain`,  `FAISS` for vector storage, and `OpenAI's` embedding and language models to enable intelligent responses based on the content of uploaded PDFs.

## Features
* **PDF Text Extraction**: Upload one or multiple PDF documents, and the application will extract and process the text.
* **Chunked Text Processing**: Splits the extracted text into manageable chunks to optimize the performance of embeddings.
* **Embeddings and Vector Store**: Utilizes OpenAI embeddings and FAISS for efficient storage and retrieval of document information.
* **Conversational Memory**: Keeps track of previous interactions to allow for a continuous, context-aware conversation.
* **Customizable User Interface**: Implements templates for user and bot interactions using HTML and CSS styling.

## Setup and Installation
1. Clone the repository:

```bash 
git clone https://github.com/RawatRahul14/llm-PDF-Chat.git
cd llm-PDF-Chat
```

2. Create a virtual environment:

```bash
python -m venv .venv
.venv/Scripts/activate
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Set up your API Keys:
    * Obtain your OpenAI API Key and set it in `.env` file.

5. Run the Application:

```bash
streamlit run app.py
```

## Usage 

1. **Upload PDFs**: Click the upload button to add PDF files for analysis.

2. **Ask Questions**: Enter questions or commands related to the content of the uploaded PDFs.

3. **View Responses**: The assistant will respond with answers based on the document content and context.

## Project Structure

* **app.py**: Main file to run the Streamlit application.
* **htmlTemplates.py**: Contains HTML and CSS for styling the user interface.

jdfhbviufedbv