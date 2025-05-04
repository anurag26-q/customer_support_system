import  pandas as pd
from langchain_core.documents import Document


class Data_Converter:
    def __init__(self):
        self.product_data=pd.read_csv(r'F:\customer_support_system\customer-support-system\data\processed\flipkart_product_review.csv')
        # print(self.product_data.head())

    def data_trasformation(self):
        required_columns=self.product_data.columns
        required_columns=list(required_columns[1:])
        # print(required_columns)
        product_list=[]
        for index,row in self.product_data.iterrows():
            object={
                'product_name':row['product_title'],
                'product_rating':row['rating'],
                'product_summary':row['summary'],
                'product_review':row['review']
            }
            product_list.append(object)

        # print(product_list)
        docs=[]
        for entry in product_list:
            metadata={'product_name':entry['product_name'],
                      'product_rating':entry['product_rating'],
                      'product_summary':entry['product_summary']
                      }
            doc=Document(page_content=entry['product_review'],metadata=metadata)
            docs.append(doc)
        # print(docs[0])
        return docs




if __name__=='__main__':
    data=Data_Converter()
    data.data_trasformation()
