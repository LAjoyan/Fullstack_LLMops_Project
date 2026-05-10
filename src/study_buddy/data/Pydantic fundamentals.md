# Corrected Words / Terms

Hello and welcome to this video where we'll go into the basics of Pydantic so that we can work with data in an OOP manner.

We'll work with fields, methods, validate data, and we'll output JSON data as well.

In order to show you the power of Pydantic, we'll start with a normal OOP class. Then based on this one, we'll do manual validation to see how that works.

After that, we will move over to Pydantic.

Pydantic is very useful for things such as FastAPI.

But if you are also interested in AI and LLMs, then you'll notice that Pydantic is required and used a lot in order to structure the output.

The output from LLMs is usually very unstructured, and you want to have it in a structured format and validate its output so that you can use it more easily in later stages of your applications.

Let's dive directly into the code.

Here I will start with some setup.

If you have watched many of my videos before, I've usually used uv for package management.

However, I've used it in a more traditional way.

In this video and future videos, I will go into a more modern way of using uv.

To do that, we'll start with:

uv init

This starts a uv project.

You can see there is a main.py file.

Actually, I don't need that, so I will remove it directly.

You can also see the pyproject.toml file.

Here is some description of our project, and here you can see which version of Python I'm using.

Then we do:

uv add

We don't need to activate the virtual environment in order to install things into it, as we did before.

Instead, you just use uv add.

What do we need to add?

I want to add Pydantic and ipykernel since I will be working in Jupyter Notebook.

If I need something else, I will add it later.

uv add pydantic ipykernel

A few things are installed and you can see there is a pyproject.toml file.

Here it shows the dependencies that exist.

You can also see uv.lock, which contains all installations.

Now it's time to get started.

I will clear my terminal and create:

touch pydantic_basics.ipynb

This is my Jupyter Notebook where I will work.

I choose my virtual environment, pydantic_basics.

Change the kernel to Python.

Now I'm ready to start working.

Let's start without Pydantic first.

To start without Pydantic, we create an example class.

class Person:

What should this Person have?

def **init**(self, name: str, gender: str, age: int) -> None:

That is a nice starting point with type hinting.

We assign the parameter values into the instance itself using self.

Remember, when instantiating an object from this Person class, Python injects the instance into the self parameter automatically.

That's why we do:

self.name = name
self.gender = gender
self.age = age

Now let's instantiate a person.

person1 = Person(name="Tion", age=34, gender="male")

If I write person1, you can see that we only get the default dunder repr representation showing the memory address.

However:

person1.name

returns the name.

person1.age

returns the age.

And so on.

This is how we access attributes using dot notation.

Now let's try something strange:

person2 = Person(name=3.1415, gender=True, age=-10)

This works even though it is completely wrong.

Even though we used type hints, Python still accepts these values.

Type hints are only hints.

Python is not a strongly typed language like Java, C#, Rust, or C++.

That means users can still provide incorrect values.

This flexibility is nice, but when building larger and more robust systems, validation becomes important.

Now let's manually validate our Person class.

For example:

if not isinstance(name, str):
raise TypeError(
f"name must be of type string, not {type(name)}"
)

Now if we do:

Person(name=3.1415, gender="male", age=10)

we get a TypeError.

Great.

Let's continue.

Now suppose we create:

person3 = Person(name="Wagner", gender="M", age=-54)

This works, but negative age is incorrect.

We need validation for age as well.

We can validate age like this:

if not isinstance(age, int):
raise TypeError(...)

and:

if not 0 <= age < 125:
raise ValueError(...)

Now negative ages fail.

Great.

However, we still have another issue.

Suppose we create:

person4 = Person(name="Bella", gender="F", age=4)

This works.

But then we do:

person4.age = -5

This also works.

Why?

Because validation only occurs inside **init** during object creation.

Later attribute changes bypass validation.

To solve this we use properties.

We create a getter:

@property
def age(self):
return self._age

and a setter:

@age.setter
def age(self, value):
validation code here

Now whenever we assign:

self.age = age

or later:

person5.age = -3

the setter automatically validates the value.

This works correctly.

But notice how much code we needed just to validate a simple object.

This is where Pydantic becomes extremely useful.

Now let's validate using Pydantic.

We start with:

from pydantic import BaseModel

BaseModel is a class.

By inheriting from BaseModel, our class becomes a Pydantic model.

But remember: it is still a normal Python class.

class Person(BaseModel):
name: str
gender: str
age: int

Now let's create:

person6 = Person(
name="Christina",
gender="female",
age=29
)

Notice that we automatically get a nice representation for free.

We didn't need to implement **repr** ourselves.

We can access fields normally:

person6.age

returns 29.

We can even do:

person6.age = 36

and it works.

However:

person6.age = "30"

also works unexpectedly.

We'll fix that soon.

Let's see validation errors first.

Suppose we create:

Person(name=123, gender=True, age="abc")

We get validation errors immediately.

We can catch them using:

from pydantic import ValidationError

Pydantic tells us exactly which fields failed and why.

Interestingly:

Person(name="Nina", gender="F", age="29")

works because Pydantic coerces the string "29" into the integer 29.

However, we still want validation during assignment.

To do that we use:

from pydantic import ConfigDict

model_config = ConfigDict(
validate_assignment=True
)

Now when we assign invalid values after object creation, validation also occurs.

For example:

person7.age = "30"

now raises a validation error.

Great.

Now let's add validation constraints for age.

We import Field:

from pydantic import Field

Then:

age: int = Field(gt=-1, lt=125)

Now age must be between 0 and 124.

We can also validate gender more strictly using Literal.

from typing import Literal

gender: Literal["M", "F"]

Now values like "female" fail validation.

This is extremely useful when working with APIs and structured outputs.

Now let's talk about serialization and deserialization.

Serialization means converting a Python object into JSON.

Deserialization means converting JSON back into a Python object.

This is very important in APIs because APIs send data as JSON.

Suppose we have:

person7

We can do:

person7.model_dump()

This gives us a dictionary.

Then we can save it as JSON using json.dump().

Now we have written JSON to a file.

To deserialize:

Person.model_validate_json(json_data)

This converts the JSON string back into a Python object.

Very cool.

Pydantic allows serialization, deserialization, and validation with very little code.

This is one reason why FastAPI is built heavily around Pydantic.

It is also heavily used in AI applications and LLM frameworks because LLM outputs are often unstructured.

Pydantic helps structure and validate that data.

This is the foundation of many modern Python systems.

I hope this was helpful for you.

There is another video where I use Pydantic together with an API using the Pokémon API.

Take a look at that as well so you can learn how to validate data coming from APIs.

Later on I also have many FastAPI videos where Pydantic plays a very large role.

And of course, Pydantic together with LLMs, especially Gemini because they have a really nice free tier.

Thank you for watching this video and see you in the next one.

Bye.
