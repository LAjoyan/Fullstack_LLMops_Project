# Serving PydanticAI Gemini Model with FastAPI Tutorial

Hello and welcome to this video where we'll go into PydanticAI together with FastAPI. I will use FastAPI to serve a PydanticAI model. That will be very cool. And using PydanticAI, we will use a Gemini model.

The idea here is that, how do you combine FastAPI together with PydanticAI? Because basically you want to be able to serve your model, otherwise your model or whatever project you create with LLMs will just be a proof of concept that will probably die out and there will be no value out of it.

You need to be able to serve it. And the way to do it is using FastAPI to build an API, which a frontend afterwards can consume. The frontend that consumes it could be like Streamlit, it could be Taipy, it could be a JavaScript frontend such as Vue, React, Svelte, SolidJS, or even Rust Leptos for example. Whatever you choose.

This is really cool. Let's move on directly into the coding part.

I'm here in Visual Studio Code and let's set up:

UV init

uv add pydantic-ai

I need to have uvicorn to work with FastAPI and I need FastAPI. Uvicorn is used to serve it. Let's see, what else do I need? Yeah, I will actually use DuckDB, so I will have DuckDB.

And what else do I need? Let me see. python-dotenv because we need that. Otherwise Python is included in PydanticAI.

Let's run this one and let's do something else. We'll do rm main.py because I don't want that. I want to have:

mkdir src

cd src

And here I will do:

touch data_models.py

I need movies_api.py, setup_db.py and util.py. Just a few things that we need here.

And also I will do:

touch ../.env

I have .env here, and starting here we'll have:

GOOGLE_API_KEY=

And here basically you save your Google API key from Gemini. You have Google AI Studio.

Google Gemini API key.

Let me just show you here. Yes, here you have Google Gemini API key. And you can click here, “Get the Gemini API key”, and you just follow this link here.

You can go into settings, your API keys, or like here, Google AI Studio API keys. Go in here and get your API key and then afterwards you copy it in here.

But very importantly, it should be called GOOGLE_API_KEY or GEMINI_API_KEY.

I will pause the video and then I will place this one in.

Let's create this API to work with Gemini or work with PydanticAI.

We can actually go ahead and start with utils. Actually, I want to have a convenience function to work with DuckDB because I want to save the data in the database.

I'll start there actually.

From pathlib import Path

and here I will import duckdb as well.

And then I will have:

data_path = Path(**file**).parent / "data"

I will have a data folder as well. Here I will create a data folder, and here I will place my database.

And then I will use this data_path and I will create a query:

query_duckdb

Here I'll have sql_code: str

and I will do:

with duckdb.connect()

Connect to DuckDB data_path and go into movies.db.

I'll use movies examples. The idea is that I would want to be able to put in text input to generate a movie, and then it will automagically generate a movie that will be placed in the database.

That is the idea.

To do that, we can have here:

con

We create this connection object and this connection object we use to create this cursor.

And let's see:

cursor = con.execute()

And here I'll put in SQL code.

However it's important that we put in parameters as well.

parameters=parameters

And why is that? Because the parameters I will use to avoid SQL injection. I'll show you how to do that.

If you send in any parameters, then they will be used here.

parameters=None by default. But you can put in different parameters and place them in here together with question marks that you can use in con.execute for the SQL code.

We have the cursor, and then what I want to do is:

if sql_code.strip().lower().startswith()

I want to strip so that we remove leading and trailing spaces. Lower to make it lowercase.

And then I will do:

.startswith()

If it starts with some of these commands or some of these words:

select, from, describe, pragma

If it starts with one of these, then we know that we want to return a dataframe.

We'll return cursor.df()

Otherwise I will return None.

This is my simple util function, this query_duckdb that will help us as a convenience function.

Starting with this convenience function and then I want to do a setup_db.

I will go to setup_db and here:

from utils import query_duckdb

and then I will do:

query_duckdb()

And basically here I will put in my SQL code:

CREATE TABLE IF NOT EXISTS movies

What do I want the movies to contain?

A title is a good start as text or string or varchar, same thing.

year as integer

genre as text

and we have rating.

I will put it into tinyint because this will be very small numbers.

See my colon?

Here I do query_duckdb.

I use this convenience function.

We can just run it.

We do:

uv run setup_db.py

and you can see it has created a movies.db.

To check that out we can do:

duckdb data/movies.db

and we can do:

describe movies

and you can see, yeah, we have the movies here.

title, year, genre, rating

from movies

and we should get nothing.

No rows.

Yes. Great.

Ctrl+D to close down the connection.

Now we have set up our DuckDB database.

What we want to do now is data models.

I want to make sure that we get our data models correct.

from pydantic import BaseModel, Field

And here we'll have:

class Movie

this inherits from BaseModel.

title: str

year: int

genre: str

rating: int

and here I'll have:

Field(ge=0, le=5)

I want to have 0 to 5.

We will have a Prompt as well.

This is also a BaseModel.

And here we have:

prompt: str

Now these are the data models that I have, and based on this, now it's time to create our API.

movies_api.py

For the movies API, to create an API it's very simple.

You take:

from fastapi import FastAPI

And here I will also have my agent.

from pydantic_ai import Agent

Actually, we could also have a setup_agent in a separate script, but since it's simple, I will keep it in the API script.

from dotenv import load_dotenv

from utils import query_duckdb

from data_models import Movie, Prompt

And then we start with loading in .env so that we have our Google API key available because our agent will require it.

We'll have:

agent = Agent()

model="google-gla:gemini-2.5-pro-preview"

Let's try that one. This is new. I haven't tried it before.

output_type

What should output_type be?

I want it to be my Movie. This is my Movie model.

And here I will do:

app = FastAPI()

And what I want to do is:

@app.get("/movies")

This will return all my movies.

async def read_movies():

movies = query_duckdb("from movies")

You are maybe used to doing:

select * from movies

In DuckDB, you can just type:

from movies

and it will work as:

select * from movies

and then return:

movies.to_dict(orient="records")

That means the movies, we know it's a dataframe.

When we return it, we will make it into a dict and we will have the orient set to records.

Let's try this out.

uvicorn movies_api:app --reload

I made a mistake before, one that was very costly for me in terms of time.

I forgot to type in the reload, which means when I changed the API, I was very frustrated why it didn't make the changes that I wanted to.

But I forgot to type in the reload.

It became a lot of messages back and forth to different LLMs, which couldn't solve my problem, of course.

I'll run this one and I will open up my localhost.

Here it is.

I open this one like this, divide into two.

Cmd+B.

Detail not found of course, because I don't have anything at home, but if I do:

/movies

we get internal server error because:

No module named numpy.

Let's fix that.

Ctrl+C

uv add pandas

because pandas will install NumPy as well.

Then:

uv run uvicorn movies_api:app --reload

Now you can see.

Let's see:

/movies

Yeah, it works.

You can see it's empty here.

And it's empty because basically we don't have anything here yet.

Let's post some data.

@app.post("/movie")

Here it means that I will post a movie here.

And we will do:

async def create_movie(query: Prompt)

result = await agent.run()

What am I waiting for?

I'm awaiting my agent.run.

And here I will do:

query.prompt

because our Prompt has a prompt field which is a string.

And then we'll have:

movie = result.output

If you watched my previous video, you will understand what all this does.

Because basically the result is what we get back from the agent.

And then afterwards we do result.output to get the output.

And now our output should be in the form of this model.

It should be in the form of a Movie model.

What we want to do now is to take that and query_duckdb.

Or basically I can show you what I mean.

I can just return movie and we'll see.

I will go in here:

/docs

and this is the Swagger UI.

And we can go into movie and try to post something.

Try it out.

“Give me a cool soccer and kung fu movie.”

Hope it'll give me Shaolin Soccer.

Let's see.

There is actually an error here, which we can see.

Yeah, Gemini 3 Pro.

Maybe it's the preview that it cannot take.

I will just change it.

Let's see:

gemini-2.5-flash

Yeah, that should be it.

Let me try this one.

Execute this one.

Yeah, Shaolin Soccer.

Nice.

Shaolin Soccer, year 2001.

Genre: sports comedy kung fu.

Rating: 4.

Yeah, I would say rating 5, but yeah, the LLM thinks rating 4.

That is fine for me.

You can see we have this dictionary.

If we have this dictionary, we can easily just input it.

This is quite structured data.

We can do:

query_duckdb()

However, to make sure that we put in things that are safe, we need to:

INSERT INTO movies VALUES (?, ?, ?, ?)

And I will put in my parameters.

Parameters are basically:

parameters = (
movie.title,
movie.year,
movie.genre,
movie.rating
)

That is it.

And now I will execute this again.

Let's see if we got Shaolin Soccer again.

“Give me a cool soccer and kung fu movie.”

Yeah, Shaolin Soccer again.

Nice.

That means that now you see I got this details back.

And this means that this should put in the data into our DuckDB database.

Let's choose something else.

“A futuristic AI movie about a robot that pretends to be a human and makes the human fall in love.”

Something like this.

Let's see what it comes up with.

Yeah, I was thinking about Her.

Title: Her

Year: 2013

Genre: sci-fi

Rating: 5

Nice.

Let's do one more.

I will be back.

What did it find?

Terminator.

1984.

Sci-fi.

Rating 5.

Nice.

Let's go into our GET endpoint and try it out.

Execute.

And you can see, ah, this is our response body.

Let us just try out.

We have this URL here.

We can just copy this URL.

I paste it in here and ah, this is our data.

Cool.

This means that if we can connect this FastAPI into a frontend of our choice, then we could consume this JSON data without problems.

And we can for example use some kind of JavaScript frontend and consume this and make a really nice UI on this.

Super cool that this works.

I will close this down.

Ctrl+C.

And you can see this doesn't work anymore.

I will just take a look into my data.

If I do:

duckdb data/movies.db

and I do:

from movies

you can see this is my database now.

We have populated it with a few data points.

And the rating became 5 after the second time I ran it.

Strange.

Or not strange. It's fine.

I will do Ctrl+D to close this down.

Make sure that you gitignore your API key or your .env.

And then afterwards you should commit and push this code to your repository.

Super cool.

In this video we have created a FastAPI application, a very simple one with a POST endpoint and a GET endpoint.

And in the POST endpoint you could put natural language and after that it will automatically create a movie based on the movie model, which is a Pydantic BaseModel.

And after we have created this Pydantic model, then we could easily put it into our DuckDB database.

Very cool.

And then when we used the GET endpoint, we were able to read all the data in JSON format.

That is super cool because this means that you could connect this API to a frontend of your choice and it's possible to build applications where you have this AI model in the background.

I hope that you learned a lot in this video, and thank you.

See you in the next one.

Bye.
