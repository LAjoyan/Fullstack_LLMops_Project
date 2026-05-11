# PydanticAI fundamentals - outputting structured pydantic model

Hello and welcome to this video on PydanticAI fundamentals.

I've been waiting to make this video.

This is a very nice framework for working with agents, LLMs, chatbots, RAGs, and structured AI applications.

One of the most important parts of working with LLM APIs is getting structured output.

Without structured output, the responses are not very useful for real applications.

PydanticAI is developed by the team behind Pydantic.

If you have followed my videos before, you know how much I like Pydantic.

Pydantic makes Python much more structured and pleasant to work with.

Let's move directly into the code and see how to get started with PydanticAI.

Here I am in Visual Studio Code.

Let's start with:

uv init

Then remove main.py because I don't need it.

Next install packages:

uv add pydantic-ai ipykernel

Good.

Now let's create a notebook:

pydantic_model.ipynb

I will call this:

construct_pydantic_model_from_text_input

Text input from LLMs is usually unstructured.

The goal is to make it structured using Pydantic.

Now change the Python environment to the PydanticAI environment.

Since I will use Gemini inside PydanticAI, I choose Gemini as the model.

Create a .env file.

Inside it:

GOOGLE_API_KEY=your_api_key

I won't show the actual API key.

Now let's get started.

Import:

from pydantic_ai import Agent

Then create an agent:

agent = Agent(
"google-gla:gemini-2.5-flash"
)

Now let's run a simple prompt.

result = await agent.run(
"Give me an IT employee working in Sweden. Keep it short."
)

Then inspect:

result.output

We get something like:

"Elara Nielsen, DevOps Engineer in Stockholm, Sweden."

Nice.

But this output is still unstructured.

Now let's make it structured.

Import:

from pydantic import BaseModel, Field

Create a model:

class EmployeeModel(BaseModel):
name: str
age: int
salary: int = Field(gt=30000, lt=50000)
position: str

Now rerun the agent:

result = await agent.run(
"Give me an IT employee working in Sweden.",
output_type=EmployeeModel
)

Now the result becomes structured.

result.output

returns an actual EmployeeModel object.

Very cool.

Now we can do:

employee = result.output

employee.name

employee.age

employee.position

This is much cleaner than parsing strings manually.

Since this is a Pydantic model, we can also do:

employee.model_dump()

to get a dictionary.

Or:

employee.model_dump_json()

to get a JSON string.

We can even format it nicely using indentation.

Now let's generate several employees.

result = await agent.run(
"""
Give me 10 employees in AI and data engineering fields.
Salary must be between 30000 and 50000.
""",
output_type=list[EmployeeModel]
)

Now:

employees = result.output

We get a list of EmployeeModel objects.

Check:

len(employees)

returns 10.

Now we can loop through them:

for employee in employees:
print(employee.name, employee.salary)

Very cool.

Now let's create a more advanced nested model.

For example a CV or resume model.

Create:

class ExperienceModel(BaseModel):
title: str
company: str
description: str
start_year: int
end_year: int

Then:

class EducationModel(BaseModel):
title: str
education_area: str
description: str
school: str
start_year: int
end_year: int

Then:

class CVModel(BaseModel):
name: str
age: int
experiences: list[ExperienceModel]
educations: list[EducationModel]

Now let's generate a Swedish person applying for a data engineering position.

result = await agent.run(
"Create a Swedish person applying for a data engineering position.",
output_type=CVModel
)

Now:

resume = result.output

We can inspect:

resume.name

resume.age

resume.experiences

Each experience is itself an ExperienceModel.

For example:

resume.experiences[0].title

returns something like:

"Data Engineer"

This is already very powerful.

Now let's do some optional post-processing.

I want to load this into DuckDB.

Install:

uv add dlt duckdb

Then import dlt.

Create a pipeline:

pipeline = dlt.pipeline(
pipeline_name="resume_json_duckdb",
destination="duckdb",
dataset_name="staging"
)

Then run:

pipeline.run(
data=[resume.model_dump()],
loader_file_format="jsonl",
table_name="cv_entries"
)

Now the data is loaded into DuckDB.

Next connect to DuckDB:

import duckdb

Then:

duckdb.connect("resume_json_duckdb.duckdb")

Now we can inspect the generated tables.

DLT automatically normalizes nested JSON data into relational tables.

We get tables like:

* cv_entries
* cv_entries__educations
* cv_entries__experiences

This is very cool.

Now we can query them.

For example joining the parent table with education and experience tables.

DLT creates:

* _dlt_id
* _dlt_parent_id

which allow relational joins.

Now we can load the query into pandas DataFrames and inspect it easily.

This demonstrates how powerful structured outputs are.

Instead of receiving raw text from an LLM, we receive validated structured Pydantic objects.

Afterwards we can:

* serialize them
* store them
* load them into databases
* query them
* join them
* process them further

Of course, for nested document-style data, a NoSQL database like MongoDB may also be suitable.

But the important point is:

We converted unstructured LLM text into structured Pydantic models using PydanticAI.

That is the real power here.

In the next video we will continue using PydanticAI together with FastAPI to build actual APIs and API endpoints.

This is super cool.

Thank you for watching and see you in the next video.

Bye.
