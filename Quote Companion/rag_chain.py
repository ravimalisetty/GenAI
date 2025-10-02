from langchain_community.vectorstores import Chroma #This imports ChromaDB as your vector store — it will hold your embedded quotes for retrieval
from langchain_community.embeddings import HuggingFaceEmbeddings #This loads a sentence transformer from HuggingFace to convert your quotes into vector embeddings.
from langchain_community.llms import HuggingFacePipeline #this lets you use a HuggingFace model for text generation
from langchain.chains import RetrievalQA #This is the core LangChain class that combines retrieval + generation - the heart of your RAG pipeline
from langchain.document_loaders.csv_loader import CSVLoader # This loads your quotes.csv file and turns each row into a document LangChain can process


#Define a function to build and return your RAG pipeline
def build_rag_chain():
    # Load your CSV file from the data folder. Each row becomes a retrievable document
    loader = CSVLoader(file_path="data/quotes.csv")
    documents = loader.load()

    # Use HuggingFace’s default embedding model (e.g., all-MiniLM-L6-v2) to embed your quotes.
    embeddings = HuggingFaceEmbeddings()

    # Store the embedded quotes in ChromaDB so you can search them by theme
    vectordb = Chroma.from_documents(documents, embedding=embeddings)

    # Convert the vector store into a retriever object — this will fetch relevant quotes
    retriever = vectordb.as_retriever()

    # Load a lightweight HuggingFace model (distilgpt2) for generating responses. You can swap this later.
    llm = HuggingFacePipeline.from_model_id(model_id="distilgpt2", task="text-generation")

    #Combine the retriever and LLM into a RetrievalQA chain and return it
    chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return chain