# Modern data stack - deploy dockerized dashboard into Azure web app

[00:00:00] Hello and welcome to this video where we'll continue on the previous video. In the previous video we have,

dockerized, data pipeline, and, orchestrating this with Dexter that we have. Dockerized it into a Dexter image. And this image we sent up to Azure Container Registry.

~~It's ~~the image is stored in container registry and then ~~we spin, ~~we create an Azure. Container instance, which connected to this, Azure Container Registry, this image, that we spin up a container. And this container, the idea is that ~~it will~~ it is ~~this the Dexter, it's ~~scheduled it will, automatically once per day.

~~We'll, give us we'll ~~orchestrate, D-L-T-D-B-T ~~and ~~into Duck db. And the Duck DB is stored in a file share in Azure as well. Okay. And also in file share, we had, profiles, YAML and DBT that ~~the ~~DBT ~~could~~ could [00:01:00] work, ~~in~~ in the deployed version. ~~Yes. ~~And, the idea with this video is that we'll continue on, the previous one.

We will create our, we have created our dashboard before, but now it's time to dockerize our dashboard as well. And then, send it up into container registry. And, then ~~we~~ we connect a, Azure web app to this, container registry. And then we have a deployed web application as well. And, the web application that is deployed, ~~it ~~means there's a URL that we can, go into and we are able to see our dashboard ~~and this dashboard is.~~

Connected to the file share of course. ~~It means that we will have our ~~once per day, when the data is, updated, even the dashboard will also be updated. That is really cool.

**Kokchun Giang-1:** Okay, starting in Azure, we have our Dexter container, and this Dexter container is connected to it has spin up this container from the image in [00:02:00] Azure Container Registry. Here we can go into this IP address. I'll copy this one and I'll go into ~~I will co go into. ~~Here in the browser, colon 3000, and you can see we're inside of text there, and you can see here in assets.

And here ~~they are material, ~~they have been materialized before. You can see the lineage here, the ~~D DB, DLTD, db ~~DBT for the rest of them. ~~They are, ~~first we move the data from the extract and load the data from the API into the staging layer of ddb. And then here they do a different transformation in the warehouse layer or the refine layer.

And then finally we have, the Marts layer, which, ~~is that this ~~is the one that is connected to the Streamli application. Okay? Yes. Now I will leave this Dexter. And we'll go back to Visual Studio Code. ~~This is what we started with la ~~This is what we had last time. We [00:03:00] have the docker file data warehouse, and we have the Docker file dashboard.

The Docker file dashboard, let's. Just remove this environment variable because we don't need that anymore since this is the one that will, be, sent in. ~~The, ~~this is, all that we need let's see. 8, 5 0 1. Yes, exactly. And and here you install ~~a lot. ~~A few things that is needed.

Okay. Save this one and let's go into our, docker compose YAML here. For the Docker compose yaml we should add a service here now. We add the service dashboard, colon build context dot. Docker file dashboard. This is the docker file that we use. And then ports, let's do ports [00:04:00] mapping.

8 5 0 1 2 8 5 0 1. Okay. And then we have the image here. ~~We have ~~the image here. We need to use the same as, ~~it's ~~the same login server. I'll copy this one.

This is the login server that we had last time. You can find it. If you don't remember it, you can find it in Azure Container Registry, your login server, and then slash what do we want ~~it~~ the image to be called. ~~And I, ~~I have a dashboard, colon latest. That is it. I saved this one. And now, ~~we, ~~let me see if there is anything else that we need.

Yeah, exactly.

~~We, ~~there is yeah, here, we need to go into our let's see dashboard here. And we have this connect data warehouse. Now the DB path it [00:05:00] needs to be changed. We changed it to the file share path. Let me remove, actually we can keep this one. We can do like this. We can call it ~~files share p, or ~~file share path like this equals to path.

Let me import path, from PO Lib import. Path,

path slash mount slash data slash job ads db. Okay, this is the path that we will need ~~to the file share~~ in Azure, and the file share will have job ads ~~tb. ~~I'll add in here. Actually ~~I can, instead of, ~~I can call it DB puff. It's simpler because I used DB puff before like this. Okay.

By changing this one, now we have, a connection to or we do need to do this mount~~ in ~~inside of web app [00:06:00] later on. But what you should know is that when this mount is up, we can connect to this job ads dotdb ~~and it's~~ and we can show our dashboard. That is the idea. Now what we should do is open up a terminal and we should do, docker compose, build our dashboard server that we don't build the data pipeline.

**Kokchun Giang-2:** One important thing that I forgot is that here in the Docker compose, we act since I am in an M three Mac an ARM-based Mac. If you have M1, M two, M three, M ~~four ~~chip, et cetera, then you need to add this one platform, colon Linux, a MD 64. Because otherwise we will have a platform of ARM 64 and the one in Azure is is in a and D 64.

It won't work for for the web app. We need to add this platform here. Platform Linux in D [00:07:00] 64.

**Kokchun Giang-3:** in order to save time in this video, I have actually run the commands. And the commands that you need to run is docker compose, build dashboard. Okay? This will build your dashboard and build the image of the dashboard. And then afterwards when you have it you basically do like this, paste this in.

No talker push. This login server and slash dashboard colon latest. Given that you have already signed into your Azure Container Registry, which we did in the last video, after you've done that, you have pushed it up and in your container registry, you should have two different, ~~contain~~ images now.

We go into here, this is the text container home, my resource groups and resource group analytics dev, and I have my. Here is my container registry, and inside [00:08:00] here we have repositories. And you can see there's a dashboard and there's a HR Dash pipeline. Now I have two images stored in my registry.

What we should do now is to go into home, create a resource, and I will need a web app. Create a web app.

To create a web app let's do like this. ~~We have, we choose our close this one. ~~We choose RG HR analytics Dev, this resource group and the web app name HR analytics, like this.

And then let's choose container Linux and the region. Let me choose here. Sweden Central

and the app. HR is not available in Sweden Central because someone else has taken it. 1101. I hope it's okay. Yes.

And here, let me see. [00:09:00] Yeah, this one is okay. ~~We can have a stronger one, but~~ actually, yeah, this one should be fine as well. You can choose, one that is stronger if you want. It doesn't matter right now. The thing is, I'm just see if it will work or not. And then afterwards, what you should do is that, in order to save credits, you should, delete ~~all ~~the whole resource group when you're finished with, this exercise.

In order to save your credits, ~~okay let's see. And then ~~let's move on to next and go into container. Here we will remove this sidecar support. This one will disappear and we'll choose Azure Container Registry. ~~And then ~~I'll choose this registry that I have and I'll choose admin credentials. ~~And here we have, ~~select the image dashboard.

~~Call on ~~latest ~~Yes. ~~Startup command. We don't need anything there. Then we do review and [00:10:00] create.

This will create, the web app, basically.

~~Yes. ~~Now it goes through the validation and then creates. ~~All right. ~~It's validating now, but it's deploying and hopefully this will work.

~~Yes, ~~it's deploying.

Now I'll close this down and wait until it's finished up.

**Kokchun Giang-4:** Yes. And ~~when the, ~~when this is done, you go into, the web app. Here is, the resource that you just click go to resource, and you come into here HR analytics, and now we go into, settings and we need to do some configurations in order to add our, mount our file share.

**Kokchun Giang-5:** Here you go into path mappings and inside of Path Map mappings, you can do new Azure storage mount. Click on this one. And we just call it file share and basic Yes. Storage account. Let's see, we have this STHR [00:11:00] analytics 1, 1 0 1. I'll choose that one. And here we have Azure files. SMB. Yes. And then the storage container.

Choose the data because this ~~is ~~was the storage container that we have created, and then the mount path slash m mt slash data and just click. Okay. This means that now our stream data application should be able to connect to this because we had this connect data warehouse, right? And this connect data warehouse, we connect to to, to this.

Now what is left is just~~ go ~~going into the app settings in the environment variables let's see, will be the you need to save it. Also save.

Now we have saved the configurations and go into environment variables. And we need to add a new one. I'll call it websites [00:12:00] port. And we'll have here value 8 5 0 1

and apply this one.

Okay. Now we should not go into the overview. Save this one as well. Apply, confirm. Yes. Now it has updated, we have this website support.

**Kokchun Giang-6:** firstly, I wanted to show you this. Here, this is an error that I got~~ when, ~~when I prepared this I clicked ~~on~~ on the link and, this is ~~what ~~the error I got. And the thing was that it was just a typo. You can see here ~~its ~~says, I cannot open database slash mount data slash job ads ddb.

And you can see DUCD kb. K and d needs to be changed. And if you followed along with the video and you also made the same mistake, then you know what to change. And afterwards when you have changed it ~~and ~~make sure that you, [00:13:00] do docker, build a docker compost build, and then you. Push this new, image to your, ~~a CR~~ Azure Container Registry.

And after you have done that, it's important that ~~you ~~in your web app, click restart ~~it. ~~You restart the one. And, usually it takes around like, since I chosen this very cheap, plan, then it takes like a few minutes before it's, working. But afterwards when, ~~when~~ it has been loaded, you can click on this link and you can see your fantastic Streamlet application here.

That is quite cool. And you can see the data here. That is really cool. This is deployed and you can use it and share it to your friends and family. Okay.

Okay. Wasn't this super cool? We managed to have our, dashboard application Dockerized, and then sent to push to a CR Azure Container Registry. And then ~~in our web ~~we created a web app in Azure's Azure web app and connected it to this [00:14:00] container in, a CR. And then we also made sure that we, had the file share the amount and then.

It was able to read the ~~D DB ~~database that we ~~can, ~~could see our Streamlet application live, deployed. That is, super cool. And, this, concludes like the whole pipeline is deployed, together with the dashboard. And since the pipeline is in container instance, it will run. Once, per day, and then we will have an updated dashboard for our end user to enjoy.

The next, steps, that you might, ~~figure thinking about should ~~think about when you're doing this kind of, pipeline is that, we need, now we have a, proof of concept that works. However, we need to make sure that, the price is, good enough. We need to think about, is there any better option?

Should we run the, container instance all the time? ~~Should, ~~or is it possible to schedule it somehow? That for example, half an hour before it starts, or like 10 minutes before it starts, we'll [00:15:00] start it that, you don't need to have it on all the time that ~~we, ~~it doesn't need to, ~~run, ~~take much cost ~~when,~~

unnecessarily costs. Is that a possibility? That is a question to explore. Yes. But I hope that you learned a lot in this video, and thank you for watching and see you in the next one. Bye.

