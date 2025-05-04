from langchain_astradb import AstraDBVectorStore
from dotenv import load_dotenv
import os 
import pandas as pd
from data_ingestion.data_transform import Data_Converter


class Ingest_Data:

    def __init__(self):
        print('hello world')
    

    def data_ingestion(self):
        pass

if __name__=='__main__':
    data_ingestion=Ingest_Data()
    print(data_ingestion)
