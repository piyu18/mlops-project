import pandas as pd 
import numpy as np
from src.logger.logger import logging
from src.exception.exception import CustomException
import os, sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    raw_data_path:str = os.path.join('artifacts', 'raw.csv')
    train_data_path:str = os.path.join('artifacts', 'train.csv')
    test_data_path:str = os.path.join('artifacts', 'test.csv')

class DataIngestion:
    def __init__(self):
       self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info('Data ingestion started')
        try:
           #print(os.path.join("experiment", "data.csv"))
           data = pd.read_csv(os.path.join("experiment", "data.csv"))
           #print(data.head())
           logging.info('Reading dataframe') 
           os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)))
           data.to_csv(self.ingestion_config.raw_data_path,index = False)
           logging.info('raw data saved successfully')
           logging.info('Start train_test split')
           train_data, test_data = train_test_split(data, test_size=0.25)
           logging.info('train test split completed successfully')
           train_data.to_csv(self.ingestion_config.train_data_path,index = False)
           test_data.to_csv(self.ingestion_config.test_data_path,index = False)
           logging.info('data ingestion completed successfully')
           return(
               self.ingestion_config.train_data_path,
               self.ingestion_config.test_data_path
           )


        except Exception as e:
            logging.info('Exception occured while data ingestion')
            raise CustomException(e, sys)

if __name__ == '__main__':
    obj = DataIngestion()
    obj.initiate_data_ingestion()