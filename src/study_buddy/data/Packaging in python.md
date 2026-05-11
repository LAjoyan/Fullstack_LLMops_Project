# Corrected Words / Terms

Hello and welcome to this lecture where we'll go into packaging a Python project.

As you will see, packaging a Python project will make importing much simpler because as you might have noticed, when you're importing modules from different folders, it might give you troubles in Python.

However, when you have packaged it, you can pip install it. And when you have pip installed it as a package, it is very intuitive to use the modules that you have created.

So we will create a real application here called the Travel Planner that will use an API.

As you will see, this application contains a lot of different modules separated into different directories. And this is kind of the idea, so that you can see that when you're growing a larger and larger project, you really should package it.

We will move on to Visual Studio Code.

So in a previous lecture, you have already seen me working with the Trafiklab API. So I won't go through that again. Instead, you can go there and look at my previous lecture.

I'll just create a new terminal.

Let's start by creating a virtual environment.

uv venv

So now we have a virtual environment.

Let's activate that.

source .venv/bin/activate

Okay. It has been activated and you can see that from the parentheses, but it's not always certain that the parentheses are there.

It depends on how your terminal is configured. Sometimes it might not be there. Then you can use echo to check that you are inside the virtual environment.

echo $VIRTUAL_ENV

If you type this, you should get something with .venv here.

If this is empty, then you're not in a virtual environment. It is as simple as that.

Okay, so I will clean this terminal and let's move on.

Let's start creating some folders.

mkdir backend frontend utils

Now we have three folders.

Going into the backend first, I will create:

touch backend/connect_to_api.py

So here I have created this Python module.

Let's create another one:

touch backend/trips.py

Then in frontend:

touch frontend/dashboard.py

touch frontend/plot_maps.py

Actually, I accidentally put them outside, but they should be inside the frontend folder.

So let's move them.

mv plot_maps.py frontend/plot_maps.py

mv dashboard.py frontend/dashboard.py

So I basically just moved these two.

In utils, I will create constants.py.

touch utils/constants.py

And also another directory called tests and an explorations directory.

Okay, now you can see that this project is already growing.

But the scripts are empty right now.

Let's create something more.

touch explorations/exploring_travel_planner.ipynb

In utils I also want a run_dashboard.py.

Now you can see that we have created the same kind of skeleton for this project.

Usually I don't have all of this in my mind directly when creating a project, so I don't create the entire structure from the start.

Instead, I create some skeleton parts like backend, frontend, utils, explorations, and tests.

These folders are a very good starting point.

Let's continue.

I will also have an .env file.

touch .env

Inside the .env file you should put your API credentials.

So I will pause this video and come back.

Okay, I've placed my API key into my .env file and now I will copy and paste the code from the lecture notes.

Actually, in the lecture note I didn't have:

if **name** == "**main**":

But I will have that and test that it works.

When I'm running this one, you can see that it works.

I get the data.

So it is just using this method.

I'm creating an instance from this ResRobot class and from this instance I use the method timetable_arrival().

This method basically goes into an endpoint with a default location ID and returns the timetable for that location.

You already know from the last lecture how to obtain the location ID for a particular location, so I won't go through that.

Instead, you can just see that it works.

Now let's go into trips.py.

I want to do:

from connect_to_api import ResRobot

because I want to use that class.

Then:

resrobot = ResRobot()

and:

resrobot.timetable_arrival()

When I run this one, we get data and it works.

Importing from a sibling module is usually no problem.

However, what if I'm inside dashboard.py and want to get something from trips.py or connect_to_api.py?

How do we do that?

If I try:

from backend.connect_to_api import ResRobot

and then:

print(ResRobot.timetable_arrival)

and run this one, we get an error.

ModuleNotFoundError: No module named 'backend'

How do we solve this?

One way is to use sys.path.append() and append different paths manually.

Another way is to set the PYTHONPATH.

But neither is really recommended for larger projects.

The best way is to package the project.

In order to package this, we need to add a file called **init**.py inside our folders.

So for each folder we should add:

**init**.py

Actually, for Python 3.3 and forward you technically don't need this, but because I'm using find_packages() later, we do need them.

So I create **init**.py in:

* backend
* frontend
* utils
* tests
* explorations
* root folder

I will also create setup.py.

This is very important because setup.py contains the metadata for your package so that it can be installed with pip.

Inside setup.py:

from setuptools import setup, find_packages

Let's start by printing:

find_packages()

When running this, you can see that it finds frontend, explorations, tests, utils, and backend.

Basically, it finds every folder containing **init**.py.

If I remove **init**.py from utils and run again, utils is no longer found.

So for consistency I also add **init**.py to explorations and tests.

However, tests and explorations should not be importable by the user.

So we use exclude:

find_packages(exclude=("tests*", "explorations"))

Now only frontend, backend, and utils are found.

Great.

Now we package them using setup().

We need:

* package name
* version
* description
* author
* author email
* install_requires
* packages

For example:

name = "travel_planner"

version = "1.0.0"

description = "This package is used for travel planning in public transport in Sweden. It contains backend code, frontend code, and utils."

install_requires includes:

* pandas
* streamlit
* requests
* folium

Then:

packages=find_packages(exclude=("tests*", "explorations"))

To install the package:

uv pip install -e .

The -e flag means editable mode.

That means when I change my code, the installed package updates automatically.

Running this installs the package and all dependencies.

We can verify using:

uv pip show travel_planner

Now backend, frontend, and utils can be imported everywhere inside the virtual environment.

For example:

from backend.connect_to_api import ResRobot

works correctly.

But remember: you must be inside the correct virtual environment.

At one point I accidentally used the global Python environment, which caused ModuleNotFoundError again.

After activating the virtual environment, everything worked.

Now I will paste the real code for the application.

Inside dashboard.py I import streamlit and TripMap from plot_maps.py.

I also import station IDs from utils.constants.

In plot_maps.py I define an abstract base class called Maps.

TripMap inherits from Maps and implements display_map().

The map itself is created using folium and displays station coordinates using longitude and latitude.

Inside constants.py I use enums.

Enums are a special type of class that create collections of name-value pairs.

For example:

StationIDs.MALMO.value

returns the Malmö station ID.

Enums improve readability and type safety.

Inside run_dashboard.py I use subprocess together with pathlib.

I define:

root_path = Path(**file**).parents[1]

Then:

frontend_path = root_path / "frontend"

This lets me locate dashboard.py.

run_dashboard.py launches the Streamlit dashboard.

When I run it, I get a Streamlit app showing train stations between Malmö and Umeå.

You can see the travel time, station names, dates, and times.

Now I want something even cooler.

Instead of manually running:

streamlit run dashboard.py

I want a terminal command called:

dashboard

So inside setup.py I add entry points:

entry_points = {
"console_scripts": [
"dashboard=utils.run_dashboard:run_dashboard"
]
}

After changing setup.py I must reinstall the package again:

uv pip install -e .

Now I can simply type:

dashboard

in the terminal and my dashboard launches automatically.

Super cool.

So in this lecture we went through how to package Python projects.

I haven't gone through all the code in detail because this is the beginning of a much larger project.

The important thing is understanding how packaging simplifies importing modules in larger applications.

Packaging is a very important skill in Python.

Make sure you learn it well because it will elevate your Python skills significantly.

Thank you for watching this video and see you in the next one.

Bye.
