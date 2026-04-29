# Pydantic fundamentals

[00:00:00] Hello and welcome to this video where we'll go into ~~pedantic ~~the basics of pedantic that we can work with, data in an OOP manner. We'll work with fields, methods, validate data, and we'll output J data as well. In order to show you the power of Edan, we'll start with a normal OOP class. And then based on this one, we'll do manual validation to see how that works.

And we will go over to Pedant. And Pedant is very useful for, things such as, fast API. But, if you are, also interested into AI and lms, then you'll notice that the edan, is required and used a lot in order to. Structure the output. As that the, output from LMS are usually very unstructured, and you want to have it in a structured format and validate, its output that you can use [00:01:00] it more in later, stages of your applications.

Let's dive directly into the code.

**Kokchun Giang-1:** . Here I will, start with doing some setup. And if you have watched a lot of my videos before, I've usually used uv, for, package managing. However I've used it in a more traditional way. I will start in this video and in future videos, I will try to I will go into more modern way of using uv.

For doing that, we'll start with UV in it. This one will start a UV project. And here I want to you can see there's a main dot pi. Actually, I don't need that, I will remove it directly. And you can see PI project. Here is some, description of our project, and here you can see which version of Python I'm using.

, Then we do UV add, and ~~here we, ~~here we don't need to activate the virtual environment in order to install things [00:02:00] into it, as we have done before. Instead, you just do UV add. What do we need to add? I want to add pedantic and I want to have I pi kernel since I will be in Jupiter notebook and if I need something else, I will do it on the way.

, UV add. I have installed a few things and you can see there's a PI project here. Here they show the different dependencies that exist and you can see UV lock is actually all the installations. , Now when we have done this one, it's time to get started with whatever I'm going to do.

I will clear my terminal and I will do touch let's see, gigantic basics dot IB. . This is my Jupiter notebook, and here I will work. I will start with fundamentals and I don't need my terminal anymore, I close it down. I need to choose [00:03:00] my virtual environment and I choose this ENT basics.

? Change this one to Python. And that is it. Now I'm ready to start working. Let's start with we start without pedantic first, start without pedantic. . To start without pedantic, we create a, an example. Class person. What should this person have? Deaf dunder in it. I want to have a name, a gender and age, and I want to type in it string gender string as well.

And age. I will have let's see in. , That is quite nice starting point as a type painting and it returns none. ? Note that we will create. We will assign the values from the parameters here into the [00:04:00] object itself or into the instance itself. Then we need to use self.

Because the thing is I'm taking this from the ground up. That you, you should have OOP background. You should have done some OOP in Python before, but if you haven't I think it should be able, manageable to follow along anyway. That's why I'm explaining a lot of OOP in very fundamentally.

Here, basically the self it's when you're instantiating a instance from this person class it will inject itself into the self parameter. Then it will have everything ~~ref ~~you can reference, attributes ~~and, ~~and methods using the self, ? That's why we do self name equals to name.

That means that we will bind this variable name into the instance itself. Then I will do copy this [00:05:00] a few times and I will do self, that gender equals to gender. And here I will do some, vs. Code magic. Command D, command D. It means I mark these two and I will change it to H. .

Nice. ~~Some ~~some small magic. . And now I have this person class. Now let's try to instantiate the person. Person one. Equals to person, and here I'll name equals to tion and age equals to 34, and gender equals to male. Something like this. . And then if I write person one, you can see that, oh, this is the default than the wrapper of my person.

That's why it just says a person in a particular in a particular memory address. ? However, if I do [00:06:00] person one.name, you can see, ah, I get tion. Person one dot H. I get the H. . And on and forth. This is how I get my attributes. I use the dot notation to do that. , Let's try out something else we can do like this person two equals to person name equals to.

Yeah, this one will work. Gender equals to true. This is totally crazy, but it will work. Age equals to minus 10. That works like there is nothing preventing it to not work. ~~Even if you have seen ah, but we had. ~~Even if I hover it, you can see that we have name as a string, gender as a string, H as an int, but these are just type hint, that's [00:07:00] type hint.

It's not statically, it's not a hard type language in Python. That means that when, even if we're type hinted, we said that. Yeah, name should be string, gender should be string. H should be in, but nothing hinders the user from actually putting in crazy values like this. If I do person two, you can see it works very strange, ?

But actually it's not strange because. As we said, Python is not hard type as in other languages such as or many other languages such as Java C sharp rust, and c plus and many more. In Python, there's a lot of freedom. But it comes at a cost. ~~The cost is that ~~? The freedom is that, yeah, it's very easy to work with Python and start building stuffs, but when you start [00:08:00] to come to the certain point that you need to have validation, you need to have.

A lot of different things in order to make make it like robust. Then Python is actually hard to scale and make it more robust. You need to learn some more packages. I will show you something like this. We will try to validate this code now to try to make it more robust. I will do validation of our person class.

, To validate this one, let's just go up and copy what I have here. I'll copy this past, paste it here. This should be a Python cell. ? Let's check this out. We want to check the name. For example, I want it to be string, if not this instance, [00:09:00] name comma string. Then we shall raise a type error and say that F string name must be of type string, not.

Whatever you put in, what did you put in? You put in type of name, ? If I do like person three, for example, or I can try and fail one here. Person name equals say three point 1415. . Yeah, you can let all the ones be there. You can see there's a type error. Now it says, must be of type string, not class float.

Great. Let's try and accept this. Try accept as l print error. I get the error. And let's see, why doesn't this work? Except, ah, except hyper, of course, like this. . And now you can see, ah, [00:10:00] it worked. It has given an a validation here, it's stopping me to actually put in a name and that is not a string.

, Let's continue. I will copy this one. And I will, I want to try out to how about if I do say that name is we say person three, I guess I haven't used that one. Name equals to Wagner and you are age 54. Or actually ~~we taken ~~we take minus 54 because someone has accidentally clicked on the minus button, unfortunately.

Person three, actually I will just write a down the wrapper here that we get a nicer representation done. The wrapper return, s string of [00:11:00] person. Let's see, person, let's see. Self name, self, gender, self h. , This done the wrapper. You can see now when I'm running this person three, I will.

~~The d the wrapper, writing it out, ? This is the, ~~in Jupyter Notebook they will use the wrapper by default for the last statement or the last line here. , Here you can see person three, and this is the d the of it, it returns person, and then self.name, nar. And then. Gender m and age minus 54.

, There is an issue here now, and the issue is that we are able to have a negative age, and that is bad, ? In order for us to have a better we need to validate on the age as well. [00:12:00] However, we don't want to validate the, because if you, for example, I will show you one way, if not is instance if not is instance value, comma in.

For example, if we want to have in, we could have ~~in or ~~float as well, but let's make it a little bit simpler. Raise type error. F string H must be of type in not type H. . Yeah, exactly not type H And we shouldn't have value here. Instead, we should have h like this. And we need to protect it also with that it cannot be negative, ?

If. H we need to have h is larger than zero. Larger equals zero because it can be zero less than 125. And we have raised a [00:13:00] type error here or value error. Sring h must be between zero and 1 24, not. Value which you have provided, ? Or not age. . Yes. Now we should get an error. Let's see.

We should get an error now, ? Because. We have age if not, ? If not age is in this this interval. Now we should get the error. Good. We get value error. Now I want to actually accept value error. , This one is actually the old one. That's why it's. Staying there. You can see h must be between zero and 124, not minus 54.

, Great, that works. However, what if we want to do something in the style of this, ~~person? ~~[00:14:00] Person. Let's take another person that will work. I will copy this one. ~~Person three or ~~person four, we can take equals to Bella. You are you are four years old and you are a female. , Person four.

It's called Bella, and ~~this one's, ~~this one works. However, if I do person four H equals to minus five. It works as well. Strangely enough, you can see it works. However, we had validation ? Let's take a look. The validation, you can see it's when it's in the init. It's in the dander, init that we have this validation, ?

The validation. It's only in the DDA init, and it's not, when we are changing the value, it's not [00:15:00] affecting it, ? Because it's only when we are instantiating an instance then that the DDA init will run. Afterwards it doesn't run anymore. What you need to do in order to validate this is to actually put in something called a property.

If you are from other OOP languages, you will probably understand properly with getter and setter. In Python, we have property with Getter and setter as well. But the syntactic sugar is quite nice when we use something called the decorator. I'm sorry for you guys that haven't studied enough OOP.

But if you need to review OOP, take a look into my other videos where I have taught a lot of OOP as well, Python, o, OP, but I want to just make a point now with with the how to do the validation. I copied this person and let's try to [00:16:00] fix this issue here. What we need to do is something called, at.

Property. I want to create this h self. This is the getter of H. What it does is return self underscore h. Underscore is the backing private variable, private by convention. It's the ~~packing ~~variable ~~which which will protect. ~~Which we won't touch, basically. This one, this is the getter, and then we have a setter that is called at h Setter, FH.

And here we have self comma value or we can have cell from H. Actually, this one will work. And you can see here is all our. Validation code for the age setter. Whenever we [00:17:00] do something in the style of actually. Self doco H equals to H and we need to set here as well. Self H equals to H. When we do something in style of, with the equal sign here, equal operator, it will call this the setter by default.

This setter code will be run. And whenever we just do self h then the getter code will run. This part is the getter, this part is the setter. And the thing with this is that the setter will have a lot of validation that will protect our H. What you do now is that for example, I'll just copy this one.

I'll take this example again. Person five. But I'll say Natalie. Natalie [00:18:00] for example. You are four years old person. Five. . This one works because it works because we have this is it went through the validation. And then if we take person five H equals minus three, you can see there is a value error and which says.

H must be between zero and 124, not minus three. If I take 125 and you can see it fails as well. Good. Here I'll do, try accept value, error as add print out. . That is quite cool. Now we are able to protect it. You can see we've protected with some validation codes that the input is as we expect.

What we can also try out is that I'll just copy this [00:19:00] one. I will try with a type error now, type error person. I will create the new person here. Just to show you that even in the DDA in it, it'll work. . Instead of, I will do something like this, a string four, and you can see h must be of type ink, not class string.

. That means we have done some validation on the name and done validation on the. On the edge, however, take a look into this code. Now it's becoming bloated. If we are going to do more validations more we do the gender as well, we need to validate that one as well. While you could make it more dry by lifting out some stuffs into some functions and you can do some.

Other things we've done their sets and done the get, of course. There, there's a lot of things you can do. [00:20:00] But this is like a normal way in op to like a naive way to do validation. However, now we will try to do validation, but we will go into pedantic to see how that will look.

Remember the code looks like this, and now we will move on to pedantic. Validate using pedantic. . ~~I.~~

**Kokchun Giang-2:** , To do. Validation using edan, you need to start with importing. From pedantic import let's say import base model. Base model is, it's a class which we will inherit from and by inheriting from the base model our class becomes a edan model, but it's still a class, remember? ? It's still a class as normal, but it's also a EDAN model.

And as a edan model, [00:21:00] there is some really nice benefits I'll show you. Class person, it inherits from base model. ~~Then you, ~~then what you do is that you do type thing for the syntax is basically type thing. We do same as before, but now we have name colon string. This is a field, gender, colon string, H colon int.

And now we have our person class. , We can do person. How much, if I'm up to six, ? We can do like person name equals Christina. Gender equals to female. And we have age equals to 29, for example, person [00:22:00] six. Oh, we got a repper for free. Oh, that was nice. We got a done the wrapper for free, we didn't need to implement it as we did before.

. That was one thing. Can we do. Something like this person six H. Yes. We got 29. Nice person. Six H equals to 36 person. 6 36. Great. It works. However, can I do something like this person?

**Kokchun Giang-3:** Person six. Person six H equals to 30. And that works strangely enough. ~~Person six ~~person six, you can see it becomes 30. Apparently it works. But let me show you something else. ~~Let's create a person. ~~Let's create a person where it fails. [00:23:00] Person, I will come back to this issue later on.

I would say issue here. Person of say we have some numbers here, for example, and you can see there's a validation error. ~~I will do try accept here. ~~Try, accept validation, error. Then we need to import that from tic, import validation error, accept validation error as added print add.

. Yes, this is the validation error that we get. Name input should be a valid string. You can see type, string type input. Value is this. Input type is int that is not . However, I could do something in style of this. For example, compare this one person, I say quote 29, and I say, here is ~~now, ~~for example, , this one [00:24:00] works because ~~29, ~~the quote 29 is coerced into. 29. This string, ~~string ~~29 is coerced into 29. It works. You can see there's no quotes here in this 29. However, we still get an issue ~~with, with this like ~~we can change it afterwards, ? In order to stop us to change it afterwards, what you need to do is that we copy this person here,

We copy this person, and what we should do is to also add in model config. Model config equals two. From P import config dig. We do a config dig and we say assignment validate assignment. Validate assignment equals to true. ? When we do this. You can see what will [00:25:00] happen when we, for example, say we say that this is an person.

~~Person. How many? Seven. This is very bad naming convention, by the way by doing a lot of persons. But no matter, ~~this is just to show you how works. Person seven. You can see, ah, it works. We have coerced it ~~to ~~to an H, ? That works. Person seven dot H equals to 30, for example.

Yeah, it can be 30 and we get the validation error. That is great. I will just copy my validation error as before. Copy this one ~~and I will. Put in this one instead of this one here. ~~. And we get one validation error now when we're changing the attribute, ? We try to assign to this attribute, assign to this age, and now we get validation on it as well.

You can see one validation error per person. You can see 30. Input type string, ? It should be in int parsing, ? Person seven H [00:26:00] equals 10 will work. Person seven, you can see it works. Now the age is 10. , That is some examples. And we can show some more example.

For example, ~~I can ~~I can use another ~~try, ~~try accept here and let's create another person here. Person I will try to fail in several places. Name equals to three point 1415, gender equals to two point. Seven 14 h equals to minus four, for example. And you can see it fails in, it gives two validation errors you can see it, fails in several and that is quite nice that you can know which, places it has failed.

It has ~~play ~~failed in name and gender. However, the age, we haven't actually done validation for [00:27:00] negative values. We'll fix that as well. Now when you have this, ~~you can, for example, ~~you can change it. ~~You can do ~~you know that the name needs to be changed to Sophia, for example, and the gender.

We say F . And now it works. But ~~the problem is that. For ~~the problem is that the h is still negative, we need to fix the person class with some age validation. Let's ~~do ~~add h validation. I'll go back and copy from, my previous code. Let's see. Here is the code, ? This is the code.

You can see the class is quite neat. It's quite short. We want to have some validation on the age as well. From p import field. The field is used to do, validation. Here we can do equals to field and ~~we do. ~~It should be [00:28:00] greater than minus one. It should be less than, let's see, did I say 125 before?

I don't remember. Less than 125. This means that if we do something in style of this one. We see that we get the validation error for person, ? We can see input should be greater than minus one. That is quite nice. We have, by default we have really nice validation by having like very simple code like this.

And also, of course, we could do some more validation. We could do something more here. We could, for example. From typing, import literal, since I've used m and f here, we can do like this. Gender should be a literal

M comma [00:29:00] F. If I do fem like this, you can see this one fails as well. Input should be M or F what we got fem. . That is quite neat. We have and now let, this is like very useful for for example, when we're working with Fast API later on. We will have to we will create our own APIs.

And when you are creating API, you need to be able to validate code. You need to validate data and you need to output into j you need to do something called serial serializations and de serializations. ? Serialization means that we go from an object back to a J string. And this serialization is that we go from a Jason.

Into an object in a Python instance. And the thing is, that object is [00:30:00] really nice to work with in Python. However, when we're sending data back and forth through an API, then we need to do that through json. That is the standard. That's why we need to change it back and forth from Jason.

. Then we need to do some ~~serialization and de serialization. To do that let's see, ~~serialization and de serialization. And Edan supports that fast. API builds a lot upon Edan. And also we will if you're following me, of course I will go into some ai and for ai we will use a lot of edan to structure the output from L LMS LLMs.

Edan is I will refer to it a lot. You need to learn pedantic. , Let's take a look into person seven. This is Nina, gender, F and H 10. I do model dump,

and you can see this is a dictionary. [00:31:00] And if I go from. This is we go, we do a serialization here.

And when you have it in a, as a dictionary, you could, for example, do something in style of this. I'll copy this one.

**Kokchun Giang-4:** I will do with open, let's see, open person J in mode, S, F or S five. And then I will do import. Jason and I will do ~~Jason dump. ~~Jason dump, and I will copy this one inside here, comma file. . When I do this one, I get this person adjacent. If I click on this one, you can see this is the data that we have dumped into this file, ?

This person adjacent [00:32:00] file. ~~I, ~~you can see that if we have dumped it, we can go back also. Now we have written to a Jason. Now we want to do deserialization ~~de serialization ~~and to do deserialization. Basically what you do is to do with open person Jason, as read as file, and with the Jason data equals the file read.

Now you can see Jason data. It looks like this. It has a string here. This is serialized, ? I'll just do a print here that you can see that. ~~Or ~~actually print. ~~I will do ~~wrapper of this one ~~wrapper. Let's see, ~~wrapper like this. And you can see there's a coat there. It's a string.

And now I want to DC realize it. Person, actually the DC realization happens here. Person [00:33:00] dot ~~model model validate Jason. I ~~model validate Jason, I model validate this. J data basically. . And you can see, ah, I got back my instance. That is really cool. We go, we can serialize, we can deserialize.

With the help of pedantic ~~and there, and ~~we have done a lot of validation ~~with pedantic, ~~with very little code. I hope that this was helpful for you. Let's do. Take out the terminal and GI at dot git, commit dash m gigantic basics. . And then do git push as well.

, in this video we have gone into pedantic for validation that we can work with data in an OOP manner. You can go from OOP instances back into, jason and from Jason back into OOP instances. That is [00:34:00] really cool since, for example, I talked about fast, API ~~when you are ~~when you need to create an API and you need to send data back and forth, and that is through Jason and when you have sent data.

Or receive data in json, then you can make it the d serialize into Python objects which you can work with. And also you can go from Python objects and serialize it back into JSON and then send it, to, to someone else to get that data. And also we with pedantic validation that is really useful when we're working with LLMs, as you've seen that a lot of LLMs get a lot of unstructured data, we need to structure it in a certain way.

And a lot of frameworks ~~using ~~use, pedantic under the hood. To make the data structured. This is the foundation of everything. I hope that you've learned a lot in this video. And there, there's another video I have in pedantic where I go into [00:35:00] pedantic together with an A an API.

I use Pokemon API. Take a look into that as well that you learn how. To ~~get the use more ~~validate the data that comes from an API. And then later on I also have a lot of videos in in Fast API where pedantic plays a larger role there as well. And also pedantic in lms of course in particular Gemini have used because they have really nice free tire.

, Thank you for watching this video and see you in the next one. Bye.

