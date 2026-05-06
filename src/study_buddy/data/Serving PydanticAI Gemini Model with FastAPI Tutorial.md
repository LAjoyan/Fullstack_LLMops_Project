# Serving PydanticAI Gemini Model with FastAPI Tutorial

[00:00:00] Hello and welcome to this video where we'll go into ent AI together with Fast API. I will use Fast API to serve a ENT AI model. That will be very cool. And using ent AI, we will. Uh, a Gemini model. Uh, the idea here is that, uh, how do you combine, uh, fast API together with Den ai? Because basically you want to be able to serve your model, otherwise your model will just be, uh, or what whatever project you create with LLM will just be a ~~puck ~~proof of concept that will probably die out and there will be no value out of it.

You need to be able to serve it. And the way to do it is using fast API. Uh, to build a, a, uh, an API, which, uh, a front end afterwards can consume. The front end that use, uh, that, uh, consumes. It could be like streamed it, it could be type I, it could be, uh, JavaScript [00:01:00] front end, such as, uh, view, uh, reacts, felt, uh, could be, uh.

Uh, solid js could also be like, uh, rust lepto, for example. Whatever you choose. Uh, this is really cool. Let's move on directly into the coding part.

**Kokchun Giang-1:** , I'm here in Visual Studio Code and let's set up, UV in it, UV add PI and the dash ai. ~~I need to have let's see. ~~I need to have UV corn to work with fast API and I need fast API UV corn to serve. Let's see, what else do I need? Yeah, I will actually use Duck db, I will have Duck db.

And what else do I need? Let me see. Python dash dnv because we need that. And otherwise Python is included in Python ai. Let's run this one and let's [00:02:00] do something else. We'll do r main pie. 'cause I don't want that. I want to have touch. Let's see. We can have, actually I can do like this, make the SRC source cd, SRC.

And here I will do touch data models, do pi, I need movies, underscore API do pi, I will work with movies and then set up under SCORE DB dots. Pi and util pi. Just a few things that we need here. And also I will do touch dot slash dov. , I have NV here, and starting here we'll have Google and the store API and the score key.

And here basically you save your Google API Key. From Gemini you have Google AI Studio. Google ai. API, Google Gemini [00:03:00] API Key. Let me just show you here. Yes. Here you have Google, Gemini, API Key. And you can click here, get the Gemini API key, and you just follow this link here. You can go into here setting your API key or.

Like here, Google AI Studio, ai, API Keys. Go in here and get your API key and then afterwards you copy it in, in here. But very importantly is that it should be called Google API under score key or Gemini under API under key. ~~I will I will put it ~~I will pass the video and then I will place this one in.

**Kokchun Giang-2:** , let's create this API to work with Gemini or work with p ai. We can actually go ahead and start with say utils. Actually, I want to have a convenience function to work with ddb. Because I want to have [00:04:00] my data, I want to save the data in the database. I'll start there actually.

From Path Lib import path, and here I will have I'll import duck DB as well. And then I will have data path equal the path done, the file parent slash data. I will have a data folder as well. Here I will create a data folder, and here I will place my database. ? And then I will use this data path and I will create a query.

Query Duck db. Here I'll have SKL code string and I will do with duck db do connect. Connect to Duck DB data path [00:05:00] and go into movies db. I'll use movies examples. The idea is that I would want to. Be able to put in text input to generate a movie, and then it will automagically generate a movie that will be placed in the database.

That is the idea. To do that, we can have here s. Con. , We create this connection object and this connection object. We use it to create this cursor and let's see, cursor equals to con dot execute. And here I'll put in SQL code. However it's important that we put in parameters as well.

Parameters equals to parameters. And why [00:06:00] is that? Because the parameters~~ I will use to ~~I will use it ~~for ~~to avoid SQL injection. I'll show you how to do that. If you send in any parameters, then they will be used here. I will use it to avoid a scale injection soon.

Parameters equals to none, by default it's none. But you can put in~~ a parameter ~~different parameters and place it in here together with question marks that you can use in conduct execute for the SKL code. , We have the casa, and then what I want to do is I want to do SQL code.

~~I want to make it to ~~I want to do something like this, if SQL code strip lower, I want to strip that we remove leading and trailing spaces. Lower to make it lowercase. And then I will do dot [00:07:00] starts with. If it starts with some of these commands or some of these words, select from home desk.

Or Pragma. , If it starts with one of these, then we know that we want to return a data frame. Will ~~the ~~return cursor, df, otherwise ~~I won't re ~~I will return none. It returns none by default. This is my simple util function. This query reductive b that will help us. To for as a convenience function, let me do it like this.

No. Yeah. . Starting with this convenience function and then I want to do a setup db. I will go to setup DB and here from you TILs import [00:08:00] query duct db, and then I will do query duct db. And basically here I will put in my SL code, create table, if not exists movies. What do I want the movies to contain?

A title is a good start as a text or string or bar, car. Same thing year as integer. Genre as, let's see, text and we have rating. I will put it into Tiny In. . Because this will be very small numbers. , See my colon. Here I do query duct db. I use this convenience function we can just run it.

Source, we do set up db, ? We do uv run set DB [00:09:00] pi, and you can see it has created a movies DB to check that out. ~~We can do ~~we can do something like tech db data slash movies, detect db, and we can do desk and you can see, yeah, we have the movies here. Titled Year genre rating.

From movies and we should get nothing, ? No rows. Yes. Great Control D to close down the connection. Now we have set up our d DB database. What we want to do now is data models. I want to make sure that. We get our data models correct. From ~~pedantic, normal ~~pedantic, import, base, model and field.

~~And here, ~~and we'll have class movie, this inherit from base model. It's a base model title string [00:10:00] year year as in int. And RA is a string rating is an int and here I'll have a field and greater equals zero, less than equals to six. I want to have a zero one to five. Class will have a prompt as well.

This is also a base model. And here we have prompt as a stream. ~~. Now I have this these are the data models that I have, and based on this, ~~now it's time to create our ~~API. Movies, ~~API. For the movies, API to create an API, it's very simple. You take from fast API import fast, API. ~~.~~

~~And here I will also have my agent. ~~From P ai import agent. Actually, we could also have a setup agent in a separate script, but since it's simple, I will keep it in the ~~API here, ~~API script. , From [00:11:00] d nv, import load dnv. From U utils, import query reductive, B from data models, import, movie, and prompt.

. And then we start with loading in ENV, that we have our ~~Google ~~Google API key available because our agent will require it. ~~We'll have agent. ~~Agent equals agent model equals the Google. Let's see, two point, actually they have three here. Pro preview. Let's try that one. This is new.

I haven't tried it before. Output type. What should output type be? I want it to be my movie, this is my movie model. And here I will do app equals to fast API and what I want to do is app dot get slash ~~movie ~~movies. This will [00:12:00] return all my movies Async Dev. Async is not needed because in fast API, it's async by default.

However async is just. It's quite nice to clearly mark that this is an API endpoint. ? Read movies, colon on movies equals to query duct DB from movies. ~~Yes, you are. ~~You are maybe used to like doing select star from movies. Inducted B, you can just type from movies and it will work as select star from movies, and then return movies dot two picked.

Orient equals to records. , That means we will, the movies, we know it's a data frame. When we return it we will return it will make it [00:13:00] into a dick, and we will have the orient test records. Let's try this out. UV corn. Actually I cannot run uv. I need to run UV corn. Movies, a movies colon app, dash reload. I made a mistake before one that was very costly for me. In terms of time, like I did, I forgot to type in the reload, which make, when I changed the API, I was very frustrated why it didn't make the changes that I wanted to. But I forgot to type in the reload.

It became a lot of messages back and forth to different lms, which couldn't solve my problem, of course. , I'll run this one and I will open up my UV unicorn. Here it is.

I open this one like this, divide into two. Command B. , Detail not found of course, because I don't have anything at [00:14:00] home, but if I do slash movies, we get internal server error because no module name, mpi. , Let's fix that. CTRL C UV add, actually we need pandas because pandas will install NumPy as well.

You add pendas and then UV run UV corn. Let's see, movies, API code on app. Dash reload.

, Now you can see let's see, movies.

~~Let's see. ~~Yeah, it works. You can see it's empty here, if I zoom in a little bit, you can see it's empty. And it's empty because basically we don't have anything here yet. Let's post some data. App.post/movie. Here it means that I will post a movie [00:15:00] here. And we will do async dev. Create movie query.

Prompt

result equals to await. ~~What ~~what am I waiting for? I'm awaiting for my agent run. And here I will do query. The query is the thing that I get in and I do query dot prompt because our prompt has a prompt field which is a string, and then we'll have movie is equal to result dot output. ~~If you are, ~~if you watched my previous video, you will understand what all this does.

Because basically the result is what we get back from the agent. And then afterwards we do result of output to get the output. And now our output ~~is ~~should be [00:16:00] in the form of this, the model. It should be in the form of a movie model or movie. ~~Is the data type. ~~What we want to do now is to take that and ~~query, ~~query reduc db.

Or basically I can show you what I mean I can just return movie and we'll see. , I will go in here slash docs and this is the Swagger ui, and we can go into movie and try to post something. Try it out. Give me a call. Soccer and Kung fu movie. . Hope it'll gimme shoveling soccer.

Let's see. . There is actually an error here, which we can see. Yeah. Gemini three Pro. Yeah. Maybe it's the three tier that it cannot take, but what, I will just change it. Let's see. Dash [00:17:00] 2.5 flash. Yeah, that should be, that should lemme try this one. Execute this one. .

Yeah. Shouting soccer. Nice. Shouting soccer, year 2001. Genre sports comedy, Kung fu. Rating four. Yeah, I would say rating five, but yeah, the LLM things rating four. That is fine for me. Let's you can see we have this dictionary. If we have this dictionary, we can easily just input it, ?

This is quite its structured data we can do query reductive b. However, to make sure that we we put in things that are safe, we can do, we need to, I will do insert into movies and then values. Question mark. Question [00:18:00] mark. . On this comma, comma, not the dot.

. And I will put in my parameters. Parameters are basically parameters. I will have a topple of movie dot title, ? Movie dot, here, movie genre, movie rating. . That is it. And now I will execute this again.

Let's see if we got showing soccer again. Gimme a cool, yeah, show soccer again. , Nice. That means that I've I've now you see I got this details back. And this means that this should put in the data into our DDB database. Let's choose something [00:19:00] else. A space, a futuristic AI movie about a. Robot that pretends to be a human and make the human fall in love. Something like this.

, Let's see what it comes up with. Yeah, I was thinking about her. Title her year 2013 genre sci-fi rating five. . Nice.

Let's do one more. I will be back.

What did it find that Terminator 1984 SCI five rating five. Nice. . Let's go into our get endpoint and try it out, execute, and you can see, ah, this is our response [00:20:00] body. Let us just try out we have this URL here, ? We can just copy this URL. I paste it in here and, ah, this is our data.

Cool. This means that if we can connect this fast API into a front end of our choice. And we could consume this json data without problems and we can, for example, use some kind of ~~J ~~JavaScript front end and consume this and make a really nice UI on this. Super cool that this works.

I will close this down. Control C, and you can see this doesn't work anymore. I will just take a look into my data. If I do duck DB data slash movies, duck db and I do from movies, and you can see this is my database. Now we have populated [00:21:00] it with a few data points and the rating became five after when the second time I ran Strange.

Or not strange. It's fine. I will do Ctrl D to close this down. Make sure that you you're getting ignore your API key or your dot END. And then afterwards you should commit and push this code to your repository

Super cool. In this video we have created a fast API application, very simple one with a post endpoint and a get endpoint. And in the post endpoint you could put the natural language and after that, it will automatically change it ~~to ~~to create a movie based on the movie model, ~~which movie, ~~which is a Pi onic base model.

And after we have created this pedant model. Then it, we could easily put it into our ~~d ~~DB database. [00:22:00] Very cool. And then when we used get endpoint, we were able to read all the data in JSON format. That is. Super cool with this means that you could connect this API to ~~an ~~a front end of your choice and it's possible to build applications where you have this AI model in the background.

I hope that you learned a lot in this video, and thank you. See you in the next one. Bye.

