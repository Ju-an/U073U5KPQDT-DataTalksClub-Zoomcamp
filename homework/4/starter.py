#!/usr/bin/env python
# coding: utf-8


# In[8]:

import argparse
import pickle
import pandas as pd
import numpy as np


# In[11]:


YEAR = 2023
MONTH = 3


def main(year=YEAR, month=MONTH):

# In[3]:


    with open('model.bin', 'rb') as f_in:
        dv, model = pickle.load(f_in)


    # In[4]:


    categorical = ['PULocationID', 'DOLocationID']

    def read_data(filename):
        df = pd.read_parquet(filename)
        
        df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
        df['duration'] = df.duration.dt.total_seconds() / 60

        df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

        df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')
        
        return df


    # In[6]:


    df = read_data(f'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year:04d}-{month:02d}.parquet')


    # In[7]:


    dicts = df[categorical].to_dict(orient='records')
    X_val = dv.transform(dicts)
    y_pred = model.predict(X_val)


    # In[10]:


    print(f'STD: {np.std(y_pred)}')
    print(f'Mean: {np.mean(y_pred)}')

    # In[12]:


    df['ride_id'] = f'{year:04d}/{month:02d}_' + df.index.astype('str')

    df_result = df[['ride_id']].copy()
    df_result['prediction'] = y_pred
    output_file = 'predictions.parquet'

    df_result.to_parquet(
        output_file,
        engine='pyarrow',
        compression=None,
        index=False
    )

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--year', type=int, default=YEAR)
    parser.add_argument('--month', type=int, default=MONTH)

    args = parser.parse_args()
    main(args.year, args.month)

