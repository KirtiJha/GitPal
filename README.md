## Chat with Github Repository using IBM WatsonX, Langchain, FAISS and Streamlit (RAG)

Chat with any public github repository using IBM WatsonX, Langchain, FAISS vector database and Streamlit for user friendly chat interface. This is an RAG (Retrieval Augmentented Generation) application.

### Features

Users have to enter their IBM WatsonX API Key and GitHub Repository link. The repository is then cloned in your local and chunked. Then it is converted to embeddings using Langchain and stored in FAISS vector database. Langchain is then used to build a QA retriever so that users can chat with their code.

To use this chatbot, follow these steps:

1. Clone the repository:

`git clone https://github.com/KirtiJha/chat-with-github-repo.git`

2. Install the required dependencies:

`pip install -r requirements.txt`

3. Set your environment variables in the `.env` file

- Get your IBM WatsonX API Key and add it here

3. Run the Streamlit app:

`streamlit run chatbot.py`

Access the chat interface by opening your web browser and navigating to http://localhost:8501.

Enter your IBM WatsonX API key and the name of your GitHub repository in the provided input fields.

Ask questions or provide instructions using natural language, and the chatbot will respond accordingly.

### Limitations

- The codebase chatbot relies on the Language Model and its capabilities.
- Large codebases or repositories with complex structures may take longer to chunk and embed.
- The accuracy and quality of responses depend on the accuracy of the language model and the code embeddings.

### Run App with Streamlit Cloud

[Launch App on Streamlit](https://ask-codebase.streamlit.app/)
