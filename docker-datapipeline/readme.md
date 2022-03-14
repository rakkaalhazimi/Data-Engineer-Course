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
    -v d:/Python/Projects/DataEngineering/docker-datapipeline/ny_taxi_postgres_data:/var/lib/postgresql/data \
    -p 5433:5432 \
    --network=pg-network \
    --name pg-database \
    postgres:13
```


<br/>

# Connect to your postgres server
```
psql -h localhost -p 5433 -U root -d ny_taxi
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