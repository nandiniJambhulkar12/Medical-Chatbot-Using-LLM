from dotenv import load_dotenv
import os
from src.helper import (
    load_pdf_file,
    filter_to_minimal_docs,
    text_split,
    download_hugging_face_embeddings
)
from pinecone import Pinecone, ServerlessSpec 
from langchain_pinecone import PineconeVectorStore

# Load environment variables from .env file
load_dotenv()

# Get API keys from environment
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

# ✅ Error handling for missing keys
if not PINECONE_API_KEY:
    raise ValueError("❌ Missing PINECONE_API_KEY in .env file.")
if not TOGETHER_API_KEY:
    raise ValueError("❌ Missing TOGETHER_API_KEY in .env file.")

# Load and prepare data
extracted_data = load_pdf_file(data='data/')
filtered_data = filter_to_minimal_docs(extracted_data)
text_chunks = text_split(filtered_data)

# Load embeddings
embeddings = download_hugging_face_embeddings()

# Initialize Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)
index_name = "medical-bot"

# Create index if not exists
if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )

# Connect to index
index = pc.Index(index_name)

# Upload documents to Pinecone
docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings,
)

print("✅ Indexing complete.")
