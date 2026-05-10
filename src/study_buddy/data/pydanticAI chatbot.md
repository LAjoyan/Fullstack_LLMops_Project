# pydanticAI chatbot

Hello and welcome to this video where we'll go into PydanticAI.

This is a really good framework for creating AI applications.

You can use this for AI engineering, create RAGs, chatbots, AI agents, and many other AI applications in a very neat way because it integrates very well with Pydantic.

If you work with Pydantic, you know it's a top library for doing data validation.

That is the strong point with PydanticAI: you can get output from an LLM in a structured way.

Usually LLMs produce output as strings, and if you want to structure that output, you either need to parse it yourself or use another library.

Many of those libraries also depend on Pydantic internally.

But PydanticAI is developed by the Pydantic team itself.

I think right now it is one of the top libraries for creating chatbots, agents, RAG applications, and other AI systems.

We will use it together with Gemini.

First we'll explore how it works and create a simple chat application.

Then we'll connect it to a frontend.

You can choose Taipy, Streamlit, or another frontend framework.

If you want a frontend framework outside Python, then you probably need to build an API first, for example using FastAPI.

But I will keep it simple and use Taipy.

Let's start in the browser.

Search for:

Gemini API

Open Google AI Studio.

Log in and click:

Get your API key

Then create an API key and bring it into Visual Studio Code.

Now here in Visual Studio Code, let's start with:

uv venv

Then activate it:

source .venv/bin/activate

Now it's time to install some packages.

We need:

* ipykernel for Jupyter Notebook
* pydantic-ai
* python-dotenv
* taipy

Possibly pandas later, but maybe not yet.

Then create a .env file.

Inside it:

GEMINI_API_KEY=your_api_key

I won't show my actual API key, but you should place yours there.

Now let's create a Jupyter Notebook:

chat_test.ipynb

Change the kernel to the virtual environment.

Now let's start simple.

from pydantic_ai import Agent

Then:

from dotenv import load_dotenv

load_dotenv()

Then:

import os

os.getenv("GEMINI_API_KEY")

You can test this yourself to make sure the API key loads correctly.

I won't print mine because I don't want to expose it.

Now let's create a chat agent.

chat_agent = Agent(
"google-gla:gemini-2.5-flash",
system_prompt="""
Be a joking programming nerd.
Always answer with a programming joke no matter what the question is.
"""
)

This automatically uses the Gemini API key from the environment variables.

Now let's try it.

await chat_agent.run("Hello")

Notice this returns a coroutine.

That means it is asynchronous and must be awaited.

We can store the result:

result = await chat_agent.run("Hello")

Then:

result.output

returns the model response.

For example:

"Why did the programmer quit his job? Because he didn't get a raise."

Very funny.

Now let's ask another question:

await chat_agent.run(
"Tell me how to choose an Azure region"
)

It still responds as a programming joke because of the system prompt.

Now let's test memory.

We ask:

"What did I ask you first?"

The model replies:

"My memory is like a REST API — delightfully stateless."

Interesting.

Let's inspect:

result.all_messages()

Now we can see the full message history.

We see:

* the system prompt
* user prompts
* model responses

So the memory exists, but we need to pass the history back into the next request.

Let's do that.

message_history = result.all_messages()

Then:

await chat_agent.run(
"What did I ask you first?",
message_history=message_history
)

Now it remembers correctly.

Great.

Now let's build a proper chat application.

Create:

chat.py

Import Agent and load_dotenv().

Then create a class:

class JokeBot:

Inside **init**:

self.chat_agent = Agent(
"google-gla:gemini-2.5-flash",
system_prompt="""
Be a joking programming nerd.
Always answer with a programming joke.
"""
)

Also:

self.result = None

Now create a method:

def chat(self, prompt: str) -> dict:

If self.result exists, use:

message_history = self.result.all_messages()

otherwise:

message_history = None

Then:

self.result = self.chat_agent.run_sync(
prompt,
message_history=message_history
)

We use run_sync() here because later we want it to work nicely with Taipy.

Finally return:

{
"user_prompt": prompt,
"bot": self.result.output
}

Now let's test it.

bot = JokeBot()

result = bot.chat("Hello there")

Then:

print(result)

Now ask:

"What did I ask you first?"

It correctly remembers the previous prompt.

Great.

Now let's build the frontend.

Create:

main.py

Import:

from taipy.gui import Gui
from chat import JokeBot

Then:

bot = JokeBot()

Create:

user_prompt = ""
messages = []
users = ["Human", "Bot"]

Now define the page using Taipy.

We create a chat component with:

<tgb.chat>

This component requires:

* messages
* users
* sender_id
* on_action

The on_action callback will be:

send_message

Now define:

def send_message(state, var_name, payload):

The payload contains information about the message event.

By printing the payload we can inspect its structure.

We extract:

message = payload["args"][2]

and:

user = payload["args"][3]

Then:

result = bot.chat(message)

bot_message = result["bot"]

Next we append both messages to the message list.

First the human message:

messages.append(
(
str(len(messages)),
message,
users[0]
)
)

Then the bot response:

messages.append(
(
str(len(messages)),
bot_message,
users[1]
)
)

Finally:

state.messages = messages

Now run the app.

We get a working chat window.

We type:

"Hey"

The bot replies with programming jokes.

We ask:

"What did I ask you first?"

And now it correctly remembers because we pass message history.

At one point I had a bug where memory seemed broken.

The issue was actually the system prompt.

Previously I had written:

"Always answer with a programming joke no matter what."

That caused weird behavior.

After simplifying the prompt, memory worked correctly.

Now we have a full chat application.

We started with exploration using PydanticAI.

Then we built a JokeBot class.

Finally we connected it to a Taipy frontend.

Quite cool, and surprisingly little code.

Now you also have the possibility to style the chat window however you want.

You can make it look more like Messenger, Discord, or another modern chat application.

Maybe I will cover styling in another video.

For now, this is enough to learn the logic behind PydanticAI and Taipy together.

I hope you learned a lot from this video and see you in the next one.

Bye.
