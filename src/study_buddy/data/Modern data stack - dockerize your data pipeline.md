# Modern data stack - dockerize your data pipeline

[00:00:00] Hello and welcome to this video, which is a continuation on the previous video where we created a modern data stack project using Dexter and D to orchestrate DLT and DBT, and. Storing the data into dtb. Basically it's doing ELT inside and the data is stored in dtb. And then afterwards what you can do is to connect a Streamlet application, of course, and that I have shown in previous videos as well.

Here I will just, put in the STREAMLET code that you can see a front end of this. And then afterwards we will go to the main point of this video, which is to dockerize it. We'll containerize the whole data pipeline. And that is really cool because when you have containerized it, ~~it's in ~~it will work in every system.

You don't need to be dependent on. Particular parts of installations, et cetera. The idea is that when this works locally in my [00:01:00] computer very well, then I can easily just deploy it up into Azure and then Azure or a VS or Google Cloud platform or somewhere else. It's it should work as well.

And and that is really cool. What we'll do here and focus on in this video is to dockerize this.

**Kokchun Giang-1:** I've copied over the folders that I had in the previous lecture. It means that we have our data extract load for DLT. We have data transformation where we have DBT and we have data warehouse, which is this job ads Duck db. And then we have orchestration, which is the Dexter. What we need to do now is a new terminal.

And I will activate my virtual environment. ~~It's, I already activated. ~~I see. We'll go into orchestration and here I will run Dexter dev dash F definitions [00:02:00] and we can see that this is running our texter web server. Yes. I can click on this Dexter web server and you can see it running here. This is my Dexter web server, and you can see the assets here.

You can see the lineage. This is basically the lineage, okay? And the idea is that now I'm running this in local host, as you can see, local host 3000. ~~But I will close this down. ~~I will close this down. With Ctrl C, the idea is that we want to dockerize this. I want to dockerize this together with Dockerizing the Streamlet app.

For doing that, I will start with pasting in my Streamlet application. Then we will create a. Dashboard here. Another folder, dashboard, and the streamlet application is very simple. I'll just copy these files in here. [00:03:00] From my lecture notes and you can see here, connect Data Warehouse.

Basically what it does is that it goes into our DB path OS dot get, NV duck DB path. That means we will go in and create a dot e NV here and we will see what it's called, duck DB path. And this is basically the path to my duck db.

**Kokchun Giang-2:** I choose to write this path here, data warehouse slash job ads db, just to see that we can run it locally. ~~Because why do I do this? ~~Because in this connection now I've also added this from DV import Low DNV and low d nv. That is because we will go here and take the O os, get the NV that we get this ENV path.

This duct D Buff. Here we'll take from do NV now, but later on we'll send this into a dock. We'll dockerize this. We will send in [00:04:00] environment variable and we will change the path as well. We can see that I'm you not using PFL here, I can remove that one. And here you can see this is basically just a convenience function that we can connect to DDB and then do the query basically.

And then we have a dashboard here. And the dashboard is basically a Stream IT app that is very simple. We have simple layout, and then we run the layout basically like that. And in order to run this, we actually need to be in in the root folder because how I specified this path. I specified it as data warehouse, job ads, tech db, to run this one stream, lead, run dashboard.

Dashboard pi. Now I have run this one and you can see it works. That, that the reason why we choose I choose this path is because and why I choose to run it [00:05:00] from outside is that when I run it from the root here~~ it will go in will, ~~it will have the path to dockerize data pipeline.

And then slash and then it adds this path here. We go into data warehouse, we go into job ads, ddb, and this is then the absolute path that is used here for this query for this DDB dot Connect, that we can connect to this data warehouse, this TB file. Okay, that is basically how we run it locally.

Now we will try to dockerize this and to dockerize this. We start with creating a few docker files. I will have this in the root. I'll call this docker file.data warehouse because here I will~~ use I will ~~dockerized the data warehouse. Or dockerize basically the [00:06:00] pipeline to create this dashboard.

Or the pipeline to ingest the data to transform the data. Basically it's the the one that will create this DDB database. And then we will create one ~~for ~~for the Streamlet application. ~~We'll have one other one. ~~We'll have docker file dot dashboard. This is for the stream list application.

And here from Python three point 11 slim in. And then ENV. We choose which environment variable. We choose the D DB path. Equals to slash data warehouse slash job ads Duck bb. This is what we send in. Now you can see that okay. This is in [00:07:00] the root of our Docker container.

We have this data warehouse folder, and inside that we have this job, ads Tech db. And then we'll have work directory is in slash app slash dashboard. This is our work directory and we'll just copy our dashboard folder. This one will copy this folder dashboard into our into our slash app.

Slash dashboard. We just copy it in. And then we also need to run pip install Streamlet duck db, and Pandas ~~to ~~to run ~~this this ~~this streamlet application. Let's see. Do I need, yeah, I need Titan dash NV as well. In case we use the dot d nv and then command when I spin up this container, I wanted to run this [00:08:00] stream, it run dashboard dot pi

server port equals 85 0 1.

Dash server address is the local host, 0.0 0.0 0.0

basically like this. And then ~~we will have our ~~we will have our dashboard. ~~It, we, ~~we will orchestrate this with Docker compose that we'll have both this Docker file dashboard and this docker file data warehouse that they will be run. And then ~~we, ~~for, to do that, we'll create a docker dash compost yamo.

And here we'll have version let's see, 3.9. Actually, I don't think this is needed. Services data warehouse, [00:09:00] pipeline build and context. Okay. The context is dot. And then Docker file will choose the docker file we want. Docker file dot actually I can remove this fast. We'll start with just to show you that it works.

~~We'll go into, ~~it's inside of services. I'll go into dashboard first and build.

Build context dots. It means that we'll go into this let me just remove~~ data where, ~~remove this one. ~~Okay. ~~Context that we'll look into this folder here which the dot means. And then docker file will choose docker file dot dashboard. We'll choose here dockerfile dot dashboard, this one, and inside here we'll have volumes.

We'll have [00:10:00] volumes. Is this dot slash data. Warehouse colon slash data warehouse ro.

**Kokchun Giang-3:** Okay, RO means read only. Here we have our dashboard. Let me see. We have this data warehouse, we send it, we take this data warehouse folder, we send it into this slash data warehouse ~~in ~~in our container. Here we can go into ports. We need to do ports mapping. And we will do 8 5 0 1 2 8 5 0 1.

You can see the local host is 8 5 0 1. Like this. Now we have our dashboard ready, then we just do docker, compose up dash d.

And we'll see if this one works, because now this one [00:11:00] will run the docker file dashboard and inside there we will run the Streamlet apps. We'll see if this one works. It does a lot of installation now, run people install. You can see first time it takes a little bit of time, yeah, I will close this and yeah, it's finished. Okay, great. Now we should be able to go into local host 8 5 0 1 and run this one. And let me just check. Docker, PS And you can see ~~this one. ~~This one this event chair is running. It's up and you can see this port here. We should be able to just copy this one here and go into our browser and paste it in.

And you can see this dashboard is up now, and you can see here it's the local host 8 5 0 1. And this is the one that is in our Docker container. Cool. It [00:12:00] works. Okay. I'll just. Do Docker compose down to close this one down. Good. And now it's time for my other service. I'll create my data warehouse service.

But that one is dependent on the stock file data warehouse, I can write it first here. Okay, DDWH pipeline. And here we'll have build and same here. Context is dots and then Docker file. It's the doca file data warehouse. And here we'll have volumes. Let's see, volumes. We'll do a read only bind mount here, and note that this you can do for local development.

For local development we go into our home, we take our DBT slash profiles, [00:13:00] yaman. And then we send this into our pipeline. Pipeline slash profiles, yamo and read only. Okay, let me just yeah, the prettier doesn't work very well here, actually. I hope that this one works. Let's see.

Volumes. Maybe I have Misti, something I'm not sure. Volumes we will have another volume here dot slash data warehouse. We send this one into our data warehouse. This we create this data warehouse first this job as Duck db using our using this, and using our what is called Dexter, and then we send this folder into here.

Okay.

Let's see. But then ports [00:14:00] the ports ~~for ~~for Dexter is 3000. We have 3000 mapping towards 3000. Okay. Let's see if this one will work. The prettier doesn't work here. It doesn't yeah, it doesn't help me to okay. May, maybe I need to do this manually. Okay, better. Let's see, dashboard.

Actually, this ones need to go in here like this. These are part of the dashboard. Actually the dashboard, we don't need the volumes because we already have it. I think. No, actually not we need to put it in. Yes. Here we have the data warehouse pipeline. I just take like this. We have data warehouse pipeline, we have the dashboard, and this maps 3000 to 3000.

What remains is the dockerfile for data warehouse. Just ~~write this one and to ~~write this one. We do similar here from Python three point 11 HS three 11. I choose three 11 because I use three [00:15:00] 11 in my system. Otherwise we could choose a ~~new ~~newer version. It doesn't matter. ENV DBT profiles, directory is our slash pipeline

deck, db o equals slash warehouse slash job adsb.

These are the environment variables that we send in that we can use ~~them. ~~We'll have work directory is slash pipeline slash orchestration. This is where we will have our work directory inside of our container, and then we'll copy. Our data, we'll copy everything. Now. Our data extract load folder, this needs to be copied into our slash pipeline slash not orchestration, but data extract load, [00:16:00] and then we copy similarly, but we copy the transformation.

Data transformation. Into our data transformation here, like this. Copy this one, and now we'll copy our orchestration into pipeline slash orchestration like this. Or since we are in pipeline orchestration, we could do like dot. Okay. And now run PIP install. We need to have Dexter. We need to have Dexter dash DBT Dexter dash DLT Dexter dash web server.

We need DBT dash core. We need DBT dash db. We need [00:17:00] TLT. We need Tech db. Okay. And now we will do command. We'll run text there. We'll run dev, we'll run dash F and the definitions. File definitions. Do PI

dash h and the host is 0, 0 0 0. A local host. And the port is 3000. Okay, I think we've got it. Lemme just open a new terminal. Okay. I will ~~re ~~remove this data warehouse here. ~~This the duct B here, ~~since we have bind mounted. ~~We have done this docker compose here. We have bind mounted this.data, wear ~~this data warehouse folder to this data warehouse.

Whatever ends up in the inside of the container inside of [00:18:00] this data warehouse folder in the container it will end up here. In this data warehouse as well. That is the idea. Okay, now let's go into ls. We'll see our docker compose, ? Docker compose app dash D. Okay. It's installing a lot of things.

First time for this other image. With Docker Compose here, we have two services. We have two. Containers running. We have one that is data warehouse pipeline and one that is our dashboard.

Yes, it takes a little bit of time. The first time,

yeah, I can close this down and wait until it's finished.

**Kokchun Giang-4:** Okay, let's open up the browser to look into our~~ local host 3000. ~~Local host 3000. And you can see it works. However, there's some failure here. ~~Assets ~~we cannot see any assets reload definitions. Just to check out and we get an error [00:19:00] message here. What is the issue? It cannot find the dbt.

This profiles director, it cannot be found. ~~And the, that, ~~the problem is that I forgot to change a few things. We need to set those now. First in our definitions file here, we need to update a few things. We need to update let's see here. ~~We need to have a d ~~This is the DB path, ?

We'll have

remove this one and we'll have here duck DB path. Equals to os Get E nv. We need to pick our duck DB path and then we'll need to have our DBT profiles. Directory equals to os. Get NV DBT profiles [00:20:00] dear, because remember here. We send in our DBT profiles directory. We send in our duck DB path environment variables.

Then we need to import os. Okay? We get these things in our definitions files. Let's see. Is there something else that I have forgotten?

**Kokchun Giang-5:** take a look into this. We have DBT profiles DI did. ~~We take a look into DBT profiles. Did you can see ~~Yes, it is here. Good. ~~We have let's see. ~~We need to put in, in our DBT project, actually, DBT project~~ let's see. Project, yeah. ~~DBT, project director here, DBT project. ~~Let's see. ~~It's the DBT project and here we have project directory.

And here you see we have profiles. Di did. This is not correct anymore. We'll remove this one and instead here we'll have our~~ pro DT, let's see, ~~DBT profiles there. Okay, this is [00:21:00] very important. And also here in the destination, here we have ~~DDB path, ? ~~DDB Path. Now this should work in our docker containers.

Soon we'll actually go into our profiles as well. Let's go into our profiles. Open slash dot dbt slash profiles yaml. Here you can see there's a DBT Duck db. ~~This is we will do like this. ~~We'll change this to ~~DBT Duck db. Actually, we can still have it here, it doesn't matter. But I will change it here.~~

DBT Duck db Docker Local. And here we'll have Targets Dev, outputs Dev, and we'll have type db. We'll have the path and the path here. Let's pick that from our environment variable. ~~Enver ~~environment variable, and we'll pick Duck DB [00:22:00] under score path. Yeah, we don't need to install formatter for that.

Yes. This DVTD DB Docker Local, as you can see this is taking the environment variable, that DB path, which we have set and sent ~~in our, when we ~~in our docker file. I'll close this profiles yaml. And now we just need to do like this let me see in transformations. DBT project at yaml.

Here, we need to change this one that it points towards the correct one. Docker local. Save this one. Okay. ~~Don't ~~don't mind the red. It's just the editor that has problem. Okay. Let's do Docker. Compose down.

Docker Compose app dash D. Okay.

And now let's go into our browser. Reload this one. [00:23:00] Let's see. Go into our assets, reload definitions. Okay, there is still an error. Let me just close this one down. Go into browser again. Local host 3000. Yeah, there's still an error here. Let me debug and come back.

**Kokchun Giang-6:** Okay, with some debugging, I have managed to find the problem. ~~Here. We have here ~~I forgot this path here, but~~ we add, ~~I add this path that we have the path to DBT Profiles, directory and also remember in DBT project at yaml, we point towards DBT Duck DB Docker local. ~~And ~~and then when you have done the changes, you also need to do docker, compose down to close down everything, close down the containers, and then docker, compose up dash D.

But that is not enough because if the images already [00:24:00] existed ~~and, ~~and even if you change files, it'll just pick the old images, you can't force it to build dash build. When you run this one, it will run for a while and then afterwards it should work. For me, I've already done that.

I will just do docker compost app dash D. Now if I do Docker PS, you can see that I have two containers. I have the data pipeline here, and I have this. Dockerized Data pipeline dashboard. Then we can go ~~into browser and ~~into the browser. The local host 3000. And here you can see this is my Dexter.

Let's go into the assets. And you can see it has been loaded perfectly. ~~Okay? ~~View, lineage, it works, and we can materialize all. Then when it's materializing, you can see that this one will run here now, and then ~~this ~~this three will subsequently run. ~~Okay. ~~After we do this, you can see in our VS code that we will get back our job ads tech db, our [00:25:00] data will go there.

We'll go into the browser and you can see it's finished materializing, and then we can go into locals 85 0 1 and you can see the streaming dashboard works. ~~Okay, this this is how it worked. ~~We have managed to dockerize our pipeline and dockerize our dashboard.

Okay, in this video you've seen me working with Docker to containerize both the data pipeline and ~~to containerize the ~~the dashboard into two different services using Docker Compose. And~~ they were connecting to ~~they were pointing to two different Docker files. That is quite cool.

And~~ you, ~~you can see that it worked locally. The next step is to use this and push it to Azure. Azure Container Registry, and then connect it ~~towards an ~~to a web app. That will be really cool and I hope that you'll follow along and learn a lot more. Thank you for watching this video and see you in the next one.

Bye.

