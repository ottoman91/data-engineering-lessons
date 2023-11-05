
The following is the definition of the docker postgres image.

services:
  postgres:
    image: postgres:13
    environment:
      POSTGRES_USER: airflow
      POSTGRES_PASSWORD: airflow
      POSTGRES_DB: airflow
    volumes:
      - postgres-db-volume:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD", "pg_isready", "-U", "airflow"]
      interval: 5s
      retries: 5
    restart: always


* In the above docker postgres image, the `volumes` command tells us which file we need to map from the host machine to the container. This process is called mounting.

* We also need to map a port from the host machine to a port in the database, in order to be able to send requests to the container.




We can use the following command to run the docker postgres image.
docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:13

* pgcli is the python CLI program used for communicating with the postgres database
once its been set up.


* See all pyenv versions by running: `pyenv versions`

* Run a specific pyenv environment by running `pyenv activate [name_of_environment]`

After activating the pyenv environment, run this:
`pgcli -h localhost -p 5432 -u root -d ny_taxi`

* [NY Taxi Data Link](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)


* [Jan 2023 Yellow Taxi Parquet](https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet)

* [Data Dictionary](https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf)

* [potential link for iterating through parquet file](https://github.com/aws/aws-sdk-pandas/issues/660)


## parquet files

`pip install parquet-tools` install this to inspect parquet tools.

`parquet-tools inspect yellow_tripdata_2023-01.parquet` run this in the CLI to
read the metadata of the parquet file.

* [No MKL error](https://stackoverflow.com/questions/55778337/what-is-intel-mkl-fatal-error-cannot-load-libmkl-core-dylib-while-running-pysp)


