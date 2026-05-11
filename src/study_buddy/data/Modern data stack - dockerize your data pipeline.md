Modern Data Stack - Dockerize Your Data Pipeline

Hello and welcome to this video, which is a continuation of the previous video.

Previously we created a modern data stack project using:

Dagster
DLT
DBT
DuckDB

Dagster orchestrated DLT and DBT.

The data was stored inside DuckDB.

Basically we performed ELT workflows and stored everything inside DuckDB.

Afterwards, we could connect a Streamlit application as the frontend dashboard.

In this video, I will:

add the Streamlit frontend
dockerize the full pipeline
containerize the dashboard

This is really cool because once the application is containerized, it can run consistently on every system.

You are no longer dependent on specific local installations.

If the project works locally on my computer, I can easily deploy it to:

Azure
AWS
Google Cloud Platform

or anywhere else.

That is the focus of this video.

Project Structure

I copied the folders from the previous lecture.

We now have:

data_extract_load → DLT
data_transformation → DBT
data_warehouse → DuckDB database
orchestration → Dagster

Now I activate the virtual environment and run:

dagster dev -f definitions.py

This starts the Dagster web server.

When I open the browser, I can see:

assets
lineage
orchestrated pipelines

The Dagster UI runs locally on:

localhost:3000

Now I stop the server because we want to dockerize everything.

Adding the Streamlit Dashboard

Next I create a folder called:

dashboard

I copy in the Streamlit application files.

Inside the dashboard we have a helper function called:

connect_data_warehouse

This function connects to DuckDB.

The DuckDB path is read from an environment variable using:

os.getenv("DUCKDB_PATH")

We also use:

python-dotenv

to load variables from .env.

Locally, the .env file contains:

DUCKDB_PATH=data_warehouse/job_ads.duckdb

This lets the Streamlit app connect to the DuckDB database locally.

Then we run the dashboard using:

streamlit run dashboard/dashboard.py

The Streamlit dashboard now works locally.

Creating Dockerfiles

Now we create two Dockerfiles:

Dockerfile.data_warehouse
Dockerfile.dashboard

The dashboard Dockerfile handles the Streamlit frontend.

Dockerfile.dashboard

We start with:

FROM python:3.11-slim

Then we define environment variables.

Example:

ENV DUCKDB_PATH=/data_warehouse/job_ads.duckdb

Next:

set the working directory
copy the dashboard folder
install dependencies

Dependencies include:

streamlit
duckdb
pandas
python-dotenv

Then we define the startup command.

The container launches Streamlit on port:

8501

using:

0.0.0.0

so the container exposes the app externally.

docker-compose.yml

Now we create:

docker-compose.yml

We define services.

First we create the dashboard service.

The service:

builds from Dockerfile.dashboard
mounts the data_warehouse folder
maps port 8501

The volume mount is:

./data_warehouse:/data_warehouse:ro

ro means read-only.

Now we run:

docker compose up -d

Docker builds the image and starts the container.

Then we verify with:

docker ps

We can now open:

localhost:8501

and see the Streamlit dashboard running from inside the Docker container.

Very cool.

Dockerizing the Data Pipeline

Now we add another service:

data_warehouse_pipeline

This service uses:

Dockerfile.data_warehouse

We also mount:

DBT profiles
data warehouse folder

For local development, we bind mount:

~/.dbt/profiles.yml

into the container.

We also expose port:

3000

for Dagster.

Dockerfile.data_warehouse

Again we start with:

FROM python:3.11-slim

We define environment variables:

DBT_PROFILES_DIR
DUCKDB_PATH

Then we:

set the working directory
copy DLT files
copy DBT files
copy orchestration files

Next we install dependencies:

dagster
dagster-dbt
dagster-dlt
dagster-webserver
dbt-core
dbt-duckdb
dlt
duckdb

Finally we launch Dagster using:

dagster dev -f definitions.py

with host:

0.0.0.0

and port:

3000

Running Both Containers

Now we run:

docker compose up -d

This starts:

dashboard container
data pipeline container

After startup we open:

localhost:3000

Dagster loads successfully.

However, initially there is an error.

The DBT profiles directory cannot be found.

Fixing the Environment Variable Issues

Inside definitions.py we update the code.

We replace hardcoded paths with environment variables.

We use:

os.getenv("DUCKDB_PATH")
os.getenv("DBT_PROFILES_DIR")

We also update:

dbt_project.yml

to use the correct profile:

dbt_duckdb_docker_local

Inside profiles.yml we configure:

DuckDB
the environment variable path

using:

env_var("DUCKDB_PATH")

Now DBT correctly reads the DuckDB path from Docker environment variables.

Rebuilding Containers

After changing files, simply running:

docker compose up -d

is not enough.

Docker may reuse old cached images.

We must rebuild everything using:

docker compose up -d --build

This forces Docker to rebuild the containers.

After rebuilding:

Dagster works
assets load correctly
lineage is visible
materialization succeeds

The DuckDB database gets recreated.

Then the Streamlit dashboard also works again on:

localhost:8501

Final Result

We successfully:

dockerized the data pipeline
dockerized the dashboard
orchestrated everything with Docker Compose

The project now contains two services:

Data pipeline service
Dashboard service

Everything works locally inside containers.

The next step is deploying to Azure:

push images to Azure Container Registry
connect them to Azure Web App

That will be really cool.

I hope you learned a lot in this video.

Thank you for watching.

See you in the next one.

Bye.