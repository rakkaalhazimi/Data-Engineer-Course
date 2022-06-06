# Build docker image
Build your data pipeline image using Dockerfile
```
docker build -t test:pandas
```

<br/>

# Run test:pandas container
Run your image as a container
```
docker run -it --rm test:pandas
```  

<br/>

# Docker Network
Create docker network for pg-admin and pg-database
```
docker network create pg-network
```

<br/>

# Run Postgres
Build postgress server and append data inside it
```
docker run -it --rm \
    -e POSTGRES_USER="root" \
    -e POSTGRES_PASSWORD="root" \
    -e POSTGRES_DB="ny_taxi" \
    -v d:/Programming/Python/Projects/DataEngineering/docker-datapipeline/ny_taxi_postgres_data:/var/lib/postgresql/data \
    -p 5432:5432 \
    --network=pg-network \
    --name pg-database \
    postgres:13
```


<br/>

# Connect to your postgres server
Connect to the postgres on localhost, the port number 5432 might not working, change to 5433
when using docker container without docker network
```
psql -h localhost -p 5432 -U root -d ny_taxi
```

<br/>

# Run PgAdmin on container
```
docker run -it --rm \
    -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
    -e PGADMIN_DEFAULT_PASSWORD="root" \
    -p 8080:80 \
    --network=pg-network \
    --name pg-admin \
    dpage/pgadmin4
```

<br>

# Build docker image for ingest data
Build your data pipeline image using Dockerfile
```
docker build -t taxi_ingest:v001 .
```
<br>

# Run local server through python http module
In order for your docker container to get the csv file quickly, use local server
rather than internet
```
python -m http.server
```

<br>

# Ingest data with python from docker container
After everything is set, you can start ingesting your csv data into postgres.
Use your ipv4 address as url base.
```
docker run -it --rm  \
    --name ingest_csv  \
    --network=pg-network  \
    taxi_ingest:v001  \
    --user=root  \
    --password=root  \
    --host=pg-database  \
    --port=5432  \
    --db=ny_taxi  \
    --table_name=yellow_taxi_data  \
    --url=http://172.20.208.1:8000/yellow_tripdata_2021-01.csv  \
```

<br>

# Run with Docker Compose
Wrap above docker command inside docker-compose file, see docker-compose.yaml, then run:
```
docker-compose up
```

Navigate to your pgadmin again. After that press `ctrl+c` on the terminal and type:
```
docker-compose down
```
to shut them down.

You can run on the detached mode with
```
docker-compose up -d
```