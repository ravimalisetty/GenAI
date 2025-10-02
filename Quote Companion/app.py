from langchain_community.vectorstores import Chroma
import gradio as gr
from rag_chain import build_rag_chain
from langchain_community.embeddings import HuggingFaceEmbeddings
#from langchain.chains import RetrievalQA

# Initialize the RAG pipeline once when the app starts
rag_chain = build_rag_chain()

# Define a function that takes a user theme (e.g., “courage”), runs it through the chain, and returns the generated response
def get_quote(theme):
    response = rag_chain.run(theme)
    return response

# Build and launch the Gradio interface
gr.Interface(
    fn=get_quote, # The function to call when the user submits a theme
    inputs="text", # A single text input for the theme
    outputs="text", # A single text output for the generated quote
    title="Quote Companion", # The title of your app
    description="Enter a theme or emotion to receive a meaningful quote." # A brief description
).launch()

