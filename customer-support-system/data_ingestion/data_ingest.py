from langchain_astradb import AstraDBVectorStore
from dotenv import load_dotenv
import os 
import pandas as pd
from data_ingestion.data_transform import Data_Converter

load_dotenv()
ASTRA_DB_API_ENDPOINT=os.getenv('ASTRA_DB_API_ENDPOINT')
ASTRA_DB_APPLICATION_TOKEN=os.getenv('ASTRA_DB_APPLICATION_TOKEN')
ASTRA_DB_KEYSPACE=os.getenv('ASTRA_DB_KEYSPACE')
GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')



class Ingest_Data: 

    def __init__(self):
        print('hello world')
    

    def data_ingestion(self):
        pass

if __name__=='__main__':
    data_ingestion=Ingest_Data()
    print(data_ingestion)
