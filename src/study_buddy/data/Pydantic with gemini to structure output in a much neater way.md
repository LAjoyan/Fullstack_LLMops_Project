# Corrected Words / Terms

Hello and welcome to this video where we'll use Pydantic together with Gemini in order to structure the output so that it becomes much more structured than before.

We can get JSON data back and also get back Pydantic model objects, which we can further process in our applications.

I have done a similar video before, but in that video I relied too much on prompting, and there is an issue with that.

Let me show you an example.

Previously we used prompts telling the model not to write markdown backticks and similar formatting. But sometimes the backticks still appeared anyway.

That means we still needed to parse the output afterwards and remove those backticks manually.

This approach is not very robust because the model can generate slightly different outputs each time.

If you want a much more robust solution, you should look at the Gemini documentation.

There is actually a way in Gemini to directly structure the response by supplying a Pydantic model schema.

That is what we will explore in this lecture.

You'll see that this approach is much cleaner and more robust than relying purely on prompting.

Now you can see this is an empty Visual Studio Code repository or folder.

What we start with is an .env file.

Inside it I have placed:

GEMINI_API_KEY

It is very important that you name it this way, or alternatively:

GOOGLE_API_KEY

The reason is that the genai client can automatically detect this environment variable.

That means we don't need to manually import os, use load_dotenv(), call os.getenv(), and then pass the API key manually.

The Gemini client finds it automatically.

Of course, it is still good to learn how to use dotenv and os.getenv() because those are fundamental concepts.

But since Gemini handles this automatically, we will use the cleaner approach.

Let's start now.

I will create a virtual environment and activate it.

Then I install the packages:

uv pip install ipykernel pydantic google-genai pandas

I need:

* ipykernel for Jupyter notebooks
* pydantic for structured schemas
* google-genai for Gemini
* pandas because later I want to demonstrate working with DataFrames

Now let's open a notebook.

I will call it:

structure_gemini_outputs_with_pydantic.ipynb

Change the kernel to the virtual environment and we're ready.

We start with:

from google import genai

Then:

client = genai.Client()

Now let's create a response.

response = client.models.generate_content()

We choose the model:

model="gemini-2.5-flash"

And the prompt:

"List a few Asian soup recipes, a yummy description, and list the ingredients."

Then:

response.text

This is the normal way we have done things before.

You can see that the result is basically markdown text.

It is semi-structured at best.

Now let's see if we can do better.

Previously we might have prompted something like:

Give me fields of:

* recipe_name: string
* description: string
* ingredients: list[string]

and say:

"Do not use markdown."

But again, this still depends too much on prompting.

Instead we will use Pydantic.

We create a schema:

class Recipe(BaseModel):
recipe_name: str
description: str
ingredients: list[str]

Notice that these are Pydantic models.

They are normal Python classes inheriting from BaseModel.

Now we create another response.

The important additions are:

response_mime_type="application/json"

and:

response_schema=list[Recipe]

This tells Gemini exactly which structure we expect.

Now when we run this, we directly get structured JSON.

Very cool.

Even cooler:

response.parsed

returns actual Pydantic objects.

Now we can do:

recipes[0].description

recipes[0].recipe_name

recipes[0].ingredients

Very clean.

Now let's simulate something else.

Let's simulate housing data.

We create another model:

class Home(BaseModel):
price: int
monthly_fee: int
living_area: float
number_rooms: int
type: Literal["apartment", "house"]
address: str

Now let's generate Swedish housing data.

Prompt:

"List 50 apartments and houses in Sweden with their monthly fee, price, living area, number of rooms, address, and type."

We again use:

response_mime_type="application/json"

and:

response_schema=list[Home]

Now Gemini generates structured housing data.

Then:

homes = response.parsed

We can inspect:

len(homes)

We get 50 homes.

Each item is a Home Pydantic object.

For example:

homes[0].price

homes[0].address

Now let's move into pandas.

If we directly do:

pd.DataFrame(homes)

we don't get exactly what we want.

Instead we convert each Pydantic object into a dictionary.

We can do:

home.model_dump()

for each home.

Then:

pd.DataFrame(
[home.model_dump() for home in homes]
)

Now we have a perfect pandas DataFrame.

Very simple.

Now we can filter the data easily.

For example:

cheap_houses = df.query(
'price < 5000000 and type == "house"'
)

Very cool.

And we can export to CSV:

cheap_houses.to_csv(
"cheap_houses.csv",
index=False
)

Now we have structured simulated housing data generated directly from Gemini.

This is extremely powerful.

Compared to the previous video where we relied mostly on prompting, this approach is much more robust because we use Gemini's built-in structured output support.

We used:

* response_mime_type="application/json"
* response_schema with a Pydantic model

This gives us clean validated structured outputs immediately.

Super cool.

I hope that you've learned a lot from this video.

Thank you for watching and see you in the next one.

Bye.
