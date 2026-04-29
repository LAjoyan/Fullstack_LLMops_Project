# pydanticAI chatbot

[00:00:00] Hello and welcome to this video where we've come into pedantic ai. This is a really good framework for creating AI applications. You can use this for AI engineering. You can create rags, you can create chat bots, you can create AI agents in a very neat way, since it has very well it's integrated with.

Edan. If you work with edan, it's a top library for doing data validation. That is the strong point with Edan AI that you can get output from an LLM in a structured way. Usually LLM produces output in terms of strings, and if you want to make it into a structured way, ~~usually you.~~

You need to parse it yourself or you use other types of libraries to parse it. But then~~ most, ~~many of the other libraries also depend on edan. But Edan AI is developed by Edan team itself. This is really good. I think it's [00:01:00] the. Right now to go library to use for creating chatbots and creating agents and creating rag applications and other types of AI applications.

This is a really good tool. We'll use it together with. First we'll go into some exploration of how it works. ~~I will use, ~~it's also ~~note ~~noteworthy that this is model agnostic. You can use whatever model you want, but we'll use Gemini as it has a very good free.

Free tier. And then afterwards ~~we will ~~we will start with doing some explorations to see ~~how ~~how it works to create a simple~~ chat ~~chat application. Then we will take this into. Creating a chat application and then also connect it with a front end. ~~Now ~~and the front end, you can choose Tai, you can choose Streamlets.

You can choose whatever frontend framework you want. But if you want other frameworks that is not in Python, then probably ~~you, ~~you do need to make it into ~~an A. You need to create ~~an API, for [00:02:00] example, a fast API. However, I will make it simple and I will choose. ~~Ty, I, ~~and maybe I'll just stream it in another video.

I'm not sure yet. But this is the idea and I'm not sure if I will divide this into several videos or not. We'll see how long this video gets.

**Kokchun Giang-1:** I'll start in the browser here. We'll search for Gemini, API, and here you have Gemini, developer, API. We go in there and then here you can see explore models in Google AI Studio. Let's go into that one. Here you need to log in. I have logged in, but then you click on here, get your API key, and you.

~~You ~~follow along how to do that. Here you can see I've gotten this one. You can click here, look up. You create an API key and then you bring this API key back to Visual Studio Code and we'll see in Visual Studio Code.

**Kokchun Giang-2:** here I am in Visual Studio Code, and let's start with U-V-V-N-V and the source Van Bin Activate to activate my virtual environment. Now it's time to [00:03:00] install some stuffs. I will need IPI kernel to work with Jupyter Notebook. I will need to have let's see, what else do I need? I need to have a p is it pedantic ai like this maybe?

No, it's pedantic ai. Like this? Yes. Underscore. Okay, I have Python ai. Let's see what else I do need. I need to have a nv, UV PIP install Python dash en nv. Then I will need to have UVP install pandas. Or do I need pandas? Maybe I don't need pandas for this. Actually. I'll take t pii. I need a TI to build my front end.

This could be it. I think I'm satisfied here for now, and if I need something more, I will install it on the way. Start with a e NV here and in dot ENVI will create here. Gini. [00:04:00] API Key equals to my Gemini API key. I won't show this to you, but you should fill in your API key here.

**Kokchun Giang-3:** now I'll create a Jupyter Notebook chat. I'll call it chat. Test dot or yeah, chat test dot I. Or chat. EDI pin BI call it EDS, exploratory data analysis, but it's basically explorations. Okay? Chat with tic ai. Okay, here, let's change our Python environment to the tic the virtual environment and change this to Python.

Let's start very simple. From tic ai import. Agent and then we'll need from dot NV import load nv. Then we'll take load e nv. Then when we do this ~~we'll in ~~we'll [00:05:00] import we'll load the do NV here. We can do OS do get ENV, and then you can write Gemini API key and. We need to have os of course import os.

When you run this one you can run it to just test out to see that it actually prints out your API key. I won't do that because I don't want to show it for you. Here you should try this out. They type in try to run this to see that your API key is. Printed out. Okay, but I won't do that. I will create a chat agent chat agent equals to

**Kokchun Giang-4:** Chat agent equals to ~~agent. ~~Agent let's see here. You search for Gemini and you can see here Gemini 2.5 flash. We'll pick that one. You will know that this one, it [00:06:00] will take from the environment variable. When you do load ENV, you will have the environment variable. It'll look for the Gemini, API key, or the ~~Google, ~~Gemini Google, API key.

After this one, we'll create a system prompt. The system prompt that I will pick is let's see, be a joking. Okay. Programming nerd. I will make a very simple one, I don't use any much prompt engineering here. I'll just make it very simple. Always answer with a programming joke no matter what the question is.

Okay, that is it. We have a ~~chat agent. ~~Chat agent. Let's run this one. You can see it works now. [00:07:00] Agent is a Google model and you can see a little bit how we'll see how to use this one. To use this one, we can do chat agent, we can say. Chat agent.run. Hello. You can see it's a coro routine.

What does this mean? It means that ~~we ~~it's asynchronous, we need to await for the answer. Await chat agent, run. Hello. Run this one. You can see here's the results wide, we can say results equals to this one. Results. Why did a programmer quit this job? Because he didn't get a raise.

Oh, this is really funny. Okay, result we can say dot output, and you can see this is the output. This is the string that was the output. We can [00:08:00] also control how the output should be. But we will keep it very simple in this lecture, we won't do that. Let's see what else? Let's try another thing we can do awai.

Chat agent do run. Tell me how to choose an Azure region. Okay, say result equals this one and then result output.

Okay. See what it comes up with. Choosing an Azure region. Oh, that's like a really complex switch statement in a try-catch block where the default case usually just points to east us to, okay, this is quite funny. But let's say now let's now use this in an actual chat app. ~~You can use for example if I do like this I copy this one again.~~

Results dot output. Actually, I would print this one, and now I will say, [00:09:00] what did I ask you first? Because we'll see. We'll want to see if it has a memory or not. What did I ask you first? My memory is like a rest, API delightfully stateless. What was the first get request again? My session data just isn't persistent.

Okay. It says, saying that it's not persistent. Okay, something we need to know how to get the messages. Results dot all messages. We can see here are the different messages that we have. We see the first one is be a programming nerd. Always answer with a programming joke. This is the system prompt,

and then you can see there's some date and timestamp on when it that was. Here you can see. What did I ask you first? This is the only user prompt that it sees, and then this is model response. This is what it responded with. Okay. You can see a little [00:10:00] bit more details like Gini 2.5, flash, et cetera.

Okay. It doesn't have the memory, it has all messages looks like this. How to get it to have memory. It's quite simple actually. We can copy this one.

**Kokchun Giang-5:** Let's change this text. What did I ask you first? Let's see. How many service do Google have around the world Google Cloud platform have around the world? Let's say, let's let this be the first question. We can print out the results. Okay. How many services? Google collateral.

That's a bit like asking how many bits are in a bite. Okay. That is good. They turn it into joke. But now let's create we have result at all messages because I don't want the, I don't want the first message to be always. Okay. Let's see. Always. Let's see. Yeah. Here you [00:11:00] can see user prompt.

How many servers do Google Cloud platform have around the world? This is our first question, and then you can see the answer here. Yes. Now let's try to see if it has a memory.

What did I ask you first? What did I ask you first? Now let's have a memory. Message history equals to result. Do all messages and let's see what it says. You asked me how many service do Google Cloud platform have around the world? My memory is excellent, unlike the bug that keeps escaping into production.

Then it comes into a question. Good, it has memory. I will just try again. What did I ask you? What did I, or let's see. Okay, tell me more. [00:12:00] See if it can refer back to this last question. You want more? That's like asking a full stack developer for just one more feature before deployment, but since you asked for more.

~~Okay. It continues with this JavaScript developer. Why was the JavaScript developer said okay, because he didn't note I don't comment the jokes. ~~Okay. Yes, it seems to work. Let's continue make this into a real application now. To do that, I'll have a chat. Pi and from P. Ai import AI agent, ~~import agent.~~

~~Let's see, or actually I need to have ~~import agent. Then from NV import low e nv and we will have that should be it, and then low e nv and then class joke bot. I'll create it into a class deaf done in it. ~~The der init. ~~I will pick self.chat [00:13:00] agent equals to agent. Then here I will put in Gemini 2.5 flash.

Then I will take, actually I will just steal this one. I'll take the same here. Copy this one.

Okay, chat agent is this agent peer programming joke. Self result equals to none. We start with none here, and then deaf chat. This is I think this is the only method I need for now. Self prompt is a string and it should return back a dictionary. Okay, here, message history equals to self dot results all messages.

If self dot results [00:14:00] l. Oh, okay. We don't need that actually because this is self let's say self-taught result at all messages. Yeah. If there is self-taught result else it's none self, the result is is none by default since we have created it as none. Then we will make this message history into none if we don't have a self result.

Then self, the results equals to self the chat agent. Here I'll use Run Sync. ~~There is, it didn't work in ~~it didn't work in PYT Notebook with run syn. Instead, you need to await because ~~there, ~~there is already an event loop there. I won't go into Async programming in this video, but~~ just ~~just know that you do run sync here because I need this to make it work with type high later on.

Prompt. Message history equals to message history, and [00:15:00] that is it. Return. I'll make a dictionary here. User prompt and then bot self dot result dot output. That should be it. Then let's try this out. If done, the name equals ~~the done ~~the main, and then I'll run This bot equals the joke bot and result equals the bot.chat.

Hello there. Okay. Then we'll print results. ~~Do output.~~

Actually, you don't need to print result at that, but just the results. Okay. Run this one.

Yes. Seems to work. Why did the program quit this job? Then I will also copy this one to see let's see. We do print like this and then back slash n also. What did I ask first? What did I ask you first?

[00:16:00] Okay. Hello there. Oh, hello. Then what did I ask first? Oh, you initiated the main function of our conversation. It was a classic print. Hello there statement. Okay. ~~It ~~it refers back to the first message. Good. It has memory as simple as that. We have a chat application and now we will.

With this, we can build our front end.

**Kokchun Giang-6:** Okay, let's build our front end. I'll call it main dot pi, and here we'll use Typi to build it. Import, tai pi, ~~tai ~~gui ~~s or import PWI builder, STGB ~~from Tai PII gui, import GUI from chat. At import joke bots, and this is it. Bot equals to joke bot, and then we'll have a user prompt. User prompt [00:17:00] equals to empty, and then messages equals to empty as well.

Then chat history. Equals to empty list and then uses equals to human bot. That is what we need in the beginning. Then we'll have a ~~W ~~TGB do page as page. We'll do with tgb, part class name. I'll call this chat like chat window, for example. TGB text let's see. Chat with joke bot.

Chat with joke bot mode equals to md markdown. Then this should be it if done. The name equals to done the [00:18:00] main. Then we'll do Gui page equals the page. Then we'll have I, no, I won't have a CSS file for this one. Make it very simple.run and dark mode equals false. Use reloader. Equals true port equals to eight 80.

Host equals to 0 0 0 0.

Okay? Yes. This should be it. Actually, we can have dark mode on it doesn't matter. Okay. Like this. Then I'll run this one. Mode equals run ~~.~~

~~Yes.~~

Now let's create our chat bot. We'll need to have we will need to use tgb do chat. This is very cool. TGB chat. What you need to [00:19:00] place in here is messages. Then you need to place in uses equals to uses. This you can find from the documentation in type I sender ID equals to uses of zero.

Then you have an on action. Equals to send message. This is a function that we'll create. I'll create this ~~send function ~~send message. It takes in a state, it'll take in a variable name string and it'll take in a payload that is a dictionary. This is important. Then from.

I will see. I'll take print and I'll show you what the payload is. Very important, what it looks like. If I restart this one, you can see that we have a ~~chat ~~chatting [00:20:00] window now. If I say hey and run this one, you can see this is the payload that comes back. It's a dictionary. You'll get action as send message.

ARGs and it's by doing an enter. If I say something else and I click it, you can see the it's a click event here. ARGs click, and then you have here in the end of the ARGs, you see this is the message and this is by the human right. That means we can extract some things from the payload. We can take out the message, for example, is payload that gets ARGs and we'll pick out the second one is the message.

If I take out the message here and you can see let's see, user equals to payload dot gets ARGs. Of three. Then we can have like user comm [00:21:00] message. You can see if I rerun this one, clear the terminal and I'll say, Hey, I'll say hey and enter. You can see human and hey. Based on this one, now we can get the message ~~from ~~from the chat and let's do something with it.

Try results equals to bot chat message. We want to put in the message here and then we have bot message equals to results get of bot. Remember that we get out a dictionary from ~~this ~~this method. We have the bot message now.

Then we just accept here we can accept an exception as e and then bot message equals to an F string here. Bot error. We can put in our E. Okay. Then we [00:22:00] take messages dot append. What do we want append? In the documentation it says it needs to have three things. It needs to have ~~the ~~the ID in the string.

It needs to have the message and it needs to know which user it is. Then we can take string of length of messages. ~~Comm. It needs to be, yeah, it needs to be a topple, the, ~~it needs to append a topple of this first and then the bot message, and then uses of one. This is the human. Finally, state dots messages equals to ~~message ~~messages.

Like this, and this should be it. Let me see. Hey, slay. Okay. Ooh, there's a message here, and then the bot answers. Hey there. Why was the JavaScript developer [00:23:00] said Because he didn't, okay. What did I ask first? Okay.

You asked the grand opening, blah, blah, blah, hay bay. Okay, ~~cool. ~~Cool. It works, but it doesn't put in the user prompt. Let's fix that. Here we should have messages because ~~that one is put that one, ~~we give it to state messages, which we use to display the messages in TGB chat here, we need to put in the messages here equals to, or messages dot append.

It's basically same as this one. I'll just copy this one actually. Then string length messages. Yes. Here we have the message. This is the human message. Then use, this is zero, save this one. Restart this one.

Let me see. Okay. Clear this one. Hey. We can see, hey, this is what the user have [00:24:00] written. Why did the program quit this job? Because the raise. Okay. Explain that joke more. I,

I, yeah. Explain that Chuck. More. Why did the program start? Because he couldn't get any bites. Oh, that was funny actually. Okay. Let's see. What did I ask first?

Why did the programmer use a screwdriver? Because he wanted to bite into the code. Okay. It, it refers back to this question

**Kokchun Giang-8:** okay, I found the bug that looked like the memory. It didn't have any memory, even if it did have a memory. Let's try this out first. Hey, there. Now it should give an answer.

Okay. Hi there. Blah, blah, blah. What did I ask you first?

Yes. It says about here very special string value, which upon [00:25:00] inspection is, Hey, there, tell me a math joke,

but error unavailable. The model is overloaded. Please try again later. Okay. There's, I may have used it a little bit too many times. What did I ask first? Maybe I sent too many requests. Ah, okay. Yeah, we needed to wait a little bit, but ah, that's classic. If I were performing a Git log one line, blah, blah, blah, you will see that.

Ah, would be, Hey there. It remembers. Okay, what did I do well in the chat here? We had before? The system prompt was I wrote no matter what in the end. I removed that one and now it's be it joking, programming there always answer with a programming joke.

. The memory works well. 

Cool. Now you have a chatting application after we have done this work. We started with some EDA with identity ai and then afterwards we went on to doing this chat class [00:26:00] and tried it out in the terminal. Then finally built a Type I application front and. Based on this. Quite cool and quite short amount of codes.

We got a chatting window that we can chat with. Also since it's a type application, you always have the possibility to style the chatting windows to your liking you can make it look more for example, messenger chatting or some other. Cool chatting style. Maybe I'll cover that in the future.

But for now, this suffices and you have learned the logic behind it and work with both p ai and TI. I hope you learned a lot from this video and see you in the next video. Bye.

