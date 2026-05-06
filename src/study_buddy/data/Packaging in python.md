# Packaging in python

[00:00:00] Hello and welcome to this lecture where we'll go into packaging a Python project. ~~And ~~as you will see, packaging a Python project will make it much simpler with importing because as you might have noticed when you're importing modules from different folders, it might give you troubles in Python.

However, ~~whenever, ~~when you have packaged it, you can. pip install it. And when you have pip installed it as a package it is very intuitive to use the modules that you have created. So we will create a real application here that we'll call the travel planner that will use an API.

And as you will see, this application contains a lot of different modules separated into different directories. And this is ~~a ~~kind of the idea so that you can see when you're growing a larger and larger project you really should package it

we will move on to a visual studio code.

[00:01:00] So in a previous lecture, you have already seen me working with travel API from traffic lab. So I won't go through that. ~~Again, instead you will go in, ~~you can go in there ~~to ~~to look at my previous lecture.

So I'll just create a new terminal. And let's start with creating a virtual environment. So uv venv. So now we have a virtual environment. Let's activate that source. vnv, bin activate. Okay. It has been activated and you can see that from the parentheses, but it's not always sure that the parentheses is there.

~~It's ~~depends on how your terminal is configured. So sometimes it might not be there. And then you can just do echo to check that you are there. So virtual. Underscore the virtual ENV. Like this, you have here and virtualenv, it means that you will take this variable and if you're typing this one, you should get something with vnv here.

If this is empty, then you're not in a virtual environment. It is as simple as that. [00:02:00] Okay? So I will clean this terminal and let's move on. Let's start with installing a package. Actually, should I install a package? No, I should not. I will create some folders now. So makedir, I will create a backend.

I'll create a frontend folder and I'll create a utils folder like this. Okay, so now we have~~ three, ~~three folders and I will put in some let's try it. ~~Okay. ~~Going into the backend first, I will create so touch let's see backend slash ~~what do I want? I want to have ~~connect to API dot ~~PI.~~

So here I have created~~ this this Python ~~this Python module. So let's create another one. ~~Backend. Let's see, ~~backend slash trips, ~~pi. Okay. ~~And then in front end, let's create the touch dashboard, ~~pi ~~and touch plot maps, ~~pi. ~~This will continue. Oh, actually, ~~I~~ I put them [00:03:00] outside, but they should be inside.

So let's move them. ~~And the bot maps ~~into front end flash lots. Maps. py, ~~so I moved it, ~~move it inside MV~~ let's see, I want to move ~~dashboard into dashboard. py here. So I basically just move these two. So you can see in the front end, we have this ones and in utils, I will create a constants.

So let's do that. Touch. Utils slash constants. py, like this. And also I will create another directory called tests. And an explorations directory. Okay, so now you can see that this project is already growing. But we can see that the scripts are empty. All of them are empty, right? So if I go into each of them, they're empty.

And these folders are empty right now, but [00:04:00] let's create something more. Let's do touch. Exploration slash exploring travel planner dot I've been B. So I have this one here and yes, basically like this utils, we have some helper functions. We should have a touch in utils. I want to have a run dashboard as well.

Okay. So now you can see that we have created the same kind of skeleton for this project. And ~~you ~~usually it's not that I have all of this in my mind directly when I'm creating a project, so I don't create the whole scale, everything~~ all the ~~all the scripts in my projects in from the start instead, I will create some skeleton Parts for example, back and front end useful and some explorations also useful and tests [00:05:00] and utils.

So these folders are quite good for a starting point. But okay, let's let's continue. Let's do something~~ sim ~~simple to start here. Let's go into my backend, Connector API. I will actually, and also I will have a env file. I forgot that, patch. env. ENV and in the ENV file, of course you should put in your credentials for API key so that you can use that one. So I will pause this video and come back.

Okay, I've placed my API key into my env and now I will copy and paste the code from the lecture note. And actually in the lecture note I didn't have this if tandem name equals tandem main. But I will have that and I will just test this out to see that it works. So When I'm running this one, you can see that, yeah, it works.

I get the data so it is just using this method. So [00:06:00] I'm creating a class from this re robot. I'm creating an instance from this s robot class and from this instance I use this method. And this method basically goes into a, an endpoint with a default location ID. So then I get back the timetable here for this particular location ID.

And you know from last lecture how to obtain the location ID for a particular location. So I won't go through that. Instead you can see that this works. So remember we have this timetable arrival. So let's try, if we are going to some other pile here. Let's do like this. I'll go into trips and for example, I want to do this.

I want to have prom connect to API import a s robot [00:07:00] because I want to use that one. So s robot equals a s robot, like this sbo. Equals to this one in this robot dots, for example, time. Yeah, I use this one time table arrival. For example, when I run this one, we get data and it works. Yeah, there's no problems importing from a sibling is no problem.

However, what if I'm inside of, for example, dashboard and I want to get something from trips or I want to get something from connect to API. ~~Okay. From, ~~how will I do it? So if I try to do like this, from ~~backend slash ~~backend dot connect to API import ResRobot for example. And I want to try to print res robot I'll do print res robot like this, dot timetable arrival.

Let's do like this. And if I run this one, you can see there is [00:08:00] an error. ~~It says from backend. ~~It says trace back. Package not, let me clean this one, it's hard to read. Here, module not found error. No module named backend. I'll increase this one. Okay, no module named backend. So how will I do this? If I just do connect to API and I run this one.

No, no module name connect to API. I'm inside of frontend, remember? So look, if we look That I'm in travel planner, so three dots and you can see this is the, this is my folder structure. I have backend, I'm inside of frontend. How can I get to these these modules? What to do is basically like this.

So there's several ways to do it. One way is to use~~ cis pa ~~cys path append, and then you can append different modules from different paths, from different modules. But that is not recommended. [00:09:00] You can also set the Python path that is not the recommended either as this will as both of them is not sustainable when you are growing the project as well as Python path is using absolute paths, which could work if you're using you're using, for example, Docker then Python path is viable.

However, the best way is to use a package so that we're packaging this. And in order to package this, we need to add ~~some ~~some things here. We need to add a file called dunderinit. py. So for each of the folders. We should add this one, ~~blunderinit. ~~py, actually for Python 3. 3 and forward you don't really need this but as I'm [00:10:00] using something called fine packages in setup tools later on, you will see that we actually do need this.

So I'll continue, create ~~blunderinit. ~~py, actually I can copy this one, go into tests, create that one. Utils, create that one. Backend, yes I have that. And also the root. I will put it in. And I will also create a setup. py. So this is ~~a ~~very important so the setup. py, ~~this is ~~this is where you'll put the metadata and the data on on your set when you're installing the package so that you can pip install it.

So you need to have a setup. py and here from setup tools, this is a built in package. So import setup from setup tools, import. find packages [00:11:00] and we'll start with printing what this will give us find packages so when i'm running this one you can see that it finds all these packages it finds frontend explorations it finds tests ~~U ~~utils and backend.

So basically it finds all of this, which has~~ done there in ~~it to pie inside of it. So if I remove this one, for example,

and I run this one, and you can see u utils is not found now. So because it doesn't have in to pie, but I'll put it in. So for consistency, I should also add in explorations even if~~ I~~ I don't use it. And I also put in tests, which when we have unit tests, but these are [00:12:00] not the, ~~these, ~~we don't want the user to be able to import stuff from, right?

So then we need to do something called exclude so we can use fine packages and we can exclude different things. So what I want to do is. Find packages, exclude what do I want to exclude? It's a tuple. So I will exclude everything that has tests, test star. So everything that has test and everything that is called explorations like this.

So if I run this one, you can see that only front end, and back end is found. Okay, great. So then we'll package this backend explorations and frontend so that we can use this when we're importing.

Okay, so in order to package the backend, frontend and utils let's do this. We have [00:13:00] setup, our setup function from setup tools. And here we should have a name for our package. So I will call it travel planner. So this is what you will use when you're pip installing it. So then we'll have a version as well.

I have a, so version number you can choose for example if it's in beta, you don't want to choose 1. 0 yet. ~~But ~~or in development, you maybe ~~have, you ~~choose 0. 0. 0. So it's up to you. Actually ~~I will choose ~~I will choose version ~~1. 0. ~~1. 0. 0. So it doesn't really matter. Just that you, whenever you're doing a new one and you're, Installing it, ~~you can call it version one~~ you can increment the numbers.

~~Yeah, 1. 0. 2. ~~Actually, I could have chosen 0. 0. 1 or something, but ~~let's do that. ~~Let's do like this. It doesn't matter for this lecture, at least. Description. So I will have a description here. ~~So this package is used for travel planning, or actually I can copy it. There's no use for me to type this out.~~

So this package is used for travel [00:14:00] planning in public transport in Sweden. In Sweden, it has back end code, front end code, and utils. So this is Multiline string. Let's continue. Author, it's me, hun. We can continue with author email. ~~Yeah. Type out the email. Just type your email the mail.com.~~

~~So ~~just type in your email. Install. So this is quite important. Install requires. Then you can see what type of packages that your installation is based upon. So for example, mine is based upon pandas of course. Streamlit, because I will use that one for the dashboard. So streamlit. I will also ~~use I will ~~use requests.

I will use requests. Something called folium for the maps. Okay, and then I will continue here that the ~~package ~~[00:15:00] packages to choose. So here I can specify the packages I want, or I can use the fine packages. Say that we have a very ~~large ~~large package here. Then we need to find all the packages or large library.

So fine packages. Exclude. I will choose this one. Basically copy it here. Or I can type it out. Exclude equals to test star comma explorations like this. So this will find the front end, back end, and utils. Okay, basically like this.

To run this one, if I run this one, nothing will happen. Instead, I need to do python, I need to pip install. Let's do that. I'm in travel planner. I'm in the [00:16:00] root. And in the root, we have setup, right? If I do three dot, you can see here. setup. py is in the root. Python. So since it's in the root, we can install it using a UV pip install.

Let's see, what should I install? Uv pip install dash E and dot the dash E is a flag that~~ makes, make~~ makes this editable so that whenever I change something in my scripts, in my modules, then that will be reflected when. When we're importing it. So this is what I want to do.

uvpip install e and dot means from this folder here. So it will look for the setup and it will use this to set up the package. So I'll run this one. And you can see that it has installed a lot of other packages, right? Streamlit and other things. [00:17:00] And so if I do uvp show travel planner, and you can see we found travel planner here.

So Travel Planner version 1. 0. 0, that was what we installed and the location where it is installed in the virtual environment. And the project location is in this folder here. And it requires these packages here. Cool! Let's continue now. For example, what was the problem that I had before?

I will remove all this init first or close them down here. We have dashboard. py. So still I cannot find the connect to API. However, I can now find it using from backend dot connect to API. You see it's found [00:18:00] because if I run this one, we can see, okay. Module not found, no module named backend. How come?

Oh, pie in the, Oh, I was in the wrong. Yeah, I'm in a virtual environment now. So if I run this one, Yeah, it works. Okay. I was in the wrong Python environment. So I was in the global one when I ran this script, but now I'm in the virtual environment where I've installed this one. So that's why this will work, but that is cool.

So for example, if I do Python. Now I can, from backend. connect to API, import ResRobot. Cool, cool. So then I can do ResRobot like this, right? But I can also go into other. For example, let's see, I close this down first to show you. Okay, this would work [00:19:00] anyways because I'm in the root. However, if I go into, for example, utils, and here I can also I can do python, and I can do rom.

For example, here in the dashboard, I can just say variable x equals to By, for example, so from frontend. dashboard import X no module named frontend. Okay. That has to do with, let me. From frontend. Let me close this down. So I'm in utils. Okay, I'm in okay, let's see. Which environment am I in?

So echo virtualenv

Yes, I cannot find it. So I'm in the global [00:20:00] Python environment. And that happens when I run the click the run button. Sometimes it just jump out of my virtual environment. It gives me a new Python environment, which is the global one. And inside the global one frontend is not installed. Okay, that's cool.

So let's activate this. So source dot slash dot bin activate. And now if I do Python. So now I know that my virtual environment is activated. So Python. And then I can do from frontend dot dashboard import x. And I can, yeah, this code also runs. Because, from my dashboard, I'm importing s robot and I'm doing the print right.

So everything also comes in, even if you do a when you're importing from a module, everything will run. That's why if I have print [00:21:00] like this, it will run when I'm doing that. However, I've imported X, right? So I can use X here. So that is quite cool. So I can reach this wherever I am, as long as I have activated my virtual environment.

Because ~~I have installed~~ I have installed my package, my library into my virtual environment. Cool! And you can see that I didn't need to install it again, even though ~~I ~~I put in a new code. So let's close this down and I will go in and put in ~~my real, ~~the real code for the program and you can see it working.

So first of all, dashboard, I will place in some code here. I will ~~play a ~~copy in this code and here I use Let's see I import Streamlit and I take from PlotMaps, import TripMap, and then I create something with TripMap. And [00:22:00] then basically it's a display map, so I'm just displaying ~~what ~~a map of the stations ~~between~~ between Malmö and Umeå, basically.

And I'm using utils. constant, import station IDs. So we don't have these things, right? So I'm importing things from different places. First, from PlotMaps, this would be very simple to just import, even if without installing it would work if you're inside here. If you're inside the frontend. However from utils.

constant wouldn't work. So let's do like this. I will go into PlotMaps. And I will copy in that code as well.

So this code is quite a little bit more advanced. So it's based on an abstract method that I have called maps. And that means that Every map that will inherit from this one has the same interface so that it must [00:23:00] implement this display map method. And that's basically, that's the only thing that ~~this abstract, this map does, ~~maps does.

But then we have tripMaps that is implementing this, that is inheriting from these maps, right? So it has to have this displayMap function or method. So this displayMap method basically just displays the map. And the map is a folium map. I don't need to go into the details on that, but basically it's just putting out all the points where we have so we use the latitude and longitudes, basically.

And then I think this is all except constants. We have to go in there. So in utils. constants, and this is also a little bit new. This is enums. And basically what this does is ~~it's a special type of ~~It's a special type of class that makes it into an enum, which is a collection [00:24:00] of name and value pairs.

So this means ~~it's just, ~~it's for readability and type safety. So basically now you know that when you do station IDs dot ~~malmo, ~~malmo, Then ~~you will get the~~ you will get malmo and then you take dot value and you will get this value here. So it's for type safety and ~~clean and like ~~readability. So basically now we have constants and run dashboard is also interesting.

This one we have to fill as well. So this one is very simple. It's just using subprocesses to ~~run~~ run this ~~I have~~ I don't have the front end path, I see. So I will put in the front end path here. From pathlib import path. And then I will do root, I'll do like this, root path equals to path done the file dot parents of one.

So this is the root [00:25:00] path because parents of zero, I'm in utils, one I'm in packaging. And then I will copy this one. And I will call this ~~front end. ~~Front end. It's parent, it's a root path ~~divided by~~ divided by front end, basically. ~~Front end, ~~just for sake I will take the back end as well.

~~Back end path.~~

Okay, so

basically I just take a front end path so that we are into the front end here, so that I can use this one to go into the dashboard. So my run dashboard, it requires the whole path.[00:26:00] 

So I import front end path. I take the front end path. And put in dashboard. py so that I go into dashboard. py and run it. So basically if I run this one, I click on run button now,

and we can see that there's a Streamlit app going on. Let me take this one out.

There seemed to be an error here. Yeah. Okay. No module name, connect to API in let's see from plot maps, import trip map. Okay. Let's see from plot maps from backend dot trips. Okay. Let's see what they're no module name. Connect to [00:27:00] API from connect to API, import the robot. And this is inside of backend, so it's inside of trips, right?

Yes, I forgot to paste this one in. So go into trips. Okay, so basically this one ~~is~~ is a trip planner class. And this one ~~we put the, ~~we take in ResRobot and we create a ResRobot here. Okay. And then ~~we~~ this one basically picks out the next available trip and there's also next available trips today which is not implemented yet, but it's up for you to implement, but basically this returns ~~a ~~a data frame which can be used later on.

So it contains the trip~~ with~~ with all the longitude and latitudes for all the stops. Thanks. And it gets the names of the stops as well, and also the [00:28:00] times. So now, let's go back to my dashboard. And you can see that this is my dashboard. I've written it in Swedish here, but no matter. You have a map of all the stations.

Can make it bigger. So this is Umeå here. We had, was it from Malmö to Umeå or Umeå to Malmö? We can see here the time 1907 0 1 12 and into Umeå. We have 0 1 13. Okay. 11 25. So more than 12 hours to travel across Sweden. So from Malmö in the most South. into not even the most north, but Umeå is quite north.

So that was quite cool. And you can see this there's a text on station and time [00:29:00] and and the date.

Cool. So that, but can we do it a little bit cooler? Yes, we can, because right now I need to ~~do ~~go into the run dashboard and run it, or I can. Basically go in and ~~do ~~stream it, run in the terminal stream it run, and this dashboard ~~pi. ~~However, I don't want to do that. ~~I want to have, so I close this down, close down the app ~~I want to set up ~~so that I get a command line ~~so that I get something in the command line, like ~~a~~ a command that I can use.

To directly run this dashboard. That is my goal. So I go into setup. py And I can do like this EntryPoints

EntryPoints Equals to let's see, it has to be a dictionary Console Scripts [00:30:00] So what type of console scripts do I want? I want to have this Dashboard is the name that I want to use. So dashboard, if I write dashboard in the terminal, I want this to activate. So what do I want to activate?

I want to activate this ~~U ~~utils.run

dashboard basically. And here in the doc run dashboard, I have run dashboard function, right? So that is all. So ~~if I run this one, ~~if I save this one and I do dashboard and you can see that it doesn't work. Yeah, command not found dashboard. That is because I changed ~~the~~ the setup. py. Then I need to reinstall it.

So let's reinstall it and I can call it 1. 01 and I will do UV [00:31:00] pip install. Or let's see, I'm inside of utils, I need to go up a step. uv pip install dash e dot. Okay, so it reinstalled this package. And if I now write dashboard. ~~Cool. ~~Cool. So you can see, ~~now using, ~~now I have a command line. I can write dashboard to start my dashboard.

Oh, that is super cool. 

Okay. And with this ~~I have~~ we have gone through how to install packages ~~and but I won't, ~~I haven't gone through the code in detail and ~~that is~~ it's a lot of code here ~~and that, that has to do with, ~~this is~~ a~~ beginning of a much larger project. ~~So ~~to show you that you're.

Packaging larger project, and it makes it very simple to import different modules ~~from different ~~when you have packaged it. ~~And ~~this is really useful to learn. [00:32:00] So make sure you learn packaging and ~~your Python ~~your Python skills will elevate. ~~So ~~thank you for watching this video and see you in the next one.

Bye.

