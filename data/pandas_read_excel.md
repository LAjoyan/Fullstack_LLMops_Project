# pandas\_read\_excel

[00:00:00] Hello and welcome to this video with pandas where we'll go into actually reading from an excel file and similar is when we're reading from csv file later on but now we will work with excel file and you will see how that works so before moving on to visual studio code let's move on to the browser so here in the browser i'm inside of kaggle so this, web page is, provided in the lecture notes that you can, find.

so when you're going in there, you should download this, click on the download button and, also register if you're not registered, otherwise just sign in and download it. You will get the zip file and just, unzip it and, take out the Excel file

when downloading this, you will get both an Excel file and then a CSV file. So you can see this is the CSV file here. And we will actually go into the Excel file here, because [00:01:00] you will later on work with CSV files a lot. So don't worry, you will learn how to use both of them. So let's move on to Visual Studio Code here.

So here I have put in the data, I have put in calories. xlsx. So let's read that in. So read Excel and choose the kernel. So here I have my virtual environment. I have installed, IPI kernel. I have installed pandas. That's it. The rest will install together. So import pandas as pd. Let's change this to, Python here. so import, we'll need matplotlib as well. Put pipe plot as PLT and we'll also need something else called seaborn [00:02:00] as SNS. So seaborn is used for plotting and it's very good for plotting, data frames. So let's, install that UV P install, map plot Lib and Si Born.

So now we can read this. DF pd D pd. Read Excel. let's read, let's see, we need to find the path to this. So in Jupyter notebook is quite easy. It's relative to where the Jupyter notebook is. So the Jupyter notebook is here. So relative to, to the data is a sibling to this notebook file.

So you just type data. And you go inside of data using slash and you'll find this calories. xlsx. Like this. So then you can do df. head to find the head of it. Define the first, [00:03:00] rows. However, this will generate an error as you'll see.

The first time takes a little time. Okay. So it says missing optional dependency, open PI XL. So use PIP or conduct to install open PI XL. Let's do that. UV PIP install open PI XL like this. Done. So let's rerun this out. Yes. And it works. So what it does is that whenever you don't specify which sheet it will pick the first sheet.

So we can go into this Excel file to look how it looks like. It actually only has one sheet and you can see that it's tabular form in Excel is a tabular format, right? And similarly, when you read it in into a data frame, it's a tabular format. And using df. head, we get the [00:04:00] head of it.

We could do df. head. Of, 10 and we get first, ten rows. We could do df tail five to get the last five rows. that's a little bit about df head and tails. so we can, when usually when I start to read in some, Excel file or CSV file, I want to understand the data set right.

And, to understand it. You usually do some kind of, exploratory data analysis. However, I won't do a complete EDA here. I will just start a little bit so that you can see how I'm working with it. Later on, we'll go into more depth into EDAs. So let's do df. info to get some info. So you can see DataFrame is an instance of the Pandas DataFrame class, right?

[00:05:00] And in this instance, it has a method called info. That's why we have parentheses. So tail is a method, head is a method, info is a method. So now you see how good it was that you have studied some OOP. So you understand how different types of libraries work. So DF dot info, we use this method and let's see what it happens.

We see here, this is the wrapper of this, in, in, or not the wrapper. It is the, it is actually, DF dot info prints this out, right? So you can see here, range index. I will actually zoom in a little bit here. And then we'll remove this one as well. So you can see, you can zoom in one more time to make it even simpler.

So we have here, [00:06:00] we can see, they have different columns and how many counts of them non null, so that if you see that the sum are a little smaller. And then the number of entries, then you know that we have nulls and we see the data types. They have object as data type and object is the most general data type.

So usually when you have strings, it's represented as objects. When you have list, you have dictionary, it's represented as objects. But however, if you see here, for example, per 100 grams, we see 100 g. So the G makes it, makes it, a string. so pandas infers it as strings when we're reading this, into a data frame.

So that's why we have object data type. However, with object data types, we cannot do anything. addition, subtraction, [00:07:00] we cannot do arithmetic operations on it, so we need to change it to other data types, right? We need to cost it to another data type. So for example, here we can cost it to integers. This one can also be costed to integers and this one as well, so that we can do some summary statistics on it, for example.

So moving on here, we can check out the DF. So this is, this column, right? So if we do this, we get a series of 2, 225.

Oh, sorry. If you heard that, it's, when I said series, my iPhone reacted because they thought, Hey, Siri. Okay. Sorry for that. so DF food category, you can see all the different [00:08:00] food categories and you can see it's repeated, right? So we could find out how many there are. We can do dot unique.

And if you just do dot unique like this, you see a bound method series, So it's a method. So you need to call it using parentheses. So here is the array of all the unique values, right? In this food category. So moving on here, we can find out the F, for example.

Yeah, we could do this one, for example, and the unique care as well, because I want to know if, if there's any, yeah, let's do that. So we have 100 G and 100 ML, so milliliters. Okay. So now we know that, okay. This, per 100 grams is not just, it's not just the G it's also for liquids. Right? because when you have liquid, you use a 100 mil as, as a [00:09:00] reference instead of 100 gram.

Okay. So let's do some, as I said before, I won't go into more exploratory data analysis. Instead, we'll do some and what type of data cleaning do we want? we should have a strategy for what we're doing. So my strategy is like this. We notice that all data types are object. We need to type cost to int. So type ast, objects, the int

for, for a few row, for a few columns, or the columns that you want to count on, we can, for example, we're going to convert. Cals,

so we should, I want to change column names. I want to [00:10:00] convert cals per 100 grams to int.

And I want to separate liquids

and solids to different BFs. So that is my strategy. So usually what type of strategy you want to have is based on what your goal is, and also it's based on what so usually as a data analyst or a data scientist or a data engineer or some similar roles, it's not sure that you're the one deciding always, instead you should work closely with the domain expertise.

So you should talk with the domain expert. What is it that you want to, be able to show? What is the goal? For example, a goal could be a graph, it could be a dashboard, it could be some analysis of some sort. [00:11:00] So you talk to the different stakeholders, you talk to your team and the domain experts, right? but here, let's say that we are, we want to have this. So let's do it like this, df. rename. We can rename, and when we're renaming, we should use a dictionary of the current columns. So in order for that, I will create a new code here, and I will just do df. columns to see what type of columns we have. we have food category, food item, etc. I want to change, I want to do like this, a dictionary,

cals, cals per 100 grams. I want to change it to calories. I want to change [00:12:00] per 100 grams as per 100.

I want to change kilojoule per 100 grams. I want it to be kilojoules. Okay. Like this. And in order to auto format, I use a shift alt F or shift option F and I run this one. And you can see that, oh, nothing happens. Okay, why? Because rename, if you look into the documentation here by hovering it, so it renames columns or index labels.

And you can see the axis. the axis, need to be defined. So if you look down a little bit here, you can see [00:13:00] axis, zero or index, one or columns. So now we're trying to change the indices. However, the indices Don't have any of these, values, right? So we need to specify. We can do index, or axis, Axis equals to columns. Or axis equals to one, that is equivalent. So if I run this one, you can see that the name has been changed. We have renamed it. Perfect. However, if I run df now, df. head, for example. We can see that, ah, it hasn't persisted. And why is that? that is because note that we're not mutating the data frame.

We're just get, we're getting a new data frame back. And in order for us to actually mutate it, there's, some, special method for doing that, or some special option for doing that, that, or we should assign [00:14:00] it to, to DF itself. So let's copy this one and we say df equals to this. So now I have reassigned df with the new names, right?

So if I do df. add, we can see that it works. It's the new names. Okay? So now you know that we have, so you should always reassign it in order for the changes to take, take place, right? Or there's usually some method called in some option called in place equals true, which can also be used. So let's continue now.

so our strategies, we wanted to change the calories, right? So DF calories. So you can see we have a lot of, we have Cal here and we have a space. [00:15:00] So this seems to be the pattern. So how to do this? it's quite simple. We could just do string slicing if this is the case. So if we're doing string slicing, if you could do like this, colon minus three, and then you get everything except the three last ones, right?

But that this one doesn't really work. so this one is normal slicing from zero to, The last three items. That's why we have two, two, two, instead of two, two, four, I think. So what you need to do is you need to do dot string. So by doing dot string, you're accessing this property. So property, we haven't actually talked about the, in the OOP, but, And this is a, method which you have, you have used, a, you have used a decorator so that you've given the method another, it's [00:16:00] given a method another, Functionality, which becomes a property and a property access it by doing dot notation without the parenthesis, right?

So with this property, you get the, you can use this as a string, normal string, but what it's different is that this will work element wise, it will work on each of the elements. And not one thing, I'm usually always using the data frame methods or the data frame, properties or attributes.

I will almost never, loop through a data frame. And that is because looping through a data frame is really slow. You should instead use, the methods, inside of, the day inside of the data frame API itself. That is because, when you're doing that, and data pandas can use something called vectorization [00:17:00] and a lot of optimizations, in order to make the performance much faster.

So in general, never look through a data frame. Sometimes you might need to look through a few values, but that is okay, but not much. Okay. So let's do this. Now we can see the calories has disappeared. Okay, can I then change it to int. asType, int. And you can see it worked. The dType is int64. However, same idea as before. for example, if I do df. calories. head. This is the series, right? Okay. And you can see it hasn't changed. So I should copy this one and reassign it. [00:18:00] So let's do that.

So we have df calories equals to df. head. And you can see that it has changed. we have reassigned it so that we have a new data frame. All right. And where we have fixed the calories. So let's continue now. I want to divide the solids and liquids. Actually we could continue with kilojoules and per 100 gram, but I will leave it for the reader, so you can, I won't take away all the fun for you.

So let's do like this. DF per 100 and we can see a lot of 100 grams. We should do dot value counts and this will count. if you know a scale, it's similar to group by, and then you do count, so you're doing an aggregation, of [00:19:00] each unique values here and you can see here, okay. The unique values were 100 g and 100 ml.

And you can see the number of entries for each. Number of rows corresponding to each of them. Cool! let's continue now. Let's continue with this. For example, if I want to pick out all the liquids, I should do like this. Vf per 100. equals to 100 ml. So then we get a lot of false and true.

so now I've gotten a boolean mask, right? This is a mask. And using this mask, I could pick out all the rows corresponding to this mask. Corresponding to where it's true, right? So df of [00:20:00] this boolean mask. We get all the values, or all the rows corresponding to 100 ml, right?

So corresponding to liquids. And you can see here 423. Per 100 grams, right? Value counts per 100 And you can see 423. So great. this one, we should reassign it. So I will have liquids here. Because this, and I can do liquids. To get the first file. And I will do similar for solids.

However, I will use the query syntax. Which I showed you in the last lecture. So df. query, which we want to query per 100 gram. this is the column, right? And we should do equal and [00:21:00] a string 100 g. And this is only those corresponding to, the solids, right? So 1 1 8 0 2. We have 2 here.

Cool. So solids equals to this one. So it's not head. And you can see here are the solids.

Okay, moving on now, let's find out something. we can find out some KPIs, it's called. We'll come back to KPIs later on in this lecture series. But here, a KPI, it could be find out top five categories with highest calories. . So in order to do this, we can do a sorting, so we could have solids [00:22:00] dot sort values and we can have buy, which column do you want to sort on?

I want to sort on calories.

And you can see that, oh, it's sorted on calories. It's possible to sort on calories because we changed it to Intes, right? And now You can see that the last five here are the ones we wanted, but they are in ascending order now. We should change it to descending order. So ascending equals false.

So now it's descending and you can see these are the top five. Okay, soups, maybe that should have been liquids. However, you should know that the dataset and there might be errors in it. So that's why it's important for, you to understand the set you're working with [00:23:00] and you show it to your domain expertise maybe.

The domain expertise says that this soup should, be a solid or it should be a liquid. Then if that person has said that, then you can change it or you can move it to the other category, for example. So that's, it's important to understand the data set. and not just work with it blindly.

However, we'll leave it like this. so let's do like this. We have solids and we have sorted, right? So solids sorted equals to this, and we can do solids sorted dots edge to get the top five, right? since we have seen head, I'll show you another one. So this is index location, so we're, indexing, based on, where it is. So it doesn't matter that this index is called 1621. When you do iloc, you start this with zero. Anyways, so 0, 1, 2, 3, [00:24:00] 4, 5. So if I do colon 5, then I will get the same result. So this is Python way of slicing. So we're getting the solids top 5.

Moving on. We can do similar for liquids. So liquids top 5 equals to liquid. sort values by calories ascending equals false. Liquid's top five, and you can see, oh, we didn't take the top five, but if I do dot head here, we get the top five.

Okay, so let's do some, small calculations here. For example, I could do like this. df. groupBy I want

to group by all the food categories. what did we do? We got the, to get the five top categories with highest calories. We looked [00:25:00] into solids by itself. We looked into liquids by itself. But now we will look into both of them together. So what I can do is that I could group by food category. So then I will get, ah, it says generic data frame group by object.

So this is just an object living in a, in a memory place. So by, by getting something from this, group by, we need to combine it with a, an aggregation method, right? So what can we do? I will pick out the calories. And, now we get a generic series group by that didn't help so much, but we take an aggregation immediate, for example, so aggregation function or method in this case means that we have a lot of, it's a many to one, transform, many to one mapping.

So we have many values. The output is one value, right? So we get the median and it's [00:26:00] one value per food category. So if I run this one, we can see, Ooh, each food category, we get the median calorie. Okay. So let's continue here. Let's sort this. So sort values. Okay. so why can I do like this?

because this returns a, a series object and a series object. We have a sort values. So that's why I can nest, the, the methods. So I, or I can chain the methods. I do one method after another, because it returns either a series or a data frame. So this is very helpful.

Good way to work with pandas, sort values by equals calories They don't have a buy because they only have, they only have, values here, right? So sort values and then we get it, a sending and we do a It was false, but then we have descending and now we just take dot.

I look [00:27:00] cool on pipe and then we get the top five.

And now we could do, now this is a series object, right? So we can do dot reset index. So we get indices of them and it becomes a data frame object again.

So now we have the data frames of the top five. Actually, it's not correct. If you see here, vegetable oils, 885. It's not really correct. How come? Cause we do I lock here in the sort values, reset index, or it is correct. so it takes the median, [00:28:00] right? so there's, for example, vegetable oils. We have several vegetable oils, right? So for example, here with germ oil, it's, or this, cod liver oil. It has 1000 calories. However, in the median, you take, you order all of them and you take out the middle value or the middle two value and divided by two.

So this is correct. So we can call it top five category. Equals to this top five category. And let's continue with some plotting now. So I want to plot this. So for example, in order to plot it, I could do SNS dot bar plot, and I will put in data equals to top five categories, for example. And we choose here X, which column is that?

X should be food category. Food [00:29:00] category, and y equals to calories.

So basically here I have a plot. And you can see this is quite ugly here. It should be changed. However, This is a simple way to plot using, Seaborn and, what you need to put in is the data is a data frame and you choose which is the X column, which is the Y column.

So this is how simple plotting using Seaborn works. And you can see it looks really similar to Matplotlib and that is because it use Matplotlib in the backend. Okay. So now I want to plot several of my plots. I want to plot them all at once. and what I usually see a lot of people do is that they just copy and paste this code three times and do a lot of settings, 

Don't do that. Instead, you can use looping. So just do an [00:30:00] iteration using for loop. And I can show you how to do that. So fig comm axis equals to PT subplots one comma three. We can choose the DPI dots per inches. 120 fig size equals to 16 comma four. Then you get three plot windows. And this you can, change yourself to find out which one fits for you.

And then we can take out some titles equals to, I can have solid of five. I can have liquids five and let's have some five, per group median. Okay. now we're working with different, I'm using lists and you can see we have three, items, right? three elements in this titles.

So that means that We're going to look [00:31:00] through it. What else do we want to look through? we want to look through, our data frames, right? So then we can just create a list of our data frames. So data frames equals to solids top five, we have liquids top five, and we have a top five category, right?

So now we have, for example, if I write out data frames, you can see it's a list of data frames. And if we want to take the zero, we get the zero data frame. So yeah, that is a very good advantage of using this list. You can actually put in different, you can put in different, Data types, you can put in different objects.

That's no problems, so let's use that to our advantage. X columns, so we want to have food item. let's see, food item, comma, food [00:32:00] category,

because it's, if you remember, they have food category in the categories while the other ones are food items. So now when we have this, let's look. So four x comma data, comma title, comma x column in C. And when we're doing C, We're taking all of these, three here. And the axis, all of these four.

And then we pick out, so that we get first title, we get first axe, we get first data frame, we get first x columns. And then we get the second, the third. So let's do that. Axes, data frames, titles, x [00:33:00] columns. Like this. And we do plot, sns. barplot. Data equals data, because we will get each of the data here.

X equals to X colon. We'll get each of the X colon. What else do we have? we have Y equals to calories. I'm using calories here because calories are, common for all of them. And it's the one we want to plot. x equal to x so we plot on which window right on which x here and then we do x dot set

title equals to title like this run it and we can see here's our plot it's quite ugly here that it's quite crowded so let's just rotate it [00:34:00] so we can do x dot sets x tick labels And this, actually needs to have, it's strange, but it's just how it works. 

So you get the Xtick labels. And this is so that you get these, labels and then you do a rotation of it. So rotation equals 90. Congratulations. Okay. And there's some, user warning here, but we can ignore that.

So now you see it's a rotated. Okay. Perfect. And, soon finished. Let's do pig dot save pig. And we can save it to, for example, figures slash calories dot.

Let's do like this, run it, and there is fine not found because there is no figures. So let's just create [00:35:00] and make the figures like this. So then if I run this one, now it has saved in the figures folder and we have these calories. Okay. It's a clipped out here. So let's, let's fix that with an option here.

We can do B box. In chess equals height. If I run this one, we can see that. Yeah, it will fit this, it will fit everything with the box. Okay, but we will come back with a lot of plotting later on. don't worry if, if this, seems quite new for you, but, we'll plot a lot in this course.

but thank you for watching this, and learn about, you learned about the data frames and, reading in Excel files and processing it. thank you for watching this, video and see you in the next one. Bye.

