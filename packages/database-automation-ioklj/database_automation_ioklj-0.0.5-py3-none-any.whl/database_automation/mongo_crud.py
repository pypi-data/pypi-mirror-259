from pymongo.mongo_client import MongoClient
import pandas as pd
import numpy as np

class MongoDBOperation:
    
    def cleanCollection(self, uri, databaseName, collectionName):
        client = MongoClient(uri)

        database = client[databaseName]

        collection = database[collectionName]
        
        collection.drop()

    def get_collection(self, uri, databaseName, collectionName):
        client = MongoClient(uri)

        database = client[databaseName]

        collection = database[collectionName]

        return collection
    
    def insertOneDataPoint(self, uri, databaseName, collectionName, document):
        client = MongoClient(uri)

        database = client[databaseName]

        collection = database[collectionName]

        collection.insert_one(document)

    def insertDataIntoCollection(self, uri, databaseName, collectionName, fileName):
        client = MongoClient(uri)
        
        database = client[databaseName]
        
        collection = database[collectionName]
        
        dataframe = pd.read_csv(fileName)
        
        for i in range(0,dataframe.shape[0]):
            dataRow = dataframe.iloc[i,0:].values
            document = {'customer_id':int(dataRow[0]), 'credit_score':int(dataRow[1]), 'country':dataRow[2], 'gender':dataRow[3], 'age':int(dataRow[4]), 'tenure':int(dataRow[5]), 
                         'balance':dataRow[6], 'products_number':int(dataRow[7]), 'credit_card':int(dataRow[8]), 'active_member':int(dataRow[9]), 'estimated_salary':dataRow[10], 
                         'churn':int(dataRow[11])}
            collection.insert_one(document)
