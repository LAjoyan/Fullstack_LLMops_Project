# Python Fundamentals

Hello and welcome to this lecture where we'll go into the most fundamental parts of Python. So this lecture is really good for you if you want to just dive into Python when you have gone into another programming language fundamentals, or you have already studied a Python course and you need some repetition.

So these video lectures are really good for that. And here I will go directly into Jupyter Notebook, which is an interactive coding environment. I will write the code live for you so that you can pause the video and type along and try it out for yourself.

And also if you need, there's a link to the GitHub repository where the code is. And these lecture notes are also more comprehensive with full annotations for you to read and learn from.

Yes, and also there are some parts there that will be optional, which I won't cover, but for you that want to learn more about how Python works, my recommendation is to check out those optional parts as well.

Now let's move on to Visual Studio Code. So here I'm in Visual Studio Code, and I've done File → Open Folder and navigated to this Python Fundamentals folder. You should have a local repository where you have this course, and then you open that repository with File → Open Folder.

I'm here in Python Fundamentals and I start by opening a new file. So this one opens a new file. This one opens a new folder. So I open a new file and I call this Python Fundamentals Part 1.

So Python Fundamentals Part 1.ipynb. And you can see that this is a Jupyter Notebook. And right now I cannot run anything. I can write markdown, so I can do something like this: item and then notes part one. Yes, and when I want to run it, I do Shift + Enter or Ctrl + Enter.

So the difference is with Ctrl + Enter, you just run it. With Shift + Enter, you run it and it jumps into the next code cell.

So you can see here is the marking for the next code cell, right? However, this is in Markdown, so I want to change it to Python. But before doing that, we need to have a virtual environment installed, right?

I open up Terminal → New Terminal. Inside Windows, I recommend you open up Git Bash by doing this: you open up Terminal and then you can choose here Configure Terminal Settings → Select Default Profile and there you can choose Git Bash.

Okay, so here you see there's a mark on 3.11.8. I will deactivate it. And you can see here, this is my starting point. So I have 3.11.8 and you might have 3.12 or 3.13. It doesn't matter here which version you have, as long as you have around 3.8 and over, and we won't go through things that require specific newer versions.

So now let's do this. We need to have a package called uv. So do pip install uv. And for me, it's already installed. You see “Requirement already satisfied.” And for you it should install if you don't have it. And if it doesn't install, then there might be something wrong with your setup of Python and the paths.

So it's very important that the paths to pip and the paths to Python, the correct Python version, are in your system. If it's not, then you should check out the video on setting up Python and figure out how you can set it up properly.

Okay, so here I have it installed so I can write uv venv. And what you can see is that it creates a virtual environment here and it says, “Okay, we noticed a new environment has been created. Do you want to select it for the workspace folder?”

I will say no because I want to do it manually myself so that I have full control. So you can see here it says activate with source .venv/bin/activate. So let's do that.

So source .venv and then I can do tab autocomplete and then I will do tab and you can see there are these folders here and I'll choose bin.

So b + tab and a + tab. If you're in Windows, it's not bin. Instead, it's called Scripts. So big S C R I P T S. I'll show you how it looks. So this is for Mac and Linux. For Windows, you have to type like this.

So if I do that, it doesn't work because I'm on Mac obviously. So here I will clear my terminal. I do that with Command + K. You can also clear it by typing clear. In Windows you need to type clear, but on Mac you can do Command + K.

And you can see here Python Fundamentals. This is this project's folder, and it's marked with parentheses. So it means that this virtual environment is activated.

Okay, what is a virtual environment? A virtual environment is an isolated environment where you will install your packages for this particular project. So you don't want the packages that you install to disturb each other.

For example, one package might be dependent on another package. And if you are working on several different projects with global installations, then there might be problems with package mismatches, etc.

And also there will be a problem if you want to share the code with a teammate. What you always want to do is isolate your packages within a virtual environment.

And there are several types of virtual environments. There's Python's default venv, and there's for example pipenv, poetry, conda, uv, and many more. However, the one we chose is uv. So that's what we use here.

And to recap, I use uv venv to create the virtual environment. Good. And thereafter, I need to activate it using source .venv/bin/activate, right?

Okay so now it's activated and when you activate it, you can install packages to this virtual environment. So I do uv pip install ipykernel because this one is required in order for you to work with Jupyter Notebook.

That is very important. So this is Jupyter Notebook, it's an interactive shell, interactive environment for working with Python, and you can annotate it, so it's quite useful.

So you see there are a lot of things that are installed here. And we can do uv pip list in order to see them. So this is everything that is installed.

Okay, then the question is: why does it install so many things when I just installed ipykernel? That is because ipykernel depends on all the other packages as well.

So there you see that there are a lot of packages and the specified versions are listed here.

So let's continue now. In Jupyter Notebook, in order for this to work, you need to select the kernel. And you choose the Python environment and you choose .venv here so that you don't use your global Python.

So I use this one. So we see 3.11.8 and .venv. It's okay if you have another version. I've already said that.

So I open a new code cell. And now this is Python here and we have .venv. This means that we can use it now.

So let's start with something. I will print Hello and do Alt + Enter or Option + Enter and you can see that Hello is written out.

I will create a new markdown cell. I mark Python Fundamentals. I will create a new markdown. Then the markdown cell will come right below here.

And here I'll write two hashtags to give me a subsection. And here I'll write input and output.

So inputs and outputs. We want to have things that the user can write, and we want to be able to show things to the user, right?

So print is one type of output. So let's do this:

my_fruit = input()

So this one will take an input from the user and then I will print my_fruit.

And if I run this one, you can see there's an input section here where you can write something and then click enter.

So my fruit is apple, for example, and you can see apple is printed out here.

And also apple is now stored in the my_fruit variable, right?

So if I write my_fruit and run it, you can see that Apple is written out.

And then the thing is: how come Apple is written out when I just run this cell without printing?

That is because Jupyter Notebook has a special feature that will show the last statement automatically.

So the last statement here is my_fruit, and the result of it is shown here as Apple.

However, I want to print this out a little bit nicer, so I will use something called an f-string:

print(f"I like {my_fruit}")

And if I run this one, you can see that it says: I like apple.

So my_fruit is the variable, right? And the variable was specified from the input.

So the input we typed was apple. So apple in this variable will be put here.

So then what it says is “I like apple” instead of “I like my fruit”, right?

So in order to use the variable and print it out using something called an f-string, you have an f here, and then you have quotes, and whatever you write here is the string, the text, and you use curly braces in order to put in a variable.

So that is how f-strings work.

Okay, let's move on now.

We move on to something called data types.
