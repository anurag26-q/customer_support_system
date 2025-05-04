from langchain_astradb import AstraDBVectorStore
from dotenv import load_dotenv
import os 
import pandas as pd
from data_ingestion.data_transform import Data_Converter
from langchain_google_genai import GoogleGenerativeAIEmbeddings 

load_dotenv()

ASTRA_DB_API_ENDPOINT=os.getenv('ASTRA_DB_API_ENDPOINT')
ASTRA_DB_APPLICATION_TOKEN=os.getenv('ASTRA_DB_APPLICATION_TOKEN')
ASTRA_DB_KEYSPACE=os.getenv('ASTRA_DB_KEYSPACE')
GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')

os.environ['GOOGLE_API_KEY']=GOOGLE_API_KEY
os.environ['ASTRA_DB_API_ENDPOINT']=ASTRA_DB_API_ENDPOINT
os.environ['ASTRA_DB_KEYSPACE']=ASTRA_DB_KEYSPACE
os.environ['ASTRA_DB_APPLICATION_TOKEN']=ASTRA_DB_APPLICATION_TOKEN


class Ingest_Data: 

    def __init__(self):
        self.embeddings=GoogleGenerativeAIEmbeddings(model='models/text-embedding-004')
        self.data_converter=Data_Converter()
    

    def data_ingestion(self,status):

        vectore_store =AstraDBVectorStore(
            embedding=self.embeddings,
            collection_name='chatbotecomm',
            api_endpoint=ASTRA_DB_API_ENDPOINT,
            token=ASTRA_DB_APPLICATION_TOKEN,
            namespace=ASTRA_DB_KEYSPACE
        )
        storage=status
        if storage==None:
            docs=self.data_converter.data_trasformation()
            inserted_ids=vectore_store.add_documents(docs)
            print(inserted_ids)
            return vectore_store,inserted_ids
        else:
            return vectore_store

if __name__=='__main__':
    ingest_data=Ingest_Data()
    vectore_store,inserted_ids=ingest_data.data_ingestion(None)
    print(f'Inserted {len(inserted_ids)} documnets')
    result=vectore_store.similarity_search('can you tell me low budget headphone')
    for res in result:
        print(f'{res.page_content} [{res.metadata}]')
