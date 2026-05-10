Modern Data Stack - Deploy Dockerized Dashboard into Azure Web App

Hello and welcome to this video where we’ll continue from the previous video.

In the previous video, we:

dockerized the data pipeline
orchestrated it with Dagster
created a Dagster image
pushed the image to Azure Container Registry

The image is stored inside Azure Container Registry.

Then we created an Azure Container Instance connected to that registry.

The container was spun up from the Dagster image.

The idea is that Dagster is scheduled to run automatically once per day.

Dagster orchestrates:

DLT
DBT
DuckDB

The DuckDB database is stored inside an Azure File Share.

Inside the file share we also stored:

profiles.yml
DBT configuration

so that DBT works correctly in the deployed environment.

In this video, we continue from there.

Previously we created our dashboard.

Now it’s time to:

dockerize the dashboard
push it to Azure Container Registry
connect an Azure Web App to the container

Then we will have a deployed web application.

The deployed web app will provide a URL where we can access our dashboard.

The dashboard is connected to the Azure File Share.

That means when the data updates once per day, the dashboard also updates automatically.

That is really cool.

Starting in Azure

We already have our Dagster container running.

The container was created from the image stored in Azure Container Registry.

We can open the Dagster UI in the browser using the IP address and port 3000.

Inside Dagster we can see the assets.

The assets have already been materialized.

We can see the lineage:

DLT
DBT
marts layer

First, the data is extracted and loaded into the staging layer in DuckDB.

Then DBT transforms the data into the warehouse/refined layer.

Finally we create the marts layer.

The marts layer is connected to the Streamlit dashboard application.

Now let’s move back to Visual Studio Code.

Dockerizing the Dashboard

Previously we created:

Dockerfile for the data warehouse
Dockerfile for the dashboard

Inside the dashboard Dockerfile, we remove unnecessary environment variables.

We expose port:

8501

because Streamlit uses that port.

Updating docker-compose.yml

Now we add another service.

We create a service called:

dashboard

with:

build context
Dockerfile
port mapping

Port mapping:

8501:8501

We also define the image name.

We use the Azure Container Registry login server.

Example:

<login-server>/dashboard:latest

You can find the login server inside Azure Container Registry.

Connecting to Azure File Share

Next we update the dashboard code.

Inside the dashboard project we modify the DuckDB connection path.

We use:

/mount/data/job_ads.duckdb

This path points to the mounted Azure File Share.

Later, inside Azure Web App, we will mount this file share.

Once mounted, the Streamlit dashboard can connect to the DuckDB database.

That is the idea.

ARM Macs and Platform Issue

One important thing:

I am using an M3 Mac, which uses ARM architecture.

If you use:

M1
M2
M3
M4

you must add:

platform: linux/amd64

inside docker-compose.

Otherwise Docker builds an ARM image, but Azure Web App expects AMD64.

Without this setting, the deployment will fail.

Building and Pushing the Dashboard Image

The commands are:

Build the dashboard image:

docker compose build dashboard

Then push it:

docker push <login-server>/dashboard:latest

This assumes you already authenticated with Azure Container Registry.

After pushing, Azure Container Registry should contain two repositories:

dashboard
hr-dash-pipeline

Now we move into Azure.

Creating the Azure Web App

Go to:

Create Resource → Web App

Select:

resource group
web app name
container deployment
Linux

Choose a region.

Then configure the container settings.

Disable sidecar support.

Choose:

Azure Container Registry
your registry
admin credentials

Select the image:

dashboard:latest

Then review and create.

Azure now deploys the web app.

Mounting Azure File Share

After deployment, open the Web App resource.

Go to:

Settings → Path mappings

Create a new Azure Storage Mount.

Select:

Azure Files
the storage account
the file share named data

Mount path:

/mount/data

Now the Streamlit dashboard can access:

/mount/data/job_ads.duckdb

which matches the connection path in the dashboard code.

Save the configuration.

Setting the Streamlit Port

Now go to:

Environment Variables

Create:

WEBSITES_PORT = 8501

Save and apply the changes.

This tells Azure Web App which port Streamlit uses.

Fixing Deployment Error

While preparing the deployment, I encountered an error.

The issue was simply a typo.

The database path was misspelled.

If you made the same mistake, correct the path to:

/mount/data/job_ads.duckdb

After fixing it:

rebuild the Docker image
push the updated image to Azure Container Registry
restart the Web App

Since I chose a very cheap hosting plan, startup may take a few minutes.

Eventually the Streamlit application loads successfully.

Now we can see the dashboard live in the browser.

That is really cool.

You can even share the dashboard URL with friends and family.

Final Result

Now we have:

a dockerized dashboard
pushed to Azure Container Registry
connected to Azure Web App
mounted to Azure File Share
connected to the DuckDB database

The full modern data stack pipeline is now deployed.

The pipeline runs once per day using the Azure Container Instance.

The dashboard automatically updates with fresh data.

Next Steps and Optimization

Now we have a working proof of concept.

But there are still engineering questions to think about.

For example:

Is the pricing efficient?
Should the container instance run continuously?
Can we schedule startup only when needed?
Can we reduce unnecessary costs?

These are important production considerations.

I hope you learned a lot in this video.

Thank you for watching.

See you in the next one.

Bye.