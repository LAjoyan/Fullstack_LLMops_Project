# Pydantic with gemini to structure output in a much neater way

**Kokchun Giang:** [00:00:00] Hello and welcome to this video where we'll use pedantic together with Gemini in order to structure the output that it becomes much more structured than before, that we can get Jason data back and we'll get back by pedantic objects. Models ponic models, which you can use to further process the data.

And we have done this. I have done a similar video of this before, but the video I did before was relying too much on the prompt and there's an issue with that. I will show you example here. You can take a look at this example here. We use the prompt and tell it to not write out for example, these back ticks and sometimes the back ticks comes anyway.

Still need to parse it afterwards to remove these b but this this is not very [00:01:00] robust as as the model will give different result each time.

If you want it more robust, you should take a look into the documentation and see that, oh, there is a way. In Gemini to actually get it structured directly by placing in a edan model.

that is what we will explore in this lecture, and you'll see that this is much more robust and cleaner than in the previous lecture. But it's a good base to see how you would structure it. By yourself . That is pretty good to set the basics, but now we'll make it much more robust and cleaner.

**Kokchun Giang-1:** you can see this is an empty ~~v ~~vicious studio code repository or folder. And what we start with I have this dot nv, and here I've placed my

Gemini underscore API underscore [00:02:00] key. It's very important that you name it in this way, or you can name it Google API key. And the reason for that is if you name it in this way, then.

The Gen ai, it's quite smart. ~~This ~~this class and what it does is that it will be able to find this environment variable automagically. You don't need to work with import o. And then low e, nv and os get nv and then send it in as API key, it'll find it automagically.

However it is good to learn how to do it with nv with Python, NV and low e NV and os dot getTV as these are the basically fundamental and the most. To get the secrets from ENV files. But since [00:03:00] Gemini has this automagically for us, we'll take, we'll make use of it. You'll see the code is much shorter and cleaner.

Let's start now. I will create a virtual environment. I'll activate this virtual environment. I have done UV VNV, and now I'm activating it with source. I've activated it. And then UV pip install. I PI kernel. To make, to work with chip notebooks, and then I will need tic in order to work with our pedantic.

And then we will need what else do we need? ~~We need to have Gemini, ~~we need to have Google dash Gen ai. And this is basically all I need pandas as well because I want to demonstrate the working with pandas data frame afterwards. Okay. This is all I want done. That was quite quick.

Okay. Let's open up a PYN notebook now. I'll call this [00:04:00] Gemini. ~~Tic robust output. ID Okay, let's call this structure Gemini. Outputs with gigantic. ~~Okay. Changed my virtual environment. Close this down, change this to Python, and we're ready to go. From Google import gen AI from, let's start with this one, client equals to gen AI client

**Kokchun Giang-2:** let's. Create the response here. Response equals to client dot models, generate content. And here when you do generate content, you choose which model you want. Model equals to Gemini dash 2.5 dash flash. I'll use this one as a start, but when I will generate more [00:05:00] data later on, I will move on to the pro as it's more capable Contents equals to, this is basically from the example I was I've changed it a little bit. List a few Asian soups, recipes, a yummy description, and list the ingredients. Okay, this is my starting response. Create this one. And I will say dot text. I'll print this out. And if you just look at this one, this is just the normal way we have done this.

This is without any without any schema that we forces on. And we'll see what it looks like in the beginning. Here you can see. It's just unstructured text or basically it's markdown text, which you could [00:06:00] use. But the ~~mo ~~mostly unstructured maybe semi-structured if you would say, but we can see that this is just some text that we get from this model.

Let's ~~copy this one. Can we do better ~~copy this one? What we could do is that. If you follow from the previous lecture, you could do like this, for example we make it a multi-line string. Give me fields of~~ gimme me fields of let's see. ~~Recipe name string. Let's see, what do we have more?

We have a description. This is a string as well. We have ingredients, which could be list of string and then we'll say not in markdown format. ~~Something. ~~Something in this style. If I do response text, what will [00:07:00] we get from here?

Yes, it's a little bit slower when you let it think through how it will create this.

Okay. And you can see it here. We have the response to text. I will type out respon, I will to print response text and you can see, okay I, maybe I should have written it as adjacent format,

**Kokchun Giang-3:** Okay, let's make this structured we can make it structured. In this way. We create a class called recipe. This should be a base model. Then I should from Ian import base model. I have my base model.

And here are the recipe name as a string. We have description [00:08:00] as a string note that these are nan models. It's basically Python classes, but they are, they're inheriting this base model that it is a base model as well. It's an instance of base model. We have here ingredients. List of string. That is what we have.

Recipe name, the description, the ingredients as a list of strings. And then we have our client, right? Client equals the gen ai. Do client it. Actually, I can go up and paste what we had before. Yeah, this one, I'll copy this one, this response.

Okay. Here we have, let's see here we have our model, our contents, and what we need to do is just add [00:09:00] this config. This is quite simple and super nice to use, response. You call it response mind type, and you have application slash json, and in this way we'll get JSON data and then you choose the schema that you want.

You have here response schema, and you can have here list of recipe. That is it, friends. We have here close this one response mind type as application Jason. And then we have response schema as a list of recipe because that is what we want in the end. We want the list of recipes. Okay, let's do this response text [00:10:00] print.

Or basically, I don't need to write response to text, but you can see directly here. We have a list here, and ~~we get, ~~you can see Jason data here. Recipe name, Tom Mko, description, the description of it, ingredients as the list of strings. And then we have the next one, et cetera. ~~Then we can do like this response past, and this is your data.~~

You have a list of recipes. You have here recipe, recipe, name, description. ~~You have let's see. ~~You have recipe here. Next recipe. You had the description and the ingredient somewhere. Let's do like this. We call this recipes. ~~Recipes.~~

We can take a, since it's a list you can see, okay, three recipes, fine, recipes of zero. The first one we can take dot description. Here is the description. Recipe. Zero [00:11:00] dot recipe name? Ah, M. Good. Okay. Recipe Zero dot ingredients. And you can see the ingredients here. Quite cool. Quite cool. ~~Can we, ~~let's simulate something else.

Let's simulate house prices.

Let's create our model here. Class home, BM based model price in what do we have more monthly fee int. We have a living area. Float number. Let's see, number rooms. INT type. Okay. The type I want to be either apartment or home. For that, we'll do from typing, [00:12:00] import literal, then we'll have literal here as apartment.

Or house and then address as string. Okay, this is my pedantic model, the home, and now let's create this one. Response equals to client. Do models dot generate content. And model Gemini 2.5. I will have a pro since it can it can generate more data. Contents equals to. Let's just do a multi-line string here.

List 50 apartments and houses in Sweden with their monthly [00:13:00] fee price living area.

Number of rooms address type if it is apartment or house. All currencies are in SCK. Data should be simulation of Swedish. Housing. Okay. And here, let's make after the content, let's do the config equals to the same as before we have response mind type application slash json. And then we have response schema as list of home.

And that [00:14:00] is it, my friends. Let's try this out. Homes let's see. Yeah, ~~we can we can type, ~~we can do this. We can run this first.

It takes a little bit of time for it to generate this.

Let's see what we get here.

Did I miss something type address? No, I think it's fine. This will go into this schema here that we have created. We're generating ~~50 ~~50 apartments and houses. It should be 50 in total.

Okay, it's done. Let's look at it now. Response past equals our homes. Homes. Woohoo. We have data now, you can see this is let's check it out. Length of homes. This is a list, right? 50. Okay, great. Homes. Let's ~~take ~~take a look into the first one. Zero. You can [00:15:00] see this is a Edan model, home of homes of Zero.

We can take dot price. You can see the price. ~~We can take a look into. I'll copy this one. ~~Homes dot address. Maybe I can see the address here. Great. Okay, now I want to do some filtering of this. And in order to do filtering of this, it's quite simple. We just need to put this into a pandas data frame and then we can do ~~whatever is, ~~whatever we can do in Pandas data frame.

Import. Pandas as PD and take a look into this. Homes is a, okay, it's the import that takes a little bit of time. It's the homes already existed. Okay. You can see homes is a ~~list ~~list like this. If I would do like this PD data frame of homes, then we get. Not what we want, right? This is not what we want.

Instead take a [00:16:00] look into this. I will make a code in between here. We can do homes, dot done the dick. And you can see, let's see. List doesn't have done the dick, right? Yeah. Home has a done addict. Homes of zero ddi. You can see this is the dictionary of one entry. What you could do is that you can loop through this.

Instead of putting homes here, you can do like this home, do DDI for home in homes, and you can see this is your data frame, as simple as that. Or take a look into this one response is this one right? Response dot. Do you have Jason? I know we don't actually response dot [00:17:00] text. Yeah. This okay. Yeah. I think this is simpler.

You have you or you could take another direction, is that you take response text and then you do model validate. ~~You DC realize it into a or you yeah. ~~You DC realize it into a pedantic model and then, or actually ~~this is quite, ~~this is much simpler. Forget what I just said. Here you have home do means that dict means that you will get this dictionary for each entry of home in homes.

And then when you have this dictionary it's basically you'll have a list of dictionaries. And this is perfect for creating a pandas data frame directly. Now. You could do df head, we could take a look into only the cheap houses, or df query price. Let's see, price smaller than 5 million for example.

And [00:18:00] let's take a look into type equals ~~apartment type equals two ~~apartment. And ~~you can or ~~type equals to house. I wanted to have cheap houses. And you can see fewer cheaper houses. But yes, we found it we are able to to filter this data frame. When you have this one for example, you could say like this cheap houses equals this, cheap houses.

And then you could do like cheap houses dot two CSV if you want. And you could have like cheap houses dot csv. You can see here we have our CSV data. That's cool. But I don't want to have the index. Index equals the false. Okay. Run it and you can see. Yes. Perfect. Ah, cool. We can simulate data now with structured data and then we can do a lot of processing and learn a lot from this.

this was super cool that we used pedantic together with Gemini to get [00:19:00] structured responses that we get out our JS data. And then finally we used it to create Panas data frame to show you that it's very easy to just filter the data once we have it in JSON format. And this is in contrast to not a video that we made before.

Was that, there we utilize the prompting more, but that is not ~~as as ~~as robust as this video because here we use the built in in Gemini we used, its, response type, response mind type s the application Jason. And we also used response schema and we placed in our pedantic model over there.

Super cool. Super cool. I hope that you've learned a lot watching this video and see you in the next one. Bye.

