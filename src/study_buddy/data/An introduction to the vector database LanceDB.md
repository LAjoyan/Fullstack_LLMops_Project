An Introduction to the Vector Database LanceDB

Hello and welcome to this video where we'll go into LanceDB and the fundamentals of it. LanceDB is an open-source vector database designed to handle large-scale vector data efficiently. It provides a robust platform for storing, indexing, and querying high-dimensional vectors, which is very good for working with, for example, LLMs and RAG applications.

RAGs are Retrieval-Augmented Generation. Whenever you want to chat with your data or chat with your documentation, you provide a query, a prompt, or a piece of text, which is then transformed into vectors. This vector is compared to all the other chunks or all the other documents in your database.

You find the one that is closest to it semantically based on vector search. In LanceDB we will also go into vector search, full-text search, and hybrid search, where you can combine both full-text search and vector search to make it very powerful.

But before that, we will go into just working with LanceDB and getting started with LanceDB to navigate around it. How does it work with creating a table? How are the tables stored? How can we add data? How can we create schemas, etc.? And what are the formats of the data?

These are some fundamental things that you should know about LanceDB before you jump into RAG applications. In many other tutorials I see, when it comes to LLMs and RAGs and agents, they jump directly into a proof of concept without covering the basic knowledge of all the other components.

Here I want to cover the fundamentals of LanceDB before we jump into RAG applications, which will come in later videos.

Let's get into Visual Studio Code now directly.

Here I am in Visual Studio Code and you can see there are two data files here, or two JSON files. Here I have animals_text_embeddings.json and here this is basically JSON data. You can see there's text and there's vector. And here I have jokes.json, where I only have the text.

These I will come back to later on, and I will just say that these are available in my repository, which I link in the description.

This is generated fake data that I use as examples. I used ChatGPT to generate it.

Let us start with a terminal now, and I will do touch lance_db_basics.ipynb.

I will create this LanceDB Jupyter notebook that I will use.

I will start with creating a virtual environment using uv init.

And here I initialized an environment. I don't need that main.py, so then I will do uv add ipykernel lancedb.

And if I need something else, I will install it on the way.

Let's move on to lance_db_basics.ipynb.

Let's start with a markdown:

LanceDB — A vector database for LLM applications.

That is fine.

I'll change my environment to this LanceDB demo, and here I will change to Python.

Import LanceDB.

Then I will do:

db = lancedb.connect(uri="vector_database")

What do I want to connect to? I want to connect to my vector database. The URI is the path of the database.

You can see it takes a little bit of time the first time because of some caching, but now it's done.

You can see this is the wrapper for the LanceDB connection.

You can see this vector_database here. It's an empty folder. Yes, that is expected.

I will show you how to work with this one.

Save this one and then do db.uri.

You can see this is the URI. Yes, that is what we expected.

Let's start with creating a table.

Basically, we have our database connection, right? db is connecting to this folder where our LanceDB database should be.

Before we create the table, we actually need to import some data.

Import JSON.

Then:

with open "data/animals_text_embeddings.json" in read mode as file.

Remember that embeddings basically mean the vector representation of the text. That's why we have text and vector here.

Now we have vectors in three dimensions, but it could just as easily be 3000 dimensions or 4000 dimensions depending on which embedding model you use.

Now if we take a look at the data, you can see it's a list of dictionaries.

As a list of dictionaries, we can put it directly into our table.

table_animals = db.create_table("animals_text", exist_ok=True, data=data)

This makes it idempotent. If I run it several times, we'll get the same result. If it already exists, it won't create another table.

The table looks like this now.

Take a look into the vector database now.

You can see there are a few things here:

animals_text.lance

This is quite interesting. All the tables will have this .lance suffix.

Inside each table we have _transactions, _versions, and data.

The data is stored as .lance files.

Whenever you're adding more data, you will get more transactions and newer versions.

If I run this again, nothing happens because we used exist_ok=True.

If I remove that, we get a ValueError saying that the table already exists.

You can also use mode="overwrite".

Then it creates version 2, version 3, etc.

Basically, all the history is stored inside this Lance table.

That is very good to know.

Now if we take a look at table_animals.head(), you can see this is a PyArrow table.

PyArrow is the underlying file format for storing data in LanceDB.

It's memory-efficient and very fast to work with.

I will make videos about how to work with PyArrow in the future.

We can also do table_animals.to_pandas().

If pandas is not installed, use uv add pandas.

Now it works.

You can see we have six data points.

This is a normal pandas DataFrame that you can work with.

Let us create some more data to see what will happen.

We add more data to the table.

You can see:

AddResult(version=3)

Now we have more versions, more transactions, and more .lance files.

Now there are eight rows.

We're storing text and vectors.

It is suitable if you already have vector representations together with your text.

But later on I will show you how to generate embeddings automatically from just text.

Let's create an empty table.

You cannot create a completely empty table without at least a schema.

Schemas can be defined in two ways:

PyArrow schema or LanceModel.

We will use LanceModel.

A LanceModel is basically a Pydantic model that can be converted into a LanceDB table.

Let's create a schema:

class JokeSchema(LanceModel):

joke: str

rating: int

Then create the table.

Now we have a new table called jokes.lance.

The schema is stored there even though we haven't inserted any data yet.

We can check existing tables and also delete tables.

If you already have tables, you may want to open an existing table.

Now we come to a very cool thing: vector search in LanceDB.

LanceDB uses Approximate Nearest Neighbors, ANN, for vector searching.

You can either search directly with vectors or search with text and let embeddings be generated automatically.

Let's start with vectors.

We create a query vector.

Then we search and limit the results.

We get the closest matches based on Euclidean distance.

Now let's use the embeddings API.

The idea is:

Put in text, automatically generate embeddings, and search semantically.

We import get_registry from LanceDB embeddings.

Then create a Gemini embedding model.

Now we can generate embeddings.

If Google Gemini isn't installed, install google-generativeai.

You also need a Google API key in your .env file.

Now embeddings work.

The embedding dimension is 3072.

Now let's create a schema with automatic embeddings.

The text field automatically generates embeddings.

If you provide vectors manually, those will be used instead.

Now we create the table and load joke data from jokes.json.

Convert it to a pandas DataFrame and rename the column.

Now we add data.

The vector embeddings are automatically created.

That is really cool.

Now it's time to do some searching.

We search for “data engineering jokes”.

You can see the top jokes are related to data engineering.

We can also search for C# jokes and chemistry jokes.

These are vector searches.

The query is converted into a vector and compared against all vectors in the database.

Now let's go into hybrid search.

Hybrid search combines keyword-based search using BM25 and vector similarity search.

Keyword-based search is better for exact matches.

Vector search is better for semantic similarity.

Hybrid search combines both.

To enable full-text search, create a full-text search index.

Then import RRFReranker.

Now perform hybrid search.

The ranking becomes slightly different because both vector similarity and keyword relevance are considered.

Some rules of thumb:

Exact matching → Full-text search.

Meaning-based matching → Vector search.

Mixed or unpredictable queries → Hybrid search.

The best approach depends on your dataset and testing.

AI engineering involves a lot of experimentation and evaluation.

If you're using Git and GitHub, you should not push the vector database or secrets.

In .gitignore include:

.env

vector_database/

In this video we have gone through LanceDB from the basics up to vector search, full-text search, and hybrid search.

We covered creating tables, adding data, schemas, LanceModel, embeddings, vector search, automatic embeddings, and hybrid search.

I hope that gradually you built a basic understanding of LanceDB and its vector capabilities, which are very useful for applications such as RAGs — Retrieval-Augmented Generation — where you can chat with your own data and documentation.

That is really cool.

I hope I will see you in the next video where we continue building RAG systems.

Thank you for watching this video.

See you in the next one. Bye.