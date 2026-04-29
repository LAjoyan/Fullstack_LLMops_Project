# Python\_oop\_1

**kokchun:** [00:00:00] Hello and welcome to this lecture where we'll come into OOP, Object Oriented Programming in Python. In this lecture we'll go through classes, we'll go through instances, attributes, docstring, type hint, and much more. And in the optional parts there's also encapsulation and properties. With this I would like to go immediately to Visual Studio Code.

So here I am in Visual Studio Code. I have my virtual environment set up. I'm using UV. So if you don't know how to do that, look at my previous videos, how to set it up. And now I have a Jupyter notebook as well. So here's Python Fundamentals Part 3. So this is the OOP part. So starting with the class. So you can see a class as,~~ uh,~~ a type of blueprint.

And from the class you can instantiate,~~ uh,~~ instances, right? ~~Uh, ~~so [00:01:00] let's create a class now. Class,~~ uh,~~ class,~~ uh,~~ let's see. ~~I've, ~~I've written this in,~~ uh,~~ Swedish actually. ~~Uh, ~~in, ~~uh. ~~I've written this in Swedish, but,~~ uh, the, ~~the name, Antagning,~~ uh,~~ I could call it the admission,~~ uh,~~ admission.~~ So, ~~so this is a class which has an initializer.

So def dunder init, let's see, def dunder init. And this initializer, this is the code that will be run,~~ uh,~~ when, whenever we instantiate from this class. So when we instantiate from this class, we get an instance, then this code will run first. The code inside of the dunder init. And it's called dunder when you have two underscores here.

Before and two underscores after. ~~Uh, ~~which there's a special type of method called dunder init. So it has a special [00:02:00] meaning with it. There's a lot of other dunder methods. They are written in this way. So we have self as an input, so you send in the instance itself. And we use school as another input, a program.

We have name, we have a set as an input. So these are inputs,~~ uh,~~ input arguments to this class, to this in, this dunder init method, okay? So then, I would like to,~~ uh,~~ I would like to do self. school equals to school. And what does this mean? ~~Well, ~~it means that when we initialize, when we instantiate this class,~~ uh,~~ we instantiate an object from this class, we put in an argument [00:03:00] for school, and then we give an attribute to this instance.

That's called self. school. So self is the object instance itself, right? And this instance has an attribute called school. So this is how it works. ~~And, ~~and ~~we, ~~we give it the value school. And then I'll do self. program. Program equals to program. And I do self. name equals to name. Self. asset equals to asset.

Help me. So basically like this. So what does this mean? ~~Well, ~~let's create some students from this student one equals admission. We call it [00:04:00] cool school. We say the program is AI. And then note that these two are positional arguments. And now I use,~~ uh,~~ just to show that we can, I'll pass in some,~~ uh,~~ I'll pass in some keyword arguments as well, and I don't need to put them in order when I do keywords argument.

So asset because true name equals auction. And,~~ uh,~~ yeah, that is it. So then we have student one. I run this one. Okay. When I run this, what happens? We have something here. dunder main dot admission at. Some kind of hexadecimal memory address. So this is basically how Python denotes an instance of a class. So you have an instance, and so it's in the done domain, [00:05:00] and it's,~~ uh,~~ it's called dot admission at some kind of memory address.

So this means that this instance lives in,~~ uh,~~ it's somewhere here, some, it lives in this,~~ uh,~~ Address, zero x 1 0 3 something. And what is written out here is actually this clause default done, the wrapper method. We'll come into ~~done, ~~done the wrapper a little bit later,~~ uh,~~ and I'll show you how that works in order for you to override this,~~ uh,~~ default value here.

So let's create a new code. Let's do student. Equals to admission of cooler school. Now the school here, we let you go into data science and a set equals balls. Yeah. And your name is war board. [00:06:00] That's the cool name. Okay. Student 2. Oh, you're also an instance living in a certain memory address, but they are not the same memory address, right?

So we have 10 in the end here. We have 90 here. I'll actually increase this one a little bit so that it's easier for you to follow.~~ Uh, ~~I close this down and I will put this down as well like this. Okay. So let's move on. ~~We, we, ~~we try to use student one. We can take out the program, for example, program AI, right?

Student one dot name. Coction student one dot [00:07:00] accept true. Okay. ~~So, ~~so you can see in order for us to get the attributes we have, we use the instance name. So remember that we have an instance here.~~ Uh, ~~let's see. So student one refers to this one. So we instantiate that.

So here student one is here. So we instantiated student one as an admission instance. So it's an instance of this class admission ~~with these, ~~with these properties here

~~or, ~~or these attributes. So then,~~ uh,~~ in order for us to get those attributes, we use the dot notation here. So we have student one dot program, then we get the. It's [00:08:00] program attributes. Student one dot name. We get the name attribute student one dot a set. We get the set attribute, right? So moving on here, we could do student to

student to dot name. Goreboard student to dot. I said false.

Okay. So now we have. We could actually change these attributes on the fly. So it means that when we're running, when we can't change it after we have instantiated an object or instantiated an instance of this class. ~~So, ~~for example, I could do it like this. This is student two dot. Program. I can change it to something else.

I changed it to [00:09:00] UX. So then if I do student to program and I get UX, right? So now it's overwritten the old one. So let's do like this.~~ Uh, ~~we will check out,~~ uh,~~ we'll go in a little bit about that. We can check the memory addresses so we can do ID of. Student one, and this is the id. And usually they're represented with HEXA decal.

So we do HEXA decal. So this is the memory address, right of student one and hex of ID of student two. You can see there. different memory addresses. Here, 10, 35, 1. 10, 35, E. Okay, great. They're [00:10:00] different.

Okay, so now we have checked the memory addresses, so we can go into the Dunder wrapper, which I talked about before. So dunder wrapper, actually, I think, yeah, this one gives a bold text. So we need to underscore here for the markdown syntax like this and escape white to make it into Python cell. So this is dunder wrapper.

~~Uh, ~~so it's spelled out. Let's see. Dunder wrapper. This is ~~how, ~~how you,~~ uh,~~ how you read it out. And this is a, what is this? This is a method for ~~representing an object, ~~representing an object or an instance. So usually in, usually I use the word instance, but you could use object as well.~~ Uh, ~~so basically,~~ uh,~~ this represents an object.

~~Uh, ~~so you could,~~ uh,~~ for example, if I write,~~ uh, uh, ~~I can do like this. I will copy, [00:11:00] I will go up, I will copy this one.

So this is the admission. And if we have, for example,~~ uh,~~ I will have student three here.~~ Uh, ~~admission of cool school.~~ You know, ~~Haskell. And your name is Ada Lovelace. And you have been admitted true. So student 3. So you see there's an, this is the wrapper. So similar as before. But we can now override the default wrapper.

So def done the wrapper.~~ Uh, ~~so what I want to do is return a va a certain value. I want to return a string, so I'll do an f string. Admission of school equals [00:12:00] to,~~ uh,~~ equals to 12

school, comma,~~ uh,~~ let's see, comma program. equals to self. program, comma,~~ uh,~~ name equals to self. name, comma,~~ uh,~~ accept equals to self. accept, like this. So why do I do like this? When I run this one, you can see now this is my wrapper. admission school equals cool school program equals Haskell etc. So this is actually a string cool school is a string so I want to show that this is a string.

I'll do a quote here. I'll do quote, [00:13:00] I'll do ~~quote, ~~quote. Name is also a string so I'll do quote there also. A set is a boolean so I want to quote there. Okay. Much better. Actually, I could,~~ uh,~~ I could clean it up a little bit more, but yeah, because I started doing that, I will continue doing that. Okay, like this.

So basically we've done the wrapper. You want to show to other,~~ uh,~~ other developers and also to yourself,~~ uh,~~ how you would use this class. So that's why I've written with the class I've written out this,~~ uh,~~ this,~~ uh,~~ particular instance, it's,~~ uh, uh, ~~it's,~~ um,~~ that's, it's,~~ uh,~~ attributes and, or it's,~~ uh,~~ parameters, arguments that have been used together with the parameters.

~~So, ~~so this is the done, the rapper,~~ uh,~~ however. So the wrapper is [00:14:00] represented in GPT notebook when you just write it out like this, student3. But you could do wrapper of student3, and you'd get the same result here. And also you could do string of student3, and you'd get the same result. How come? ~~Well, ~~the string actually finds a value.

It looks for a, dunder method called dunder str. However, if dunder str is not implemented, then it will default to the dunder wrapper. So this is quite good to know whenever you're working with Python's normal~~ Uh, ~~ functions,~~ uh,~~ and you can see that,~~ uh,~~ you will notice, , how,~~ uh,~~ it's a wrapper ~~and, ~~and string works.

Okay, so moving on, we'll come into some documentation. So working with,~~ uh,~~ working in a team and you're making classes, it's very important that you [00:15:00] document them. So let's go into documentation. And in documentation, there's something called doc string, and there's something called type hinting. So these are two concepts that are really good to know.

So let's do that. So class student, so I create a new class now, student, and I will have depth under init,

name, string, age, colon, int. So this is type hinting. Active pool. It returns none.

So this is the under init method. So if you look into this one,~~ uh,~~ let's see, I'll show you soon. I'll do self. name equals name, self. h equals h, self. [00:16:00] bool equals bool like this, or no, not equals bool, self. ~~uh, uh, ~~active equals active, and I will have a wrapper as well than the wrapper.

So I'll return string, return. fstring student.~~ Uh, ~~actually, maybe I could do like this, or no, I need to do that like that. Name equals to self dot name. Age equals self dot age. Active equals self dot active. I'll have a this enclosed in single quotes. [00:17:00] Okay. So if I want to create a student instance, so look here what I'm doing, I'm just hovering over it and we get name as a string, h as an int, active as a bool.

Okay. So this helps me as a developer and it helps other as developers To use miss to use this class. So then I know that name must be a string. So for example, here, we could have go over board. You are 55 and it's true that you're active as one. Yeah. ~~The, ~~the naming of this,~~ uh,~~ process and instances are not really good or classes are okay, but the instance is not very good, but here you can see ~~the, the, ~~the ripper here.

So [00:18:00] you can see how useful this type hinting is. So let's continue now.

You can actually do like this. Whenever you're working with classes, you can,~~ uh,~~ you can,~~ uh,~~ create a documentation by using an LLM such as ChatGPT. So for example, I could do like this. I could copy this one I move on to chat GPT,

I'm going to chat GPT here and I'll type,~~ uh,~~ give me a doc string,~~ uh,~~ of the following. Oh, add some examples and make it readable.[00:19:00] 

Okay. So then I get a doc string here.

Okay, so I can ~~copy, ~~copy back this code, close it down,

paste it in. Okay, you can see there's a lot of code here and it seems to be quite hard to,~~ uh, uh, ~~a little bit hard to read whenever you're working with the code, right? However, you can,~~ uh,~~ you can close it down like this using this for elapsing it. So you could ~~elapse it, ~~elapse it, and you can see your code here.

There's probably some kind of hotkey for elapsing,~~ uh,~~ collapse, collapsing this. However, let's look at what ChatGPT has generated for us. So some kind of description of our class, so represents a student with a name, age, and active status. Attributes. And these [00:20:00] are attributes. They have name as a string, age as a string, active as a bool, and some description.

Okay, right now this is quite simple class, so it does it quite well. So active status of the student, e. g. enrolled or not. Okay. ~~Uh, ~~actually this is,~~ uh,~~ not what I wanted. So active status of the students,~~ uh,~~ EG enrolled or not,~~ uh,~~ means,~~ uh,~~ for example, for my student case, maybe I would like to, if they take,~~ uh,~~ if they,~~ uh,~~ participate in class

Like this, for example,~~ uh,~~ so ~~I, ~~I as a domain,~~ uh,~~ I had domain knowledge of my class, so I know it better than chat GPT that does it,~~ uh,~~ that this,~~ uh,~~ Jen,~~ that,~~ that,~~ uh,~~ that can come up with general solutions. ~~So, uh, be, ~~be [00:21:00] aware that you need to change it so that it adapts for you. ~~Right? ~~It shows some methods, it shows different examples,

and you can, so it's also, you use three,~~ uh,~~ strings,~~ uh,~~ three quotes in order to do multiline strings. And you do it in, you write it in the beginning of the class. So this is the documentation of the class. So it's the doc string. And then you can document each,~~ uh,~~ method. So down there in it. than the wrapper, right?

So this is a complete doc string. ~~Uh, ~~we, you might need to change it a little bit for adapting,~~ uh,~~ for you,~~ uh,~~ for your case, however, what can you do with this? ~~Well, ~~if I write, for example, student and a hover over it, you can see here's the documentation [00:22:00] initializes a new student instance, some arguments.

And this is for the type hinting, right? Okay. So also you could do health of student. And you can see this is the documentation that we wrote. So you see student represents a student attributes, methods and examples, right? Of how to use this,~~ uh,~~ this,~~ uh,~~ this student. So cool. We have generated some documentation for our,~~ uh,~~ our student class.

~~So, ~~but whenever they are writing more custom,~~ uh,~~ classes that are not. As general as this one, it's,~~ uh,~~ much better to write your own documentation than to use chat GPT and also make sure if you are working inside a company, if,~~ uh,~~ if they, their policy allow you to just put this into an LLM or in that case, which LLM, et cetera, and [00:23:00] also ~~you, ~~you may, and also ~~if, ~~if it's,~~ uh,~~ some very.

Custom class that you're using for your particular application. Maybe this LLMs will be totally wrong. So make sure that you write your own documentation. And also, but you could follow this structure. The structuring is quite good with the attributes, the methods, the different examples. So it's good structure.

Great! So in the lecture notes, I also have encapsulation and private attributes. It's quite good to know them, but I will skip it for this particular class. So I,~~ you,~~ you should look into this,~~ um, uh, ~~lecture in, in,~~ uh,~~ you should look into the lecture note yourself.~~ Uh, ~~so I will skip the properties and skip the private attributes.

And,~~ uh,~~ and this is [00:24:00] actually the end of,~~ uh,~~ this,~~ uh,~~ OOP lecture. ~~So, uh, ~~good that you have followed along and,~~ uh,~~ I hope that you learned,~~ uh,~~ how to use different attributes, different methods. Actually I've shown just,~~ uh,~~ the Dunder methods, but you could, there is, you could use do methods for basically anything.

So you can see ~~it's, ~~it's a function that is bound to the class. That's basically what the method is. And you've seen a little bit ~~how, how, ~~how you instantiate classes, et cetera. So this is meant to be an introduction to OOP, so it's not nothing fancy. We'll keep it for some future lecture where I'll go into more,~~ uh,~~ more,~~ uh,~~ advanced OOP.

Yes, but,~~ uh,~~ thank you for watching this video and see you in the next one. Bye.

