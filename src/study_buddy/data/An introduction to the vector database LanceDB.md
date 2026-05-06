# An introduction to the vector database LanceDB

[00:00:00] Hello and welcome to this video where we'll go into Lance db, the fundamentals of it. Lance Db is an open source vector database designed to handle large scale ~~data, ~~vector data efficiently. It provides a robust platform for storing, indexing and querying high dimensional vector. Which is very good for working with for example, LLMs and rag applications.

Rags are retrieval, augmented generation. ~~When, ~~whenever you want to chat with your data or chat with your documentation you are providing a query, ~~right? ~~A prompt or a query, a text which is then transformed into vectors. And this vector is compared. To all the other chunks or all the other documents in your database.

And ~~you take a, ~~you find the one that is closest to it, semantically based on vector search. And in LTB we will also go into both Vector search ~~will go into ~~full text search and also [00:01:00] hybrid search. That you can combine both full text ~~search and. ~~And vector search to make it very powerful.

But before that we will go into just working with Lens DB and getting started with Lens DB to ~~see ~~navigate around it. How does it work with creating a table? How are the table stored? How can we add data? How can we create schema, et cetera. And what are the formats of the data? These are some fundamental things that you should know about Lands DB before you jump into rag applications, ~~such as in, ~~in many other tutorials. I see when it comes to LLM and rags and agents, they jump directly into a proof of concept without covering the basic knowledge of all the other components.

Here I want to cover the fundamentals of lens DB before we jump into. Rag applications which will come in later videos. ~~Let's stay, say, ~~let's get into visual Studio Code now directly.

**Kokchun Giang-2:** here I [00:02:00] am in Visual Studio Code and you can see there's two data I have here or two JS files. Here I have animals, text do and text embeddings Do Jason. And here, this is basically JS data. And you can see there's text and there's vector. And here I have jokes that Jason, where I only have the text. These I will come back to later on and I will just say that these are available in my repository, which I link in the description.

~~Of course. ~~And this is what I use for I have taken this from chat chat GPT ~~to ~~to generate this fake, generate this fake data that I can use this as examples. Let us start with a terminal now, and I will do touch lance db basics. I pin B. , I will. Create this l db Jupiter notebook that I will use and I will start with in [00:03:00] creating a virtual environment, UV in it.

**Kokchun Giang-3:** and here I initialized an environment of the r main dot pi since I don't need that one. And then all the UV add I PI kernel. And what do I need? Launch db. And if I need something else, I will install it on the way. , let's move on to ~~Lance DB basics IB. , let's start with a markdown.~~

Lance db. A vector database. Yeah. Four LM application. That is fine. I'll change my environment to this lens DB demo and here I will change to Python. , ~~let's start with I will actually have this on the side like this. . ~~Import Lance db. . I will decrease this one. Import LAN db and then I will do DB equals to LAN db dot connect. And what do I want to connect? I want to connect to my vector database. I will do URI. This is the path where I will put the string or path and the URI of the database.

What do I want to connect on? I [00:04:00] want to connect to something called vector underscore database. I call this vector database. Db, you can see it is basically , first time it takes a little bit of time because of some c caching, but now it's done. You can see this is the wrapper lands DB connection, URI equals to this path.

Into this vector database. You can see this vector database here. It's an empty folder. Yes, that is expected. I will show you a little bit ~~how what ~~how to work with this one. Save this one and then do db ui. And you can see this is the URI. Yes, that is what we expected. , let's start with creating a table.

Basically. I will move this down and I will do it like this. Create a table. Now we have our db, right? DB is connecting to this folder here where our lens DB should be. DB you can [00:05:00] see this is the lens DB connection. , let us create a table and before we create the table, we actually need, we'll import some data, import json and we'll do with open, I will do data slash animals.

Let's see. Let's go see here. Animals text embeddings. Jason, remember that embeddings means that it's basically just the vector representation of the text, the text of each. That's why we have like text here and each and the vector text vector. Now we have vectors in three dimensions, but it could as easily be.

3000 dimensions, for example, or 4,000 depending on which embeddings model you use. , data slash animals text embeddings Jason. And then I want to have the mode of [00:06:00] read as file. ? I am opening this this file here. And what do I want to do? Data equals to json loads and file read basically.

. And then I can ~~get ~~take a look into data. You can see it's a dictionary here or ~~it's a list of dictionary. ~~It's a list of dictionary. And as a list of dictionary, we can just put it into our table directly or we can create a table and put it inside. Table animals equals to db. Do create table animals underscore text.

I'll call it that. Call. And will do exist. . Equals true. This makes it item potent. If I run it several times, we'll get the same results. Because if it already exists, ~~it won't ~~it won't create another table. Instead, it'll just create a table if it doesn't exist. , ~~data equals the data.~~

This is what [00:07:00] I loaded in. Table animals looks like this now. , this is~~ the wrapper for then ~~the wrapper for table animals. Lands, table name, animals, text, version one. , take a look into the vector database. Now we can see there's a few things here. If I go into CD into, or I can actually do three Vector database, and you can see the vector database looks like this.

We have animals, text lands. ~~, Lands, ~~this is quite interesting. All the tables will have this suffix lands and inside of each tables we have underscore transactions. We have underscore versions and we have the data. The data is also, it's a dot lens file. And here versions is one dot manifest.

? And here, transactions is zero. This is a transaction it's just a transaction. Whenever you're adding more data, you will get more transactions, you will get a newer version, et cetera. [00:08:00] Let's try to ~~do that. But we will ~~do that. If we run this again, you can see that if I run this one again, we can see nothing like nothing has happened because~~ the thing is that ~~it didn't do anything when I did exist.

? . If I copy this one. And instead of exist. , And I'll run this one and you can see there's an error, a value error ~~I can do. ~~The value error is that table animals text already exists, we cannot create it again. . And also you can change something called mode equals to overwrite. If I do this one now, you can see it's inversion two, and if I run this again ~~three, ~~you can see there's transaction zero one.

~~One, ~~two. And we have ~~two, ~~two lands files here. Basically we have all the history ~~is ~~stored inside of this animals lands table. Basically here you [00:09:00] can see there are transactions and versions and data all. All these are stored the history is stored. That is very good to know. Override basically is just, I'm overriding the old data.

Basically if you take a look at the table, animals now dot head to see the data. I will remove the terminal. And you can see this is same as our, this is I'll show you the whole data to see that we don't have duplicates, but here is the PI arrow table. . Pi Arrow, it's a file format which have some metadata and it has some data.

And this is stored in a very memory efficient way. And all, it's very fast to work with. ~~The, ~~you should know that the ~~pi table, ~~pi arrow table is the underlying, file ~~the ~~format for storing the data in Lens db, ~~Pi Arrow table. And I sh ~~I will make videos about how to work with Py Arrow.

~~That is in my, ~~in the future. ~~I will do that. ~~But if you are not familiar with Pi Arrow. That is fine. ~~But then know that you ~~just ~~should ~~know that this is the underlying format and we will work with it~~ as, ~~[00:10:00] as well, that it's good to know, ~~but I won't, ~~I will make a video about that in the future.

We can also do something like this. Table animals, ~~two ~~pandas that you can see a mod not found. Then we need to install ~~Pandas uv, add ~~pandas. , I've added Pendas and run this again, and now it should work. Yes. It takes a little bit time, first time, and as you can see, there isn't copies of the data because basically ~~I over, ~~I overwrote them before, we have six data points, which we had here as well.

We had six. , it looks like this. We have text and we have vector. . This is a normal pandas data frame that you can work with. You can filter it, you can do whatever you want with it, as you could have done in pandas. I assume that you already know Pandas. If you don't know, I have a lot of videos about pandas, you can take a look into that.

Let us create some more data to see what will happen. More data [00:11:00] equals to here. I'll just copy from my notes. You can also take from my notes since it's, I don't want to type it out. Here we can do table animals, add more data, and you can see, ~~ooh, ~~add result version equals three. . Let's see what will happen now.

I'll take out my terminal and I will clear it. Con command K. And then I will do three again, three vector data. You can see there are free, now free versions, many free manifest. We have data, we have free lens data, and here we have transactions. We have come to two here. , And you can take a look into this one.

It reflects here. , now we can take a look into table animals dot two pandas. And here you can see, ah, there are eight points. Now we had six points before. Right now we have eight points, or I will call it [00:12:00] rows, basically. I'm talking about points when it comes to vectors, but basically it's rows here.

~~This is ~~we're storing text and vector. ~~It, ~~it is quite suitable if you have some kind of vector representation already with your text, right? But later on we'll show you that it's maybe more practical that you just put in the text because you may not have the vector representation of it.

I'll show you how to generate the vector embeddings based on just text. But first we should go into some more operations. We'll try to create an empty table and then delete it because I believe it's very important that you understand the tool before you actually go into, you need to understand how to work with Lens DB that you are comfortable with it and not just be able to copy and paste some tutorial and think like it works, but then you don't know how to apply to your own project.

, To create an empty table, you [00:13:00] cannot just create a table that is empty because an empty table do need to have at least a schema. Either you put in some data or you put in some schema, and the schema can be defined in two different ways. One way is to use pie arrow schema, but I don't assume that high arrow.

I will do use the other way, which is to use a lens model. And the lens model is basically a edan model. Since I have done some videos on edan before, then you should know what gigantic model is. This depends on a EDAN model. What we should do is from Lance db dot den import land model. , what is a land model?

A lens model I take a look into here, it's a gigantic model base class that can be constructed to a Lance DB table. That is very important. It's not [00:14:00] just. A Edan model. It's a edan model that can be converted to a lance DB table. ? Then we do like this. I will create joke schema and my joke schema will have Lance it it inherits from Lance model and since it's inheriting from Lance model and it's a edan model, right?

And you know how to create a edan model. Basically, you have. Fields and you have type ins, right? We do joke, it's a string and we'll do rating. It's an int this is a joke schema. Then we can do db. Create table name. Aim equals to jokes. This is the jokes table. Schema equals to jokes, schema.

And we can do exist. . Equals to true. It becomes item potent. You can see the db, [00:15:00] it's still the Lands DB connection, and you can see something happened to the left. You can take a look into Vector database. We have animals text dot LANs, but we also have jokes dot lands. And here we don't have data, but they have transactions and they have versions.

? We cannot take a look into this, but the thing is. Now the schema is stored there, whenever you add data, you need to follow this existing schema. But I won't do that. Instead, I will do DB table. I showed you before how to add data you know how to do that. Table names, we take a look, we have animals, text and jokes.

. Then we can do db drop table jokes. , we drop this table. And we can see db table names. Now we only have, it's a method, we need to have callable. We have only animals text now. , Great. Now we have created a table and we have deleted [00:16:00] a table. ~~Let's ~~if you already have some tables, you may want to open a table, open existing table.

And to do that we do db.open table, and we can do that. Animals just take a look that now we only have the animals, right? If you only have one folder vs. Code collapses it ~~into ~~this way. If you have one folder inside another folder. Yes. And now we can ~~do ~~just open this table. Animals text.

And you can see we have opened this one and I can do dot head and you can see we're in version three as we saw before. . But here dot head, you can see there's five data point in dot head. But we can take a look into two data points if we wanted to. Here a small brown dog running it hat resting quietly on the sofa.

. Cool. Cool. Now we come to very cool thing vector search in [00:17:00] LANs db. . Vector search in LANs DB works in the way that it uses ~~a and n ~~approximate nearest neighbors for searching for vectors. We can search with vector directly ~~if we have ~~if we have the vector embedding. And which you can do, you can use embeddings model to embed your.

Text and then you can search with it, or you can just send in text and then it will generate an embedding for you. And it'll find the closest matches. That is even cooler, but we will start with the first approach. Just take a look into the table. Table animals dot~~ head not ~~head. I will.to pandas.

, now you can see this is all the data that we have. We have eight points here. And let's do, here, let's create a query vector. Just something ~~I ~~I think with query vector equals to 0.5. Point [00:18:00] two 0.9. . If you take a look into this, you should maybe be able to find the closest distance.

I can see, like maybe a panda eating bamboo peacefully. Here we have 0.5 1.37, 0.82. Yeah, it could be this one, I think. Yeah, if I just eyeball this I think it's this one. That should be the closest one. Take a look into now table. Animals search. We'll put in our query vector. Basically some the idea is that in later on is that someone put in a query searching for something, and then it'll be transformed into a vector.

And the corresponding vector is used for the searching. Here we have search for this query vector and we can say dot limit. Three. Top three results, two pandas. And we can take a look. Yeah. A panda eating bamboo [00:19:00] peacefully was the one that was closest as we saw, and it calculates the distance from it.

And this is the Euclidean distance. According to the documentation I have actually not just computed it ~~and take and ~~and double checked, but probably it's true. This is the distance from this vector to all other vectors, and then it's sorted ~~with the. ~~In ascending order. The minimum distance first, right?

, now let's use embedding API. ~~Embeddings API. Now we want, ~~the idea now is that we ~~want to. Idea ~~want to put in text and it will automagically generate vector embeddings. Then another idea is that we ~~put in a query. ~~Put in a query, and it will automagically generate vector embeddings. [00:20:00] And then it will calculate closest distances.

That is the idea ~~with ~~with this, the embedding API, there are several ways to do this, but in the documentation you will see that you can register different APIs. We'll show you from Lens DB dot. Tic import lands model. Actually, I already done that, but I didn't need to do it again.

But just to show you here and Vector, I need these two from pedantic. These are different fields from ~~P ~~Pedantics to use. From plans, db dot embeddings, I want to import. Get registry. , model equals to get registry dot get here I use Gemini, I took a look [00:21:00] into documentation and it's called gemini dash text dot Create.

And the name equals to which model? Whichever model you're using from Gemini, I use embedding dash 0 0 1. And now you can take a look into model. It looks like this. This one get registry dot, get Gemini text create. It basically creates an instance of this Gemini text. You have Gemini text here you can see max retry seven model name Gemini embedding dash 0 0 1, et cetera.

With this model, you can do like this, you can do model dots generate embeddings, for example. And you can say hello please install Google Dash generative ai. , Let's do that. UV add Google dash generative ai. . Yes, I did [00:22:00] that and now this should work. Ah, could not find API key for Google.

Yeah. . Then you need to have create a dot nv and you need to do Google a Pcore key equals, and you put in your API key. If you don't know how to put in, find the API key for Google Gemini. Take a look into my previous video where I have done that and when in my Gemini video, I show you how to do that.

I will just paste in my API key.

**Kokchun Giang-4:** . I did that and it worked. So now you can I also restarted and ran the whole notebook again. You can see now it says model that generate embeddings. Hello? And it works. I got some embeddings. Let's just call this hello. Embedding for example. And I will also do like this import MPI as nmp.

I got MPI from [00:23:00] when I installed Pandas, np dot array. 'cause I want to take a look into this shape here. Then I will do hello embedding shape. . And you can see it says five 3072. We know that the dimension is 3072. ? But you may see in the documentation something in similar to I will show you here.

I will create and now I will create a joke model. Class, this is the new joke model. Or joke schema and joke model. It's inheriting from Lance's model and I will use joke. It's a string and model dot source field. What is this? It marks a text as input to embedding function, which means that if you just put in text and you have this as well, you have vector [00:24:00] vector of.

3072 equals to model vector field. What it does here is that the vector is the destination of the computed embedding. The text which you put in, into source field it will automatically generate a vector embedding.

**Kokchun Giang-5:** the vector embedding is created automatically if you just input a joke and you don't put in a vector, but if you put in a vector, then ~~it will ~~it will use that input instead. ~~This is for ~~if you just put in a lot of joke text, then it will automatically create a lot of vector embeddings for you.

That is quite cool. And also whenever you put in a query vector, it'll also automatically ~~put in ~~create ~~a ~~an embedding for you based on. Model, right? This is the embedding function which you defined before. It's this embedding function that we used. And one more thing is that in the documentation you would see [00:25:00] something ~~style of ~~this model ~~do ~~end.

However, if you note our model ends, if I just put it here, this method, you can see 768. It's not corresponding to the actual. Shape, the actual size is 3000. 72 is many dimensions that we have, this is probably like it's~~ point ~~still something that is pointing towards an old documentation, an old model, that it has 7, 6, 8 while.

The newer one has 3072. Maybe they haven't changed it. ~~What the, ~~what you should do here is instead to either just put it in hard coded like this, or you could just take out an example embedding and then take the shape ~~and you could take the shape of one ~~and you would get the same results.

But I would hard code it. It doesn't matter. , I have this joke model now. And what I should do is that I will do table jokes. I'll create a new [00:26:00] jo. You can see now I only have the animals table. I will create the new jokes table, DB that create table, and I will call this jokes and I will do schema is the joke model.

This is my pedantic ~~schema, which which is or a lance model ~~schema, which is able to convert into a table, right? Remember I said that about ~~the ~~the LAN model, ~~? And exist, . Equals two. ~~It's item potent. Table jokes, as you can see. Now we have. Connected to this lands DB Demo Vector database.

If you take a look into Vector database, now we have jokes LANs as well, and here we have transactions and versions. We haven't put in any data yet, right? Let's add some data. I will do for example we tried to add the JSON data before and it worked a list of, list of dictionaries, but now I will send in the pandas data frame to see that it's also working.

, with [00:27:00] open let's see. Data slash jokes. Jason read as file and then I will do jokes. Data equals to Jason nodes. File read. . And then we have jokes, data that looks like this. . We have a dictionary here. Then we could basically just put it into a pandas data frame probably.

PD data frame jokes, data like this? Yes. Perfect. Now you can see there's a lot of rows with, and actually one more thing is that you see it's called jokes. Why? I've used joke in my lens model. What we need to do is that we need to rename it. ? That rename. Let's see. Jokes into joke.

And then axis equals one. , Perfect. And you can see each joke [00:28:00] is only the text, we don't have any vectors. And that is totally fine. That is the idea here. DF jokes equals to this one, the F jokes head, we don't have to show everything. . And if you, for example, take DF jokes of zero and then you will get, or I lock and I lock zero ~~and you will actually df jokes do pick out the joke and I lock, ~~and you can see here we get the full text.

, this is actually quite fun. Parallel parallel lines have much in common. It's sad that they will never meet. Yes. That is really good joke actually. , side note on that, let's now add our data to our table. Add data to table. . We can do it simply by, we have the table jokes, right?

This is our table. If it's taped off head we, it's empty right now, we can do table. Jokes, dots add. And we can take df jokes here and you can see we have [00:29:00] added a lot of data. . It takes a little bit of time, but it shouldn't be that long. Yeah, exactly. Now we have it. We have table jokes, head, and now you can see, Ooh, cool.

We have data. And we have the vector embeddings as well. Note that the vector embeddings, ~~these are, ~~were created ~~automagically or ~~automatically ~~with the, ~~with the model embeddings. We have the embedding model, which we had in our text model. If we go up a little bit here, we just put in the text, right?

It just found this choke column. It saw that it didn't have ~~an ~~vector column, what it did was ~~that it dust the. Conversion or it does it send, ~~it calculates this using the models vector embeddings ~~and ~~and calculates out the vector embeddings. We have vector embeddings for each of these.

. And I don't want to show all of them. I take two and I can do like this table jokes, ~~dots ~~to [00:30:00] pandas that you can see it. And ~~we can, you can see that ~~we have a lot of jokes here. We have 29 of them. . And we can take, ~~for example, ~~out a ~~vector, can take out ~~vector and ~~let's see, with small V here.~~

~~And you can see of zero, for example. And we can take, ~~you can see the shape here is 3072, which is the shape that we expected. ? That is really cool. Now it's time for us to do some searching. ~~Perform vector search. . ~~To do some searching, it's really easy. Table jokes. Do search data engineering jokes, for example.

Dot limits. 8.2 pandas. , eight closest ones. Yes. Perfect. And you can see we have why do data engineers hate nature Data engineers motto, what do you call the snake that runs your script? Blah, blah, blah. . At least you can see the top here. Ones are related to data engineers. Cool. And we can do similar thing here.

Copy this one, paste it here. I will do change a little bit. Give me some jokes on C sharp [00:31:00] and you can see, yeah, there's some with C Sharp related and then the Python programmer, ~~probably I, this is quite fun, but ~~probably Is that, why did the Python get bitten? Because he cannot see sharp or something?

Not sure. . Let's see. We can we can give continue here and give me some give me chemistry related jokes. I know I had some chemistry jokes there. Yeah. Then we get a few chemistry jokes. Copy this one. Remote lance. . Like this. ~~And I, ~~we'll have like in nature related jokes.

Yeah. . Then we got a few nature related jokes, and these were vector search. We are searching based on the closest closest vector distance from the from the search vector. This is the query vector. Or this is the Query and it will compute the query vector, and then it'll use the query vector [00:32:00] and compare to all these vectors that exist in our database table, and it'll calculate the distances.

And you can see. The closest distance are those that are fast. , this is sorting in ~~as ~~ascending order. Let's go into hybrid search. ~~And ~~hybrid search. Basically ~~it ~~combines traditional ~~key ba, ~~keyword based search with vector similarity search. ~~? And ~~keyword based search is using something called BM 25 which is which has been used a lot ~~in ~~in search engines for ages.

~~And ~~vector search is more recent for when we want to do searching with natural language. ? If you're searching for more exact keywords, then it's better to use traditional keyword based search. And if you want to search with similarities and you have changed the meaning and more natural language such, then vector ~~such ~~is better.

However, hybrid ~~such ~~is a combination of these two. And how should you do when you are doing search? Should you do just full text search or keyword based search or [00:33:00] vector search or hybrid search. ~~And ~~it depends a lot on your data sets. There are a few rule of thumb, but basically.

It's more of a trial and error. You try and see that, ah, is this~~ values ~~reasonable is this results reasonable, et cetera. . I'll continue here. In order ~~to do en to enable keyword based searching, ~~to enable keyword based search, we need to. Create an index, not on the text column, but on the joke column.

~~Let's see. Change this one. . ~~From, let's see, we can do table jokes dot create. FTS is full text search index on Jo column. And here I will do replace equals two. ~~If ~~if you're choosing another one, if you do it again, it'll replace the index. . And now I will do from Lance DB import, re-ran and re-ran.

What it does is that it'll [00:34:00] re-rank the result from a vector and a full tech search. ~~If ~~it re ranks it based on a certain algorithm and there are different types of re-ran that can be chosen. For example, linear combination. And the one that I will use here is RRF re ranker and this is the default one.

We'll use this one. Re-ran or equals to reran. RRF reran. It'll re-rank it based on a certain algorithm. . And also which re-rank you should use. It's also a hyper parameter that you should tune. . You are testing out different re rankers for your particular data set and see. What will give most consistent and best results according to your own metrics?

AI engineering is actually a lot of engineering, believe it or not. Results equals to. Table jokes, [00:35:00] search, give me nature related jokes. I use the same query as before to show that we can do a hybrid search instead and see if the results differ. Vector column. It's the vector that is our vector column and then FTS column.

We have created a FTS column, right? ~~Which is joke. ~~This is the full text search column and this is the vector column. You need to combine both, right in the hybrid. And when you do that, you do a ~~re-rank and you ~~re-rank. You put in your re ranker equals to re ranker. Dot limit. I'll do limit eight, we can see same as before.

And then two pandas, and then we have results here. . The first one was the same. Why do data engineers hate nature? And here you have a relevance score. Let me just see if there's something different. Second one, gold walks into a bar free. Why did the chemist ground his [00:36:00] kids? I told the chemistry joke.

Yeah, gold walks into the bar is the third one. It's yeah, it became a little bit different. This one was more, let me see. Gold Walks into a bar. Yeah, that was the second one. And now the second one is I told the chemistry joke, this had higher. Relevance according to the hybrid search.

That was quite cool. It's a little bit different and the, as I said, you need to try it out on your data set, but there are a few rule of thumbs. Let me change this to markdown ~~down. ~~Some rule of thumb is that we have. For exact matching. Then we use FTS full text search. Meaning based matching, then you use vector search and both or Yeah, both.

Or unpredictable or mixed [00:37:00] queries you use hybrid search. These are a few rule of thumbs, but the best is to test out which works. Try different hyper parameters. To get the results that you want. A lot in AI engineering to get more consistent results is, a lot of engineering.

You need to know how to evaluate the results what to evaluate on what are good results according to your own metrics and your requirements. ? Now one thing that is what need to be done is that if you are. Working in Git and GitHub repository is that you should commit and push, but before that we don't want to push the vector database.

I will basically just go into my gi, ignore yeah, I should have a ~~GI ignore. so.gi,~~ ignore. Very important. We should have a heightened getting ignore, but since I don't have it, I will have dot, ENV here. Save this one to remove my dnv because I have [00:38:00] my secrets there. Dots I will have a vector database I will also remove.

. I don't want the vector database to come up and the rest I can commit and push to my GitHub repository. ~~Yes. .~~

, In this video we have gone through Lance DB from the basics and up to different search with vector search, full text, search, and hybrid search. In the beginning we worked with different operations such as creating table, adding data, creating schema, using lens model. Took a look into embeddings, how that worked, and vector search with own vectors and then vector search with only text.

I hope that gradually you started with very basic understanding of Lens db, but then moving on to the key points of Lens db that is to utilize its vector capabilities and working with, the different vector search to find the closest matching text to your query, which is very useful for applications such as [00:39:00] rags.

Retrieval augmented generations where you can chat with your own data and your own documentation. That is really cool and I hope that I will see you in the next video where we'll continue building upon these topics and building up rag systems. Thank you for watching this video.

See you in the next one. Bye.

