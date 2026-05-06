# Python fundamentals

[00:00:00] Hello and welcome to this lecture where we'll go into the most fundamental parts of Python. So this lecture is really good for you if you want to just dive into Python when you have gone into another programming language as fundamentals. Or you have already studied a Python course and you would need some repetition.

So these video lectures are really good for that. And here I will go directly into Jupyter Notebook, which is an interactive coding environment. I will write the code live for you so that you can pause the video and type along and try it out for yourself.

And also if you need, there's a link to the GitHub repository where the code is. And these lecture notes are also more comprehensive with full annotations for you to read and learn about.

Yes, and also there's some [00:01:00] parts there that will be optional, which I won't cover , but for you that want to learn more about how Python works recommendation is to check out those parts that are optional as well. 

Now let's move on to Visual Studio Code. So here I'm in Visual Studio Code, and I've done File, Open Folder, and navigated to this Python Fundamentals folder. You should have a local repository. Where you have this course and then you open that repository with file open folder 

I'm here in Python fundamentals and I start with open a new file. So this one starts opens a new file. This ones opens a new folder. So I open a new file and I call this Python Fundamentals part one

so Python Fundamentals, part one IB. And you can see that this is a [00:02:00] Jupyter Notebook. And right now I cannot run anything. I can write the markdown, so I can do like this item and then those part one. Yes, and when I want to run it, 

I do shift enter or control enter. So the difference is with control enter, you just run it with. Shift enter, you run it and it jumps into the next code cell. 

So you can see here is the marking for the next code cell, right? However, this is in Markdown, so I want to change it to Python. But before doing that, we need to have a virtual environment installed, right? I opened up terminal, new terminal, inside of Windows, I should, I recommend you to open up git bash or or so by doing it, you open up terminal and then you can choose here configure terminal [00:03:00] Settings select default profile and there you can choose git bash.

Okay, so here you see there's a mark on 3. 11. 8, I will deactivate. And you can see here, this is my so this is the starting point. So I have 3. 11. 8 and you might have 3. 12 or 3. 13 it doesn't matter here which version you have, as long as you have around 3.8 and over, and we won't go through things that require specific newer versions.

So the fundamentals, so I say this one, and now let's do like this. We need to have a package called uv. So do keep install uv. And for me, it's already installed. You see the requirement already satisfied. And for you it should install if you don't have it. And if it doesn't install, then there might be something wrong with your setup [00:04:00] of Python and the paths.

So it's very important that the paths to pip and the paths to Python, the correct Python version is is in your system. If it's not, then you should check out the video of setting up Python and and figure out how you can set it properly. Okay, so here I have it installed so I can write UV and DENV and what you can see is that it creates a virtual environment here and it says here okay, we notice a new environment has been created.

Do you want to select it for the workspace folder? I will say no because I want to do it manually myself so that I have fully control. So you can see here it says activate with source. vnv slash bin slash activate. So let's do that. So source. v and then I can do tab or autocomplete and then I will do tab and you can see there's [00:05:00] these folders here and I'll choose bin.

So B tab and A tab. If you're in Windows, it's not bin. Instead, it's called script. So big S C R I P T S, I'll show you how it looks like. So this is for Mac and Linux for windows. You have to type like this. This is for windows. Okay. So if I do that, it doesn't work because I'm in Mac, obviously. So here. I will clear my terminal.

I do that with command K. You can also clear it by typing out clear. And in Windows, you need to type out clear. But in Mac, you can do command K. Okay. And you can see here, Titan Fundamentals. This is this project's folder, and it's marked with parentheses. So it means that this virtual environment is activated.

[00:06:00] Okay, what is a virtual environment? A virtual environment is an isolated environment where you will install your packages for this particular project. So you don't want the packages that you install to Disturb each other. For example one package needs required is dependent on another package.

And if you are working several, a lot of different projects in the global installations, then there will be, there might be a problem with packages mismatch, et cetera. And also there will be a problem if you want to share the code with with a teammate. What you always want to do is to isolate your packages within a virtual environment.

And there's several types of virtual environments, and there's Python's default b, e, and v. And there's for example there's PIP ENV, and there's there's Poetry, Conda and and UV, and there's many [00:07:00] more. However, the one we chose is UV. So that's what you use. So we use it here.

And to recap, I use UV VENV to create the virtual environment. Good night. And thereafter, I need to activate it using source. vnv slash vn slash activate, right? Okay so now it's activated and by then here, when you activate it, you can install packages to this virtual environment. So I do uv pip install ipykernel, because this one is required for you in order for you to work with Jupyter Notebook.

That is very important. So this is Jupyter Notebook, it's an interactive shelf, interactive environment for working with Python, and you can annotate it, so it's quite useful. So you see there's a lot of things that are installed here. And we can do UVP list [00:08:00] in order to see them. So this is everything that is installed.

Okay, then the question is, why does it install so many things when I just installed IPyKernel? That is because IPyKernel depends on all the other packages as well. So there you see that there's a lot of packages and the specified version is listed here. So let's continue now with so in Jupyter notebook, in order for this to work, you need to select the kernel.

And you choose the Python environment and you choose vnv here so that you don't use your you don't use your global Python. So I use this one. So we see 3. 11. 8 and vnv. It's okay if you have another version. I've already said that. So I open a new code. And that this is Python here and we have dot VNV.

This means that we can use it now. So let's let's start with something. [00:09:00] I will get the input. I'll start with print. Hello, and do a out, enter or option enter and you can see that hello is written out. So I will create a new markdown. I marked Python fundamentals. I will create a new markdown. Then the markdown cell will come right below here.

And here I'll write two hashtags. Give me a sub, sub section. And here I'll write input and output. So inputs and outputs. We want to have. Things that the user can write, we want to be able to show things to the user, right? So print is one type of output. So let's do like this. My route equals input. [00:10:00] So this one will take an input from the user and then I will print my route.

And if I run this one, you can see there's a input section here where input prompt, where you can write something and then click enter. So my fruit is apple, for example, and you can see apple is printed out here. And also I could now apple is stored in the, my fruit variable, right? So if I write my fruit.

And run it, you can see that Oh, Apple is written out. And then the thing is how come you see that Apple is written out when I just run this cell without printing? That is because Jupyter Notebook has a special feature that that will show the last the last statement. So the last statement here is myFruit, and this one, the result of it is shown here as Apple.

However, I want to print this out a little bit nicer, so I will use something called fstring, so print [00:11:00] myFruit, I will do fstring, and I can say I like myFruit, and if I run this one, you can see that I like myFruit, I like apple, so myFruit, this is the variable, right? And the variable we specified from the input, right?

So the input we typed in apple. So apple in this variable will be put here. So then what it says is, I like apple instead of, I like my fruit, right? So in order now you have, you use the variable and print it out using something called. F string. So then you have an F here, and then you have quote, and whatever you write here is the strings, the text, and you use curly braces here, curly [00:12:00] braces, in order for in order to put in a variable.

So that is how F strings work, right? Okay, let's move on now.

We move on to something called. Data types. Data types. And when I ran shift enter, you can see there's a markdown cell created here. We can change it to the right click here and you can choose Python or you can do a quick, quicker way. You mark this and you type type in escape s and then you type in Y and you can see that it changes the python.

This is a hot key in Jupyter Notebook. Good to know. So here. We can do like this name equals auction. So now I've created a variable which has a string. And and note, if you're in other [00:13:00] languages, you might note that, Oh why didn't we say which type it has? This is because it's dynamically typed.

So the typing is inferred. So Python sees that it's a string, and then it will give the type of name as a string. So for example, if I write out name now, you can see that Ah, there's quotes here, so it's a string and I can also write type of name and you can see that the type is string, right? Or str.

So here we can continue h equals 32. 8. Actually I'm a little bit older now, but my notes says 32. 8 and number of telegram equals one. And lovesMath equals true.

So now I have different variables. I have H that is a float or a [00:14:00] double. So here we have a double and here we have an int and here is a bool. So you can see this is how we do comments here. Okay. And let me type this out. So I will type out H and you can see the H and if I want to have several things that are outputted in the output cell.

I can type in number of children is one, you see there's a parenthesis here, and I will put in love's math equals true. And I can also put in name, which is the variable I got

the variable I got up here. Okay, so if I run this one, you can see, Cogen, 52.8 comma one, comma two. So the reason for this is that we get a top pole, a two pole when we write it like this. And this is what the, what This output in the Jupiter notebook [00:15:00] cell.

So let's move on to f strings. So I've created a new cell here, and I will type in f strings, and I want it to be Python, so I change, or I want it to be Markdown, like this, Markdown, and now we have f strings. So f strings, we have already seen it, so it's we put in variables in the string, so we can use this to look up the different data types as well.

So if you just do type of something, for example, we do type of name, which is the variable we created before, we get string, right? So I can do print of this and I do an X string instead. So it's an interpolated string. So here, let's see, last parenthesis, and we see that It's a class string, so it's different between what we had before if we only type it out type name, and if we do print in a print statement, it's a [00:16:00] little bit different, and that is, that has to do with something, called DunderString, which you will come into later on when you come into OOP.

But here, this is the DunderString, and if you just type it out in Jupyter Notebook, you get something called DunderWrapper, which is the representation, so then that could be a little bit different. So that is a little bit of details, but we don't need to understand it directly. However the most important is that we print it here now so I could type like type of name and I can do like this and we see here type name, it's a class string.

I want to copy this one and continue. So I will do a

shift out down button or shift option down button. So I do it a few times and then we copy this line, right? 

Okay. So instead of name, I will like, put in age, I will put in lamb's map. [00:17:00] I don't need to write everything and just do this I type of age and type of lots math.

So you can, so in the most important is in, in experie is that you can mix variables and text, right? Now. However, if you want to do it a little bit quicker, you can do like this. And you can also do print upstream. If you just want to show what you have written in the variable and what the output should be.

You could do like this type of for example, number of children and you can see, yeah, we only get class of in, right? But we want to get the out, what we had before. So you can make an equal sign here and then you can see. Type number of children equals class int. So you have the equal sign. It gives you whatever is here on the left upper end shown in the print as well.

[00:18:00] So this is quite neat when you want to quickly understand your data types and understand your variables. So moving on, we come into something called connections. Collection types. So in collections we have we have lists, we have tuple, we have set, we have dictionary. I won't go through all of them, but we will start with list because that is a very common one and very good to understand.

So we start with list and in list we can create a list of interests. equals to here, badminton. I want to, I have interest in yoga, in math, and in programming. So these are my interests so I can type out interests, and you can see this is a list of interests. So this is a list of strings right now.

However, it doesn't need to be just [00:19:00] strings, right? You can actually mix the data types. This is different from in in other languages, in many other languages where you have statically typed and then you have something called arrays. And in arrays they have a a fixed type. So for example, you have array of strings, then you only have strings.

If you have array of int, then you only have ints. But in Python, you can mix the types. So I can do person equals to option. I could have like the 2. 8 here. I can have one and I could have true. So I can mix all this. This is perfectly fine. So person, you can see we have a string. I have a. A double and we have a ink and a a Boolean.

So that's no problem. And also we can do, we can append a list into another list that's also no problem. So person and not append. I could append I could append my interests, for example. And if I run this one you can see what happens. I don't want to run it again, because then the interest will be added again.[00:20:00] 

So what we've done is that we have mutated the list. So the list have changed, right? Mutation means changing. So lists are mutable. We changed the list and you can see here that we have a list of a lot of values and a list. And also here you can add another thing. For example, I can do append. 100, for example, and if I type out person, you can see that, yeah, we have appended 100 in the end, so we mutate it.

But no matter, the thing I wanted to show is that you can have a list in a list. That's no problem. You can have you can have other data types in a list. You can have classes in, objects in the lists as well. So here, let's come into accessing lists. So we have accessing items in the list or elements in the lists.

And in order to access something you can do like this person of zero, and then we [00:21:00] get caution here. We can do person of one and we get the first one. Actually I will do like this. I'll create another cell here and just type the person so that you can see it as reference. So here, and if I do person of minus one, then I count backwards.

So I get 100 here. And if I do person of minus two, then I get the whole list. You can see I get this list. Okay, so what if I want to have something in the list? That's no problem. So I can do person of minus two, I get the list. And in the list I could pick out yoga, for example, one. Note that we count from zero.

So badminton is the first one, is zero. And index one is yoga. So this one will give me yoga. Okay. And here we can also come into something called slicing a list. This is really good tool. [00:22:00] Slicing a list. And this doesn't really exist in, in many languages. It doesn't exist in some languages. It does, but in Python slicing is quite it's used a lot.

Together with, different collection types. So we have person of we can have person, we can type out the person list so that we can see it as reference. So here is the list. If I do person of colon 2, then I get from 0 to 2. So I get coxion, 32. 8, and 1. Or it's two is not so it's not inclusive.

So I get the zero and one. And if I do, for example, person of zero colon two, it means that I will have every second one. So I get here, caution, I get one and I get this list. So I get every second element. I could reverse a list. So I could do [00:23:00] interest, for example, to show how interest look like.

And then I could reverse this interest if I want. Interest of colon, ms1. And then you can see here I reversed it, right? So you can see that there's a tuple here, tuple with parenthesis because I used a comma to show both. But I could have put them in different cells. And so what I'm doing here in contrast to the the lecture notes, in lecture notes we have it more compact, and here I work with a lot of cells before, because it's more dynamic for me to explain in this way, and you can see the results.

However, note that you should you can pick, put it in many of these statements in one cell if you want. So you don't need to divide into several cells. So this is really good for learning and demonstration purposes. So then we have sliced the list. We can eat the rate of our list.

So let's do some iteration. Iterate over list. And what does iteration mean? Iteration means basically [00:24:00] looping over. So you're traversing over a list. And then you can take out the elements and do something with it. For example, we have numbers that's an empty list. And then we can do for i in range n.

We can do numbers dot n dot n. So this is very common that people from other languages usually do when they see this. Start with Python because in other languages there's many hormone construct is like four in I equals zero. And as semicolon I is smaller than 10. And then I plus. Right?

And and then you. You append to each to the list, or you actually have created an array of a fixed length and you go through each of the element in the array and you assign it a number that is also possible. However, in Python, there's some other ways to do this. So we can do like this. We can do numbers equals to this [00:25:00] is a list comprehension.

So I am doing. i for i in range m. So if I write out numbers now, you can see this same result. And what this means is this is a list comprehension, and in list comprehension you have you get the i th value for i in range 10. So you go 0 to 9 and it puts it into the list, right? So with this we could continue and getting squares, for example.

So we could do squares equals to a list we could do i in square or i in numbers. So then I, it means that I look through these numbers and for each of the value, I square it, right? So squares, and you can see we, we looked through it and squared it. And if I want to, I could look through every one of them and print them out, for example.

So doing that, so for square in squares, print [00:26:00] square, like this. And then you can see it printed out here. So there's a lot of things you can do with with this. We can also take out so let's see. We could continue here. Let's see, list comprehension. Yeah, I've covered that. And and later on we have in the lecture note, there's also tuple that is optional.

It's basically an immutable collection. So it's similar to list, but it's immutable, so you cannot change it. And then there's also set, which is a unique collection, which is quite good when you want to get the unique value or for some reason. So then there's some set logic after that, but that I will also skip here.

This, that is also optional. Here we'll go into dictionary. Dictionary. So dictionary is basically a p value pair.

We start with [00:27:00] creating a dictionary here. So person dict syntax. So you can create dictionary in two ways. You can use this dict syntax like what I show here, dict. And you type in the keys in you type in the keys.

And so name equals option, age equals 32. 8, etc. So this is the person dict syntax, or this is the dict syntax by using the dict function. So you can see here we have name as option and age as 32. 8. And this is actually how you create it using the bracket syntax. So I copy this one, and I put it here. So this is how you create a dictionary with the bracket syntax.

I can [00:28:00] call it person, bit, bracket, syntax. So they are equivalent. So if I do person, bit, bracket syntax, and I can write Dot keys. And you can see here the keys are name and age. And also if I do similar here with the person picked syntax. Person picked syntax, dots, keys.

And you can see it is the same name. H Dick, case name H. Okay so let's continue with one of them. So I'll do. For example, person dict syntax, and I can take out one, one of the keys. So I will take out the name. So I will get the value, h. If I do similar here, I copy this one, [00:29:00] and I type in h, and I get the h here.

Are they the same? The question is. We can do like this. We can find out their. memory address by doing hex id of person, bracket syntax, and you can see this is the memory address in hexadecimal. If I copy this one and I will do for just the big syntax and you can see they have different memory addresses.

So they are not they, so they are they are in different memory addresses, meaning that they are two different objects. So they're not the same object, however, they have the same content. Now we can iterate through a dictionary. For key in person picked syntax, we can print [00:30:00] the keys.

And here we get name and age. And also we could do like this. So we could do person big syntax, and we can put in the key. So you can see here we have the value, right? Because we get the key for each of them for each of the keys, and then we can put it into the dictionary to get the value right. However we can get the value.

Through, we can get the keys and values in another way. So for key comma value in a person, the syntax dot items. So this is how we iterate over both of them at the same time. So items will give you the key and value as a topple. So you now you can do print key comma value, sorry, key comma value like this.

So you get both [00:31:00] the key and value, right? So this is a neater way if you want to iterate over both keys and values. But if you are just interested in the keys, you do as the first one, key and value for the second ones. And if you only want the values, you can do the dot values here instead. But I won't show that.

Instead, we'll move on to some, we'll move on to something called Dictionary Comprehension. I will make this cell into Dictionary Comprehension,

like this.

I'll copy this from my lecture note. So I have two different lists now. ML terms, and I have the ML explanations. It's just two different lists, they are [00:32:00] the same length, that means they have five items each, same amount of, same number of items. So I could do some glossary where I have ML terms as keys, and I have ML explanations values, right?

So in order to do that, I could do a dictionary comprehension. And you as we know dictionary, we need to have a, um, we can use this curly braces syntax, right? Curly braces. So term dot lower, or I can take term first, colon, explanation, or term, comma, explanation, In C, ml terms, ml explanations, just like that.

And you can see here, we have [00:33:00] The keys and the values. So zip means that we zip them together. So the first one, first element goes with the first element in the second list or the second collection. And here we, so the term will be each of the ML terms and explanation will be each of the explanations.

And then we have key and value here. And also I could do lower if I want, and lower here as well. Like this. So now I have my glossaries. Great. Moving on, we'll go into strings. Strings is working about, working with the texts. So let's do like this. We have, I will create a string that looks like this.

Thanks. Thanks. I'll copy it from the lecture note. I have a weird formatted stream, MLterm, [00:34:00] supervised learning, right? First of all, we could do like this. We can calculate the number of we can calculate the number of Characters. So ml and it gives 23. So it also gives these spaces, so if you count them, just the letters here, it's not 23.

It's you get all the spaces as well. Okay? So in order to clean the spaces, we can do, like this ML thumb do strict. And you can see, we don't have the last we remove the leading and trailing spaces using strip. We can do like this, we could do mlterm. split. And it splits by default on each space, right?

So the spaces will be splitted, so then we have a list of these two. So if I want, I could do like [00:35:00] this, mlTerm. split. So I get this list, and I could join it with one space. So join. So then, what this means is that I have a string here of one space. And I join each element in the list with this in between.

That is what the join method does. So if I run this one, we get supervised learning, right? So cool, but we could put in more functions or more methods in order to clean this. So I could do dot lower, and we can see this is pretty clean. And now I could give it ML term clean. What's this? So ML term cleaned, and you can see supervised learning.

Perfect. The strings, they are lists of characters. For example, I have ml clean. I [00:36:00] could do zero and I will get the zero character, the other fast character. And so zero is the fast index, right? So if I do ML terms of minus one and get the G right, and if I do four colon seven, it will get.

Three characters. So I get four is R and then B, I right? So you can work with it as if it would be a list. So you can think of it as a list of characters. Okay, so also one, one interesting thing with, um, with this with strings is that you can actually add strings together and it will be concatenation.

For example, I can do a hello. Hello.

This is a weirdly, weird coloring because of the [00:37:00] color theme that I have, it's nothing wrong. Plus world, and you can see they concatenate together. So if I want a space between, I can do like this space. The addition here, if you add numbers, then it will be addition in arithmetic, right? But if you add Strings, it becomes concatenation, so you put the strings together.

So for example, now I have 5 plus 5, it's 10, right? However, 5 plus 5 is 55. And if we mix the, what happens if we mix them? Then we get the type error. So you can only concatenate string to string, not int to strings. So we remove this last one. So you can see that string addition becomes concatenation. It doesn't matter if it's number or not.[00:38:00] 

And also so this is something called so it's the plus operator that has been operator overloaded. It means that it is polymorphic and it will act differently depending on the types. Similar goes for the multiplication, asterisk operator. So if you multiply string that is, for example, I have five, Times five, then I get concatenation five times, right?

It's similar to list. If you do multiplication on list, they will concatenate as well. So good to know. So moving on, we'll go into if statement.

So now I have been in list. So we go into if statement, and if statements are quite simple. So it's similar to other languages. For example, we have predicted probability [00:39:00] equals 0. 8. So if predicted probability is larger than 0. 5, 0. 5 is actually 0. 5 so you can type it like that, and we can do Y pred equals one.

So the prediction is one is in one class. Else the prediction is in the other class, which is zero, right? So if predicted probability is 0. 8, then we will have one, right? So we can type out whiter, but we'll get, yeah, we'll get to one here.

And also we could do like this. So this is an ordinary if else statement. But we could do a one line if state if else statement. In other languages, it's also called a ternary operator, which you have in many [00:40:00] cases they have a question mark and colon, but in Python it's more readable so you can do like this prediction equals positive.

This is one of them. If y prep And it's negative. Okay, so prediction is positive. So usually you need to write like this, right? But since one is a true fee value and zero is a neg, is a policy value. So since ypr is true fee, when it's not zero, then it will it will be. Positive else it will be negative.

So if y prep, so if this condition is true, then it will be positive else it will be negative. For example, if I have yprep equals 5, then it's still truthy. 0. 5, it's still truthy. However, if I have [00:41:00] 0, then it's negative, right? It's falsy. That, that is how it works. Okay. So the important part is I wanted to show is the one line if else statement so that you have so this prediction variable, it will become one of them depending on the condition, right?

So you have the condition. Okay. And let's see, we could have several if only else, right? So we could have accuracy equals 0. 6, for example. And if accuracy larger than 0. 9, then we say our model performance Equals to root. I will copy these two. So I will mark these two. These two. And then I will do shift option down button or shift out down button if you are in [00:42:00] Windows.

So I will copy this one and copy this one again. So I will do elif. This corresponds to else if in many other languages. So first one is I will have larger than 0. 9 and then I will have larger than 0. 7 and then I will have an else statement here. So this is bad and this is moderate, right? So then I can type out accuracy is 0.

6 and I will type out model performance is bad, right? Because of this, so it goes into the else because This one won't be true. Accuracy is not larger than 0. 9. It's not larger than 7, 0. 7. So it comes into the else, right? And then we get bad. Great. Another. So [00:43:00] moving on here, we have, so we have the if statement and after the if statement you want to.

You may want to loop and you have a wild statement and you can see a wild statement as a type of if loop. That is how you can see it. So there's a condition that will make it loop and and as long as the condition remains true, when it becomes false, it won't loop anymore. So I have an example here.

I copy it here. Let's see. So this is an example.

Let's see, format it a little bit better. So there's an oil leakage causing the bird population in Ireland to one half in each year. From start, there were 80, 000 birds. How many years does it take for it to have 110 remaining? Okay so we could for loop it and but the thing is we don't know how many iterations we need with for loop.

And then, [00:44:00] and for that reason, a while loop is more is better to use because here it, the condition for the stopping criteria is a condition. So it's based on as long as it's true, then it will run as it will break, right? And this so then you, when you don't know how many iterations you need, you use a while loop.

So birds, we start with saying it's 80, 000 and year is starting with zero. And wild birds is larger than 8, 000 which is the, which is one 10th, right? So we can print the year here, year which year it is. There were how many birds? There were birds.

And then we do [00:45:00] birds divided by two, divided equal by two. So this is an assignment operator. So it means this is similar to birds equal birds divided by two. So this is similar to birds equal birds divided by two. And what this means is that we have the birds each time. So this is the new variable and this is the old variable.

Awesome. And and you actually assign it to to to a new birds variable. And it's so this is a short syntax for that. Birds divided equal by two, this exists in many other languages as well. And similarly here, year plus equals one. This is means year equal year plus one. So we add by one and in many other languages there, they have assignment operated, but they also have year plus.

But in Python, we have assignment operator like this. So let's print out, print.

So it [00:46:00] takes how many years? Year, years for the birds to have one pen remaining. Like this. And you can see, ah we have dot. Zero here because of the formatting when we divide it by two, it will become it will become a floating number, but I will do colon dot zero. It's a formatting so that we don't have zero fraction, so we don't have any decimals.

So I format it a little bit nicer. Okay. So you're free and then yeah, it takes four years for it to have. 1 10 remaining. Great. And then we also have so we have gone through wild statement here and then we're gonna go for as well. And we have seen four statements already in lists and in dictionaries.

So I'll keep this, keep it a little bit short. I'll copy from the lecture note here two [00:47:00] different lists, and I want to go through these lists, right? First, I'll go through the abbreviation, the four abbreviation in unsupervised abbreviations. Brain abbreviation. And and another thing is you don't need to understand exactly what these things are.

They are terminologies in machine learning because this could be a course in some in machine learning later. This could be a prerequisite for machine learning. So I use some examples from machine learning and just to, so you get some feel of what it is. Okay, so you don't need to understand it exactly, you just need to understand the mechanism of the for loop and all the other Python syntax and constructs.

So here I loop it, so I loop through each of the elements in the list so abbreviation in unsupervised abbreviation. So I go through this one, and this one. That is exactly what they do. [00:48:00] So if I want to go through them together, we already seen it as well. It's with the SIP. So I will copy this one abbreviation comma algorithm in SIP

and we'll SIP through unsupervised algorithms and we have abbreviation we could have a comma colon comma algorithm this. And you can see here k means, etc. Yes, great and we could do, yeah, we could create the, we could create the dictionary with with looping, which you saw it before, so I won't go through that again.

So this is what you usually do in many other languages. If you want to look through and you want to have the.

The index as well. So for example, like this, or [00:49:00] I in range of abbreviation and you do print F string abbreviation, I and you do if you do like this, let's see what you do, right? No, you get. I in range length of this one, right? Abbreviation like this. So when you do length of abbreviation, you get free, right?

And and we're actually not abbreviation, abbreviations or unsupervised abbreviation, sorry, unsupervised abbreviations like this. So the length of unsupervised abbreviation is free. So then you for loop with i, then you get 0, 1 and 2, because you do for i in range 3, right? And then you want to get the abbreviation as well, so maybe you write like this the unsupervised abbreviations of i.

So this is what many people [00:50:00] do when they come from other languages. Don't do this. Don't do this. This is not Nox Pythonic. And Pythonic, what I mean with that is idiomatic Python. So there's a better way to write it in Python. So this is Pythonic. It's an idiomatic way of writing Python.

So idiomatic mean it, it is a recommended way. So for I algorithm or for I abbreviation in enumerates supervised learning unsupervised n unsupervised abbreviations. Sorry, I have a little bit different in the lecture note. But it's quite similar. So here I will do string, abbreviation of I, and then I can do here abbreviation.

You can see it's the same here. I will actually do print, [00:51:00] so that we get the space between. Yes, so cool. And now you've seen so using enumerate, we get the index of the items as well. And if you want, you could you could do like this. I can copy this one and I will start with five, for example, and then you can see that it starts with five, six, seven.

So this is the enumerate takes in a starting integer. And it takes in an iterable, it's called. Yes. Okay, great. Now, this was the most fundamentals in in Python. And and then we will go through more fundamentals part in the next lecture. And then we'll go in more, more deeper into Python.

Thank you for watching this video and see you in the next one. Bye.

