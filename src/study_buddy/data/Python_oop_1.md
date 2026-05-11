# Python_oop_1

Hello and welcome to this lecture where we'll come into OOP, Object-Oriented Programming in Python.

In this lecture we'll go through:

* classes
* instances
* attributes
* docstrings
* type hinting
* and much more

And in the optional parts there's also encapsulation and properties.

With this, I would like to go immediately to Visual Studio Code.

So here I am in Visual Studio Code. I have my virtual environment set up. I'm using uv. So if you don't know how to do that, look at my previous videos on how to set it up.

And now I have a Jupyter Notebook as well. So here's Python Fundamentals Part 3. So this is the OOP part.

Starting with the class.

You can see a class as a type of blueprint. And from the class you can instantiate instances, right?

So let's create a class now.

Class admission.

Actually, I've written this in Swedish. The name “Antagning” means admission.

So this is a class that has an initializer.

So:
def **init**()

And this initializer is the code that will run whenever we instantiate from this class.

So when we instantiate from this class, we get an instance, then this code will run first — the code inside of the dunder init.

And it's called “dunder” when you have two underscores before and two underscores after.

This is a special type of method called dunder init. It has a special meaning. There are a lot of other dunder methods as well. They are written in this way.

So we have self as an input, so you send in the instance itself.

And we use:

* school
* program
* name
* accepted

as inputs.

So these are input arguments to this dunder init method.

So then I would like to do:

self.school = school

And what does this mean?

It means that when we instantiate this class — when we instantiate an object from this class — we put in an argument for school, and then we give an attribute to this instance that's called self.school.

So self is the object instance itself, right?

And this instance has an attribute called school.

So this is how it works.

And we give it the value school.

Then I'll do:

* self.program = program
* self.name = name
* self.accepted = accepted

Basically like this.

So what does this mean?

Let's create some students from this.

student1 = admission(
"Cool School",
"AI",
accepted=True,
name="Kokchun"
)

And note that these two are positional arguments.

And now I use keyword arguments as well, and I don't need to put them in order when I use keyword arguments.

So accepted=True and name="Kokchun".

Then we have student1.

When I run this, what happens?

We have something here:
**main**.admission at some kind of hexadecimal memory address.

So this is basically how Python denotes an instance of a class.

So you have an instance, and it's in the **main** domain, and it's called admission at some memory address.

This means that this instance lives somewhere in memory at this address.

And what is written out here is actually this class's default dunder repr method.

We'll come into dunder repr a little bit later, and I'll show you how that works in order for you to override this default value here.

So let's create a new code cell.

student2 = admission(
"Cool School",
"Data Science",
accepted=False,
name="Warboard"
)

Okay.

student2 is also an instance living in a certain memory address, but they are not the same memory address, right?

So let's move on.

We try to use student1.

We can take out the program, for example.

student1.program → AI

student1.name → Kokchun

student1.accepted → True

So you can see that in order for us to get the attributes, we use the instance name.

Remember that we instantiated student1 as an admission instance.

So student1 is an instance of this class admission with these attributes.

In order for us to get those attributes, we use dot notation.

So:

* student1.program gives the program attribute
* student1.name gives the name attribute
* student1.accepted gives the accepted attribute

Right?

Moving on:

student2.name → Warboard

student2.accepted → False

Okay.

Now we can actually change these attributes on the fly.

So it means that after we have instantiated an object, we can still change its attributes.

For example:

student2.program = "UX"

Then if I do:
student2.program

I get UX.

So now it has overwritten the old value.

Now let's check the memory addresses.

We can do:
id(student1)

And usually they are represented in hexadecimal.

So we do:
hex(id(student1))

And:
hex(id(student2))

You can see they are different memory addresses.

Great.

Now we have checked the memory addresses, so we can go into dunder repr, which I talked about before.

So dunder repr is a method for representing an object or an instance.

Usually I use the word instance, but you could use object as well.

So basically this represents an object.

For example, I will create student3.

student3 = admission(
"Cool School",
"Haskell",
name="Ada Lovelace",
accepted=True
)

student3

So you see the repr similar to before.

But we can now override the default repr.

So:

def **repr**(self):

I want to return a string.

So I'll do an f-string.

return f"admission(school='{self.school}', program='{self.program}', name='{self.name}', accepted={self.accepted})"

When I run this one, you can see now this is my repr.

So basically with dunder repr, you want to show other developers — and also yourself — how this class is represented.

So that's why I've written out this particular instance with its attributes and arguments.

The repr is represented in Jupyter Notebook when you just write:
student3

But you could also do:
repr(student3)

and you'd get the same result.

And also:
str(student3)

and you'd get the same result.

How come?

Well, str actually looks for a dunder method called **str**.

However, if **str** is not implemented, then it will default to the dunder repr.

So this is quite good to know whenever you're working with Python functions and classes.

Okay, so moving on.

We'll come into documentation.

When working in a team and creating classes, it's very important that you document them.

So let's go into documentation.

In documentation, there's something called:

* docstrings
* type hinting

These are two concepts that are really good to know.

So let's do that.

class Student:

def **init**(
self,
name: str,
age: int,
active: bool
) -> None:

So this is type hinting.

Then:

self.name = name
self.age = age
self.active = active

And I will have a repr as well.

def **repr**(self) -> str:

return f"Student(name='{self.name}', age={self.age}, active={self.active})"

If I want to create a student instance, look here what I'm doing.

I'm hovering over it and we get:

* name as a string
* age as an int
* active as a bool

This helps me as a developer and it helps other developers use this class.

So then I know that:

* name must be a string
* age must be an int
* active must be a bool

For example:

student1 = Student(
"Warboard",
55,
True
)

The naming here isn't really important — the point is the structure.

You can see how useful this type hinting is.

Let's continue now.

Whenever you're working with classes, you can create documentation by using an LLM such as ChatGPT.

For example, I could copy this class and go into ChatGPT and type:

“Give me a docstring for the following code. Add some examples and make it readable.”

Then I get a docstring.

You can paste it back into your code.

You can also collapse sections in VS Code to make the code easier to read.

Let's look at what ChatGPT generated for us.

We get some kind of description of our class:

“Represents a student with a name, age, and active status.”

Then:

* attributes
* methods
* examples

Right now this is quite a simple class, so it does it quite well.

For example:
“active status of the student, e.g. enrolled or not.”

Actually, this is not exactly what I wanted.

For my student case, maybe active means whether they participate in class.

So I as the domain expert understand my class better than ChatGPT, which generates more general solutions.

So be aware that you need to change the documentation so that it adapts to your own use case.

It also shows examples.

You use triple quotes in order to create multiline strings.

And you write it in the beginning of the class.

So this becomes the documentation of the class — the docstring.

Then you can document each method:

* **init**
* **repr**

This is a complete docstring.

You might need to change it a little bit to adapt it to your own case.

What can you do with this?

If I write Student and hover over it, you can see the documentation:

* initializes a new student instance
* arguments
* examples

And this works together with the type hinting.

You could also do:
help(Student)

And you can see all the documentation that we wrote.

So cool — we have generated documentation for our Student class.

Whenever you're writing more custom classes that are not as general as this one, it's much better to write your own documentation than to rely completely on ChatGPT.

Also make sure that if you're working inside a company, their policy allows you to paste code into an LLM.

And if it's a very custom class for your application, the LLM might be totally wrong.

So make sure that you write your own documentation.

But you can still follow the structure:

* attributes
* methods
* examples

It's a good structure.

Great.

In the lecture notes I also have:

* encapsulation
* private attributes

These are good to know, but I will skip them in this lecture.

You should look into the lecture notes yourself.

So I will skip:

* properties
* private attributes

And this is actually the end of this OOP lecture.

I hope that you learned:

* how to use attributes
* methods
* dunder methods
* how to instantiate classes

This is meant to be an introduction to OOP, so nothing too advanced yet.

We'll keep the more advanced OOP concepts for future lectures.

Thank you for watching this video and see you in the next one.

Bye.
