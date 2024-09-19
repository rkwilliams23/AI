from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Pinecone
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
import pinecone
import asyncio
from langchain.document_loaders.sitemap import sitemalLoader


#function to fench data from website
#https://python.langchain.com/docs/modules/data_connection/document_loaders/integrations/sitemap
def get_website_data(sitemap_url):
  
  loop = asyncio.new_event_loop()
  asyncio.set_event_loop()
  loader = SitemapLoader(
    sitemap_url
  )
  
  docs = loader.load()
  
  return docs

#Function to split data into smaller chunks
def split_data(docs):
  
  text_splitter = RecursiveCharacterTextSplitter(
    chunk_Size = 1000,
    chunk_overlap = 200,
    length_function = len,
  )
  
  docs_chunks = text_slitter.split_documents(docs)
  return docs_chunks

#Function to create embeddings instance
def create_embedding():
  
  embedding = SentenceTransformerEmbeddings(model_name="all-MinLM-L6-v2")
  return embeddings

#Function to push data to Pinecone
def push_to_pinecone(pinecone_apikey,pinecone_environment,pinecone_index_name,embeddeing,docs):
  
  pinecone.init(
    api_key=pinecone_apikey,
    environment=pinecone_environment
  )
  
  index_name = pinecone_index_name
  index = Pinecone.from_documents(docs, embeddings, index_name=index_name)
  return index
