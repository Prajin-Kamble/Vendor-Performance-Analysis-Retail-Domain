from numpy import load
import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

logging.basicConfig(
    filename='drive/MyDrive/Vender Performance Analysis Project/logs/.log',
    level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a'
    )

engine = create_engine('sqlite:///inventory.db', echo=False)

def ingest_db(df, table_name, engine):
  ''' This function will ingest the dataframe into database table '''
  
  df.to_sql(table_name, con=engine, if_exists='replace', index=False)


def load_raw_data():
  ''' This function will load the CSVs as dataframe and ingest into db '''

  start = time.time()
  for file in os.listdir('drive/MyDrive/Vender Performance Analysis Project/Data/'):

    if '.csv' in file:
      df = pd.read_csv('drive/MyDrive/Vender Performance Analysis Project/Data/' + file)
      logging.info(f'Ingesting {file} in db')
      ingest_db(df, file[:-4], engine)

  end = time.time()
  total_time = (end-start)/60

  logging.info('--------------Ingestion successfully complete----------------------')
  logging.info(f'\n Total time taken: {total_time} minutes')

if __name__ == '__main__':
  load_raw_data()