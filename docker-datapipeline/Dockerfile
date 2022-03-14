FROM python:3.9

RUN apt-get install wget
RUN pip install pandas psycopg2 sqlalchemy


WORKDIR /app
COPY ingest_data.py ingest_data.py

ENTRYPOINT [ "python", "ingest_data.py" ]


# Simple Pipeline
# FROM python:3.9

# RUN pip install pandas

# WORKDIR /app
# COPY pipeline.py pipeline.py

# ENTRYPOINT [ "python", "pipeline.py" ]