#!/usr/bin/env python
# coding: utf-8

import argparse
import os
from time import time

import pandas as pd
from sqlalchemy import create_engine


def main(params):

    # Parameter
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url


    # Set SQLAlchemy Connection
    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")

    # Download CSV
    csv_name = "output.csv"
    os.system(f"wget {url} -O {csv_name}")

    # Read and Get Schema
    df_iter = pd.read_csv(csv_name, iterator=True, nrows=100_000, chunksize=10_000)
    df = next(df_iter)

    # Change some of the data type to datetime
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    # Commit to Database
    # Sample code to insert dataframe to database
    df.head(0).to_sql(name=table_name, con=engine, if_exists="replace")
    df.to_sql(name=table_name, con=engine, if_exists="append")
    
    while True:
        start = time()

        try:    
            chunk = next(df_iter)
        except StopIteration:
            print("Ingestion finished !")
            break
        
        # Change some of the data type to datetime
        chunk.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        chunk.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

        chunk.to_sql(name=table_name, con=engine, if_exists="append")

        end = time()
        print("Inserted another chunk for {:.2f} second".format(end - start))
    
    
if __name__ == "__main__":
    # Arguments for user, password, port, dbname, table name, url of the csv
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres.')
    parser.add_argument('--user', required=True, help='user name for postgres')
    parser.add_argument('--password', required=True, help='password for postgres')
    parser.add_argument('--host', required=True, help='host for postgres')
    parser.add_argument('--port', required=True, help='port for postgres')
    parser.add_argument('--db', required=True, help='database name for postgres')
    parser.add_argument('--table_name', required=True, help='name of the table where we will write the results to')
    parser.add_argument('--url', required=True, help='url of the csv file')

    args = parser.parse_args()

    main(args)


