# FastAPI and scikit-learn API connect to streamlit frontend

[00:00:00] Hello and welcome to this video that is a continuation on the video with Fast API and Psyche Learn. ~~When in, ~~in that video we created an API to serve psyche learn model. We created a random forest classifier ~~fast ~~and then the random forest classifier. We dumped it using job lib ~~that we ~~save the model.

Then ~~we we used psychic Learn or ~~we used fast API and ~~then we used ~~job lib to load the model and the fast API created an API to serve different endpoints where we had one~~ get ~~get endpoint ~~where we could get. ~~To show the data points. Then we had a post where you could create a prediction.

The prediction, ~~it re ~~required you ~~needed ~~to post the data on spel length, spel width petal length and petal width in adjacent object. We tried it out in the swagger ui. Then ~~we ~~we tested it out in Python, in Jupiter notebook and also in curl. [00:01:00] It worked that ~~we could create a ~~we could do a prediction through this, API and get back.

We could post this data and then get back the prediction, which flower it predicted. That is how far we came. I will show you that in the code soon. Then after in this video, we will go into using streamlet to actually creating the front end for this. In usual tutorials, you usually see that people create, streamli application directly with machine learning applications. That you use, for example, psyche learn directly ~~in ~~in streamlet. But the problem is that will be very tightly coupled and the way that we do it with an API in between, ~~and then it won't be, ~~it will be loosely coupled. It means that you can easily just ~~change, you can ~~remove streamlet if you want, and then ~~add, ~~put in another.

~~Another ~~front end. It just connects to this API. That is the idea. I'll show you. We've streamlet, but you could do this with whatever front end [00:02:00] you want. Yes. Let's move on to Vicious Studio Code and continue where we left off. 

**Kokchun Giang-1:** here in Visual Studio Code, I'll show you how far we've come. First ~~I create ~~I activate my environment, and then I did UV corn. ~~Korn, ~~API Colon app and then dash reload. I get into this fast API app, and I go into the docs. Here you can see we have get here and we can try it out, and we run it and we can see, we get back all the data points of the iris, and then for post, we click here and we can send in this request body.

When we try it out, we send in this request button. You can change this if you want. ~~The, ~~there's a ~~edan ~~model that will validate this. ~~That's, ~~see that~~ it goes into ~~it has a range of values. That's okay. Execute this. You can see that we get back a prediction. We get predicted flower, iris cosa.

This is how far we came [00:03:00] and I want to show you the API now it looks like this. Basically we have the router that we get ~~this ~~this endpoint here. You can use it to create several more endpoints by using at router. Here we have request and response schemas. Here, this is the requirement for the~~ re ~~requests that you have the values within certain ranges.

The ranges we got from doing~~ we did ~~exploratory data analysis on the, when we created a model. I expanded the range a little bit that it's a little bit more than what, ~~what's ~~covered in the dataset. Then we have the output is a string. Then basically here we have router get, and here we have router post slash predict.

This is where the prediction happens. Basically what it does is that we get the data ~~as a pay, ~~as the payload, as iris input, which does the validation for us. Then we do model dump and create a data frame out of it. We [00:04:00] load the model that we have exported before. This is the Random Forest model, and then we do prediction here with Classifier Predict, and then ~~we do ~~we return the prediction basically.

That is it for the API. We also tried it out using these explorations. Here you can see this is just showing what happens when we work with the P model to do model dump, how that looks like creating ~~the ~~the. Pandas data frame, how that looks like. Then this one is the thing that we'll look into today as well.

We used http X to create this payload, or we created this payload and then we used http X to do client post. We sent in this. Payload to our API. We needed to have ~~the, this we need to have this open. ~~This URL open. This terminal needs to here we are still serving our web server.

Then we can send [00:05:00] in request to this web server, and then it'll return a response, and then we can take a look into response. This is the correct status code. Oh, 200 okay. Means that it's okay and then we can take response to Jason and here is the predicted flower that we get. That is the idea.

Now we'll connect a stream it front end to this.

**Kokchun Giang-2:** Okay, we'll create the front end here, frontend pi. Basically what we'll do is we'll ~~create ~~import streamlet and let's see. Then I need to install streamlet. I'll create a new terminal here. You source then being activate UVP install stream it. Okay st then import [00:06:00] H-T-T-P-X from constant import.

We need assets path here 'cause we have the images in assets path. Okay. Let's just create the St. Markdown. Predict iris flower. Save this one. Then ~~we will do ~~I have activated my environment. Then I'll just do stream it to run front end like this. Yes, and it works good. Let's now do prediction.

Def actually I can leave the front down here and I'll do Def Predict flower. I'll send in the payload and then with HT Tpx dot client, time out equals 10 as client and then response [00:07:00] equals to client post URL. I'll send in a URL and I will send in Jason equals to payload. Then we'll need the U-R-L-U-R-L equals two.

For the URL I'll. Copy this one here. The request URL. Copy. Okay. Then ~~we will, ~~we'll send in the URL Jason payload and then response dots, raise for status and return the response. Basically just like that. ~~Okay, ~~now ~~it's time for us to, ~~when you think about it, when you're working with a frontend application, you have an application you want to send in spel length, spel width, pedal length, and pedal width. To do this, ~~you, us, ~~you want to have some kind of number field that you can have number input where you can change the values, right? To [00:08:00] do a number field there's ~~st number input. ~~St number input. Input and here we can say sal length in ~~cm, ~~centimeters, and then we have mean value equals to.

I will look this up to the ones that we use. I will make it a little bit more. 4.01 max value equals ~~two. ~~Let's see, 8.49. ~~'cause I think we had, ~~let me save this one. Close that one. Let me check the, API. Yeah, ~~8.5. ~~8.49 here. Okay. These ones, and then we can have a value in the middle.

For example, value equals 6.0. I will remove this one like this, save this one, and then rerun here. You can see that this is how the [00:09:00] number input looks like. You can increase this one, you can decrease this one. You can change it directly. Yes. If I go over that one, say 10. Then you can see this is in Swedish, but it means that the value must be less than or equal to 8.49 because that was the max value that we chose here.

For that we can call this sal length equals to this.

Yeah, we can change it to five. All right. Yeah. Five, enter. Yeah, that is. Okay. That means that spel length will have the value five. For example, we have st. Markdown, spel length, and I will do always rerun here. You see five here? If I change this one will change. Yeah, it's a rounding error here.

Six. Yes. The idea is that you can see that we get the value from the number input into this variable, [00:10:00] and we can do this for all these four. I will do the same here with all ~~the other ones. This one I'll just copy. Here I, I do the same for ~~the other ones.

Let me just remove the tab here. ~~Here we get four. ~~You can see we get similar for the other ones, we have ~~pet spel width, ~~petal length, and we have petal width. Now we have four variables. What we want to do is that we want to click on a button and then all these variables will be submitted into our predict flower, ~~which will submit it in, submit the payload.~~

~~In ~~which will post the payload into our endpoint. That is the idea. What to do now is that we will make a form. With St form, say Iris data, for example,

tab this in. I'll remove this one and I will say Submitted equals to ST Form. Submit [00:11:00] button Predict, or we can make it into capital letters Predict. Now we have it into form. We have predict button. I'll just show you what's submitted. Is st dot mark down submitted. If I run this one, is it true?

In default it's false. True. False. Okay. It means that if this becomes true, then it's quite easy that we can do. Remove that one. If submitted, if this is true, then we have a payload. Payload is basically like this. We have sep length, colon float. Length, and we have, because it's come out as a string.[00:12:00] 

Let me see if I need, yeah, we'll do that. SS weed let's see. S weed. I will just before I would, before I do this, I will actually just want to check the type I want to check the type of St. Mark down say type of petal width.

Class float. Ah, it's already float. Oh, good. If the already is float, then I don't need to change it to float here. Okay. Then we continue here. What else do we have? We have spel width. We have spel length. We need to have petal length. Petal length and we need to have petal width as [00:13:00] petal width.

Okay, now we have our payload and what we do, if our payload is very simple, we have a response equals to predict flower. We send in our payload. Remember that the payload need to be sent in as a dictionary, and this is the dictionary that we have created.

We have a response. We can do we can do SD markdown response,

rerun, predict, and we get response 200. Okay.

We can take J. If we rerun this one, ah, then we get predicted flower, iris versus color. Okay, then we can do a simple as this. We can do flower equals to [00:14:00] response, get predicted flour. We take out the predicted flour here. We make it into case fold that it's a lowercase, and then I change this to flour and I can make it into an F string here.

We have a predicted flour is st. Then we have, okay, we can start with this one. Always rerun, predict. We get predictive flowers, iris versus color. Cool. We can do ST image. Now F stringing assets path slash flower, because this is lowercase and it's this exactly same as the ones I have in my assets.

We have ity color. [00:15:00] I risk ity color. Except we need to have dot ~~j ~~jpeg also, dot jpeg,

and this should be it. If I predict this one, okay, we may need to, okay. Let's see. Flower. Yeah. We need to have, remove this one. We had an Okay. Predict Yes. We got the S color. Beautiful. Okay let me take a look into some in our data. Actually, we can take a look into the data.

Also, if we take here before the form, we can take here St. Data or Yeah. To simplify. I don't need to do that. We'll go into explorations Model development. [00:16:00] I just want to look into the data a little bit. Okay, this should be Iris then spel length 5.1. We'll make it five. Spel with say three, and then petal length.

Okay, 1.6, petal width, 0.2, zero point and zero comma. Three, for example, predict Iris, and you have Iris here. Good. Let's see if we can find another one here, Iris. Yeah. I'm a little bit lazy here, otherwise I could just, yeah, I'll just scroll it here.

I risk ol we showed, right? Or I forgot. Yeah, we can take ol let's see.

[00:17:00] Six. 2.83 works here, petal length four, 4.8 and then petal with it's quite large. One, one comma three. Okay. Then we have here IC color. I forgot if I missed the one flower or not. But as you can see, this basically works and you can input several different types of, parameters here, and then you do the predict, ~~you get the flower ~~you get the flower image.

This is our front end, basically. If we want to go one step further here. Right now, you can see in my front end we have the URL is a local host. This one we cannot share to other people. If ~~want, ~~we want to share this to other people, we need to deploy it. What we can do to deploy it is that ~~share, ~~you can deploy this Streamlet app if you click deploy, but then ~~if, ~~even if you deploy it, you won't be able to do the prediction because, it still [00:18:00] points to this URL, right? This local host that's only exists in my computer. What you need to do is that you deploy the API into Azure functions. Or some similar services. I choose Azure functions because it's very cheap and it's serverless. ~~It's ~~it's really good.

You can deploy it into Azure functions and then you will have an Azure function, URL which is either public or requires an API key. You choose that and then you can. You change, you just change this URL to the one from your Azure function that URL that domain.

Then you can deploy this streamlet app either in Azure if you deploy it in Azure, you need to also dockerize it. Then you can deploy it ~~in ~~into web apps or you can deploy it ~~here ~~into stream the cloud and it'll still point to the Azure functions. I will. Probably [00:19:00] make a video where I will deploy it to Azure function that you can see this app deployed and running.

in this video, we have created a streamed front end to connect to our fast API application where we served a psyche learn model. The psyche learn model, we developed separately in Jupiter Notebook in the beginning. Then afterwards we got a job lib dump that ~~which ~~we loaded into our API endpoint~~ for ~~and created one for posting.

~~Then when, and ~~then we. Connected into Streamlet and posted the payload into this API endpoint. Also in the end, we discussed a little bit how to move further, how to deploy this~~ into in, ~~into the real world, which I might create a video for that later on. But thank you for watching this video and I hope that you learned a lot and see you in the next one.

Bye.

