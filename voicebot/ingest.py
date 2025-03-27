from langchain_text_splitters import RecursiveCharacterTextSplitter
from huggingface_hub import login
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import Pinecone as LC_Pinecone  # LangChain Pinecone integration
from dotenv import load_dotenv
import os
from voicebot.data_converter import dataconveter
import pinecone
from pinecone import Pinecone as PC_Pinecone, ServerlessSpec

load_dotenv()

HUGGINGFACE_API_KEY =os.getenv("HUGGINGFACE_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = os.getenv("PINECONE_ENV")
PINECONE_INDEX = os.getenv("PINECONE_INDEX")

model_name = "sentence-transformers/all-mpnet-base-v2"
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': False}


hf = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)

pc = PC_Pinecone(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)
pinecone._client = pc

def ingestdata(status):
    """Ingests document embeddings into pinecone"""
    
    if status is None:
        docs = dataconveter()  # Ensure this function returns properly structured data
        if not docs:
            print("No documents found for ingestion.")
            return None, []
        try:
            # Create the vector store without passing a pinecone_client argument
            vstore = LC_Pinecone.from_documents(
                docs, 
                embedding=hf, 
                index_name=PINECONE_INDEX
            )
            inserted_ids = [doc.metadata.get("id", "unknown") for doc in docs]
            print(f"Inserted {len(inserted_ids)} documents into Pinecone.")
        except Exception as e:
            print("Error during document ingestion:", e)
            return None, []
        return vstore, inserted_ids
    else:
        # Load an existing index if data ingestion has already been performed
        try:
            vstore = LC_Pinecone.from_existing_index(
                index_name=PINECONE_INDEX,
                embedding=hf
            )
            print("Loaded existing Pinecone vector store.")
            return vstore, []
        except Exception as e:
            print("Error loading existing Pinecone vector store:", e)
            return None, []
    