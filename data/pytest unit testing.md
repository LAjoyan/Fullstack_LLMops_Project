# pytest unit testing

[00:00:00] Hello and welcome to this video on unit testing in Python. And we'll be using PI test. So that means we need to install PI test and then ~~we will in~~ we will use it to, test our vector class that we created in the polymorphism lecture, where we did a lot of operator overloading. ~~So then, and ~~we will use.

~~Pie ~~test to, test out different, methods, ~~different cla ~~the class ~~and~~ and show you how to do unit test. ~~You. And ~~there, ~~there's~~ a lot of different methodologies to do testing ~~and some is~~ for example, you do testing before you write the code so that, you make a test that will fail.

But the tests are basically, like requirements ~~so that~~ so that when you're implementing your code, it needs to, pass these tests. ~~Then you're working, ~~you are making the code to pass the tests. That is ~~the ~~how you implement the features. ~~And ~~this is a methodology called TDD. Test driven development.

However, we do it in the other side so that you have made, the class, you have made the methods, and now we implement [00:01:00] testing. ~~So ~~this is, just another methodology that is, somewhat simpler, but, TDD is, really good methodology ~~to, ~~to use and ~~so ~~I recommend that. Okay, so let's move on to Visual Studio Code.

So here I am in Visual Studio Code, and this time it's not empty. Now I have the vector class, as you've seen from the polymorphism lecture. If you haven't watched that, make sure to watch it. But basically what it does is that we create a vector. Class. And in this, using this class, we can instantiate vector instances.

And these vector instances, they have the property numbers, they have~~ done their ~~add method. That means that we can do addition using the addition. Operator and what it does is element wise addition, we have ~~done their sub ~~implemented, so we have ~~overloaded operator, ~~overloaded the minus ~~sign ~~operator.

We have operator overloaded the asterisk operator and did R mold to make reverse multiplication. [00:02:00] We have ~~a ~~done the length method ~~to~~ to be able to get the length of the of the vector so that basically it's just the length of the numbers, and then we have also there's something that I didn't cover really in, in that lecture but I have this in the lecture notes.

So we have done ~~their ~~abs to get the Euclidean norm of a vector. We have validate vectors ~~to ~~which we have covered and done the get item and the plot method, and then also a static method and ~~the done ~~the wrapper. So this is how the vector class looks like. So let's now set up the things that we need.

Okay, so what do we need? We need a. Uv, VNV. So we have a virtual environment. So make sure ~~you don't do this when~~ you don't do this when you are if you already have a virtual environment, ~~U uv, virtual environment. ~~But since I don't have one, I will do this and activate it as well. Activate, you need to do, even if you already have one before, so activate it and in Windows it's scripts instead of [00:03:00] bin.

So in Windows, it's source van GRS slash activate. So that is for windows. Okay, so now I've activated my virtual environment and now it's time to install the things we need. So UV P installed. Now I won't need ipi kernel because I won't work with, Jupyter Notebook. Instead I will work in Python script.

As you can see, ~~this vector class~~ this vector module is a Python script. ~~So Ppy, ~~so what I need is lib, since we use it in, my vector class, we need pie test. To do the testing. Okay, so that is it. Command K to clear out the terminal. And now I will have the terminal, to help me, run things later on.

So let's now create patch, tests, vector pi. So here, let's now import vector. So from Vector. [00:04:00] Import vector class. So what we can do is we can do vector, 1, 2, 3, and we can print that one to just try this out. So now you see that ~~we have, ~~we choose here to the bottom we choose which environment we should have our virtual environment.

And then I can run it. And when I run it, what you can see is that we have this vector output here, vector 1, 2, 3. Okay. So it means I can import this one. So now let's import PI from PI test, ~~import~~ import races, because I need that one. I don't need this vector anymore. So just start doing our tests.

So dev test. So all our tests, they start with test valid in it. So [00:05:00] just test in it. So V is our vector. 1, 2, 3. Assert V dot numbers equals two. 1, 2, 3. That is it. So now in our terminal, make sure you have activated your virtual environment and then we do LS to see that we have our test vector and our vector pi.

So we just do PI test and what you can see is that we have an error here. So it says import matplotlib pipe plot. SPLT. So no, no module name. Matplotlib. So what could an is? So we need to, in, we need to make sure that we have installed it. So uv PIP list. So I have lib, so it [00:06:00] shouldn't be an issue. I test.

Test vector. Yes, it's an issue here, let me debug and see.

Okay, so I debugged and the problem was that I had accidentally installed pie test to my global environment. So if you have done that, you should pip uninstall your pie test from your global environment. Because when I did run pie test, it chose my global. Pie test instead of my pie test in my UVVE and V.

So since it chose my global version, I didn't have mat lib installed there, so that's why I got this error. So now when I run pie test, you can see what happens. It finds test vector dot pi because it start with test and then it says dot means [00:07:00] that, yes, this is. This has been accepted. So it means that it's it passed.

So the, then let's break this down. So first we create a vector of 1, 2, 3, and then assert means that we make sure that this v dot numbers equals to 1, 2, 3. And if this is true, then it'll return true. Otherwise it will return false. So that is what assert means. So we make sure that it's it's equality here.

So then this is how we create our tests so we can create our audit tests so we can continue with our in it. So when you're testing a valid in it, you need to test a invalid in it as well, so invalid in it. So that's good practice to do and choose. Always good to choose a lot of edge cases to test your [00:08:00] program.

So with raises, we need to make sure that it raises an error whenever we do something wrong. And what type of error do we expect? We wanted to raise a type error when we put in the wrong type, right? So type error. Vector. 1, 2, 3. So when I run this one pie test, you can see now there are two dots. If I, for example, do like this because this will pass and it won't raise an hyper error, then we'll see that we will get the fail.

Yes, exactly. So there's a fail here. So it did not raise right, it did not raise type error. So that means that we have written our [00:09:00] test wrong. So then we just need to change this one and we can test other races. So with raises value error, I want a value error when I have an empty vector. Okay. So this one by test, it passes good.

So let's move on to test addition. So the test addition

here, we create two vectors, so V one equals vector, 1, 2, 3, and then we have V two goes to vector 4, 5, 6, and now we. We take out the result is V one plus V two, ~~and then we checker, ~~and for the results we know that we are doing element wise addition, right? [00:10:00] So then we do v results equals V one plus V two.

Then we check result dot numbers equal. Let's see. One plus 4, 5, 7, and then nine, right? And then we check this out. PI test, you can see three dots. And if I take for example, 90 here, which obviously is wrong, PI test. And you can see this is wrong, right? And here is an interesting fact that you might want to test is that if you want this case, for example, you want a vector and you want to add it with a ~~s ~~scaler value, ~~if you allow that~~ mathematically we don't allow it.

So we cannot add a scaler with a vector. So then you should get some kind of type error and what it could be is like whip races. [00:11:00] Type error and we can do V one plus. This is not the vector and it should give a type error. Yes, it gives ~~a PI ~~a type error. However, if we do with racist type error and then we do V one plus five.

And then we test it again and you can see it's okay. So we have pretest 1, 2, 3, and we have three dots here. So continue. We do DEF test. We can actually ~~copy this one. We can ~~copy this one to do subtraction. Subtraction, and we do minus here. Instead, we do minus [00:12:00] here, we do minus. And if we do minus, then this should be minus three.

Minus three. Yes. And it's correct.

So let us continue here. We can do test multiplication. And actually I want do that. Let's do some we can do test length. V equals the vector. 1, 2, 1 comma two, for example. And then we do assert length of V equals equal two. Test this one and it's okay. Can test the absolute value D test. Ab and as the absolute value is the Euclidean [00:13:00] norm, which is equal to the the sum of the squares and then square root of it.

So v of vector, for example, three comma four or four comma three. And then what should the result, what do we expect it to be? Four to the power of two. Plus three. Power two is 16 plus nine is 25, and a square root of that is five. So abs of V equal five.

Yes. And that works. Two, we can test validate vectors. So test validate vectors. And here we have V one equals to vector of one, two, copy. This one V two is vector of three four. And then we do [00:14:00] assert V one, validate vectors V two, and we need to assert that this is true. So we assert that it's true. And it's true.

If I assert that it's false, then you can see it doesn't work right? Because they are both vectors. So we need to assert that it's true. Okay. And then we can do V three equals another vector. However, this vector is 1, 2, 3, so this is of length three, right? So they don't have the same length, and if they don't have the same length, if you have seen the last video, then it should raise a a type error.

So with races. Type error. V one point validate vectors V three. And this should raise it. Yes, it raises it. And you should [00:15:00] also try, let's copy this one. Validate vectors. Where We'll, within something that is not a vector like this. And we run it and it works. And then we can test the get item. So dev test, get item.

So remember we had done the get item. So to do this, we have V equals vector. 1, 2, 3. Oh yeah. ~~12 ~~3 4 Also works. Asat the. V zero equals ~~12. ~~Asat V one equals ~~three. ~~Assert V say minus one equals ~~four. ~~Okay, run this one. And it works as well. Okay. And finally, we can test the plot. However, we cannot [00:16:00] we should manually check the visualization so that it's correct.

However, we can check that, the plotting works. And to do that, we do this V one equals vector one, two. Copy this a little bit. Yeah, we can take three of them. V 1, 2, 3. Say 2, 2, 3, 4, like this. And then we do V one plot, V two. Three. And then we do a set True. And what this does is it's a placeholder for successful execution.

So if it's a successful, we'll come here. Otherwise, if it's not successful, then we won't come there. So pay test. Yes, it's successful. We get the dot. Cool. So in this video, you have seen me working with testing, using unit testing, using PI test. So we [00:17:00] installed it and then we ~~I tested, we ~~tested, our vector class. We, started with testing the init. Under init and then going forward to testing the addition, subtraction testing the length and the absolute value, and validate the vectors and the get item and then the plotting.

And I hope that you worked with this in your ~~GitHub, Git, ~~GitHub repository so that you can commit and push your code. And I hope that the testing part was interesting for you. It's very important that you test your your functions, ~~your test, ~~your methods, you test your classes so that.

~~You get what you expect so ~~your code is more robust. Yes. Thank you for watching this video. See you in the next one. Bye.

