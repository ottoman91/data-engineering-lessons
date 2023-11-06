#!/usr/bin/env python
# coding: utf-8

import argparse
import pandas as pd
import os

#pip install -U SQLAlchemy

from sqlalchemy import create_engine
import pyarrow.parquet as pq



def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url

    parquet_file_link = "yellow_tripdata_2023-01.parquet"

    os.system('pip install wget')
    os.system(f"wget {url} -O {parquet_file_link}")

    dataset_parquet = pd.read_parquet(parquet_file_link, engine="pyarrow")

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    engine.connect()

    dataset_parquet.head(n=0).to_sql(
        name=table_name,
        con=engine,
        if_exists='replace'
    )

    parquet_file = pq.ParquetFile(parquet_file_link)

    for table in parquet_file.iter_batches(batch_size=10000):
        df = table.to_pandas()
        df.to_sql(name=table_name,con=engine,if_exists='append')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Ingest Parquet data to Postgres.')

    parser.add_argument('--user', help='User name for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--db', help='database name for postgres')
    parser.add_argument('--table_name', help='name of table where we will write results')
    parser.add_argument('--url', help='link to the parquet file')

    args = parser.parse_args()

    main(args)
