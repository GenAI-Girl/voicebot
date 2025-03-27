from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def dataconveter():

    directory_path = ("/Users/ritzyk/Downloads/voicebot-main 2/data")

    loader = PyPDFDirectoryLoader(directory_path)
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    docs = text_splitter.split_documents(docs)
    return docs