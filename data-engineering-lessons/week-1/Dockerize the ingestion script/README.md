* We need to convert the code in the jupyter notebook to a Python script that we can then run directly in the Docker container to copy the parquet file with the data to a postgres database.

* The following command converts a jupyter notebook to a Python script: `jupyter nbconvert --to=script upload-data.ipynb`

* Clean the script that was generated.

* We can run the following command in CLI to test that the script works:


```
URL="https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet"
python ingest_data.py \
  --user=root \
  --password=root \
  --host=localhost \
  --port=5432 \
  --db=ny_taxi \
  --table_name=yellow_taxi_trips \
  --url=${URL}
```


* need to install wget on mac, using `brew install wget`.


* After writing the `Dockerfile`, we can run the following command to build
the docker image to Dockerize the ingestion script.`docker build -t taxi_ingest:v001 .`

* Run the following command to run the docker image after it has been built:

```
docker run -it \
  --network=pg-network \
  taxi_ingest:v001 \
    --user=root \
    --password=root \
    --host=pg-database \
    --port=5432 \
    --db=ny_taxi \
    --table_name=yellow_taxi_trips \
    --url=${URL}

```
