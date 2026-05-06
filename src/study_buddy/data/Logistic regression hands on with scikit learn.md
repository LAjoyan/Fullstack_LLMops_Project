# Logistic regression hands on with scikit learn

[00:00:00] Hello and welcome to this video where we'll go into hands on logistic regression with psychic Learn in Python. Here we'll do classification and before you have learned the theory and intuition about logistic regression, and now we'll go into the code. We'll also do some exploratory data analysis ~~on ~~on the data and then we'll.

The prediction ~~on ~~with logistic regression and finally doing some evaluation that you can see how evaluating classification works~~ to, ~~that you can see the different metrics being used in practice.

**Kokchun Giang-1:** Before going into the code, we'll find the data set first. I'm into this webpage stat learning.com. In introduction to Statistical learning, and we'll go into resources section here. In the resources we have here for ISLR second Edition, we'll find data sets. ~~It's the, let's see which one we'll pick.~~

We'll pick the default.

**Kokchun Giang-2:** The default at CSV is [00:01:00] found inside here, you need to download this all CSV files as sip, and inside there you'll see a default at CSV. Pick that one and.

Here I am in Visual Studio Code, and you can see my default at CSV. We can look at that and we can open it in preview that you can see it more like a spreadsheet. Here you have default No. You're a student. No. You have balance and you have income. Okay. The, the thing is we want to we want to choose what we want to predict, and we want to choose.

Default. It could be no or yes. Before doing that, we'll set, set some things up. It will start the U-V-V-N-V to create a virtual environment and the source dot then bin activated, activated and in in windows, it's script instead of bin. Okay, and now UVPP installed, we will need ipi kernel to work with Jupyter Notebook.

We'll need side kit dash learn, and we will need. Pandas. What else do we need? Yeah, pandas. That, that should be [00:02:00] fine. I think if we need more, we'll install it on the way. Okay, close this down and I will open a new file and I'll call this logistic regression. I pin B, this is a Jupiter notebook, and now we'll have a, a logistic regression like this.

Change this to Python environment, logistic regression. Okay. Import pandas as PD import. MPI as np. Then we will do exploratory data analysis. We'll start with here. I will have, let's see. EDA, exploratory data analysis, and then we'll do DF equals ~~pd. ~~Pd read, not read report, read csv, and we want to have default do CSV and then DF [00:03:00] head.

This is the dataset, and we'll do DF info to check the dataset. You see 100, the 10,000 nonno, and it's a object here for default and students. Yes or no? While the other ones are float 

**Kokchun Giang-3:** here you can see in describe that we have summary statistics. We have balance here. You have 10,000 in count. You have what does the mean and income and standard deviation mean, et cetera, blah, blah, blah. ~~You can ~~you can read this to study the data and we'll continue looking into what we have.

D, f default and DF default. Is this one is yes or no. Then we do value counts here, and what you can see is that it's mostly no. This means that this data set is very, it's very unbalanced. Mostly it's no. Very few, yes, very few percentage. It's, yes. Also, let's take a look into the F student.

Dot [00:04:00] value counts. You can see here is no. Yes. But mostly no. However, this in default is mostly it's unbalanced. Okay? However, those that are default are important. We'll take a look into different metrics here and you'll see a large difference later on. Now we'll also need the seaborne actually, import.

Seaborne as SNS, but I don't have seaborne. Let's fix that. Source, do van bin activate, and then UV P install seaborne. Okay, done. Now I have seaborne and then I can do this. SNS scatter plot data equals df, and we want to have X equals the balance. Check the y equals to income. Then I want to check like this.

SIBO is a quick way to plot [00:05:00] the data in a quite neat way. Yeah, when I say quick, it takes some time to load it first time.

Okay, now I have plotted it and what you can see is that we have income and we have the balance. We want to see if they have defaulted we can take a look into ~~another. ~~Another dimension here. We can have a hue is the color, and we ~~ch ~~choose the default here. What you can see is that mostly those with higher balance have a higher chance of default.

As you've seen in this picture here, okay? This graph can help for that. Let's make another graph here. Let's make fig X equals PLT. Oh. Then I need to have a mat plot lib as well. UVP installed mat plot lib. Ah, it is installed. Yes, because CBO is built upon it. PL PT subplots [00:06:00] one.

Let's see, one comma, two. Yeah, like this. Then four x let's see. We have to import import it. Import mat plot lib pi plot as PLT four x. Call in zip x comma, we'll go into balance. We'll go into income. For that then we'll look into the default. We'll look into, the balance and income here, I'll take, I'll show you what I mean here. Sns box plot data equals df x equals the default, and then y equals the call. X equals to x and U equals to default. What you [00:07:00] can see here is that. We have default as the x Let me show you, let me make this a little bit better.

We can have fig size equals to 10 comma four, and we'll have~~ yeah, we can have even 16 Comm four. Yeah. Okay. It's better. ~~DPI equals 200. Okay, good. ~~We can have larger six. Okay, better. ~~Take a look into this. We have a box spot here for the default. Then we have why as the balance and why as the income.

As you can see, ~~the ~~there's default no or yes. We want to see that. ~~Okay. ~~Here we have a higher balance. ~~High have ~~a higher chance of default. While the income, it doesn't seem to matter that much. ~~That, ~~that is what we saw with this box plot here. Now it's time for doing some encoding because we have categorical features.

Note that in the theory we saw that~~ we should we, ~~we should do either 100 encoding or dummy encoding. [00:08:00] Let's do dummy encoding. To do dummy encoding, we do df equals the PD dot get Dummies, and we have DF here and then columns equals to default. Comma student, because ~~these are the ones that needed to ~~these are the categorical features.

In order to make it into one hot encoding, we just do it like this. The f dot head, you'll see how it looks like here you see default. Yes. Student, no student. Yes, it's true and false. ~~And ~~and true and false becomes one and zero. ~~But ~~we can do~~ drop, ~~drop fast equals true because the thing is if it's fault, no true and default is as false. Then ~~and tho ~~those are ~~same features, basically or student, they're ~~the same features. By doing drop fast, we get dummy encoding, ~~which means that if it's not the fault, if it's like the fault, no, true, then.~~

Then it's not default. Yes. If default no is false, then it is default. ~~Yes. ~~What you do is like this. Drop fast equals two and we'll get an error here.

**Kokchun Giang-4:** Okay. The error is due to we, we have overwritten df. Just do run all here [00:09:00] and you'll see that it works. Okay, good. We have here. As you see default yes. As false and student yes as true. Then we wanted to change this true and false to zero and one. We'll get the df and let's see.

DF default. Yes. Call student yes equals to df. Default. Yes. Student. Yes. S type in, and we have DF head here and you can see it's become zero and and won. What we have done is that we just did s type in. They become they become zero and one. [00:10:00] Okay. Now it's time for logistic regression.

What we have been waiting for, logistic regression let's see. Change this to Python. Perfect. From SK Learn linear model, we're still in linear model import logistic regression. We'll have from SK learn model selection, import train test split from SK learn. Pre-processing import, standard scaler. Note that these are the different steps that we'll we'll do in logistic regression and in general when we're dealing with supervised learning.

But I will make most of the steps in in, in same place that you'll see XY equals DF drop. I won't go into the details of all the steps 'cause I've done that in previous videos on linear regression. [00:11:00] Default, yes. We'll drop that one Axis is Quest one, and then we'll have default Yes.

Here for the Y. Then we'll do. ~~We'll do, I'll copy this one that I don't get it wrong. ~~X train, X test, Y, train y test, train, test. Bit XY. We split it up with this train test split and it needs to be in this order and then we'll do scaler equals to standard scaler, and then we'll do scaled x train equals to scaler.fit transform because it's X train, we can do fit, transform and then we'll do scaled X test.

Equals to scaler. Dot transform of X test. Note that when we're doing standard scaler, we'll get the zero mean and one standard deviation for the training dataset. But for the testing, since it's using [00:12:00] the mu and sigma from scaled X from the X train, it won't be exactly zero and one for X test for scaled X test.

However, ~~I won't these are the correct procedures. ~~I won't show exactly the details, model equals to logistic regression. Let's see. We'll take a non in penalty that we don't use elastic net or L one or L two to take the most original model of logistic regression to just show that one model that fit scale x.

Trained. We're training on the scale X train and then Y train as the label. We'll take a look into model coefficient. Model dot intercept. These are the coefficients and this is the intercept. ~~This ~~these are for the features the parameters that we have trained up. Based on these ones, we'll place it into and [00:13:00] in logistic regression, you have seen the equation for the logistic function.

You have seen that there are W zero, W one, W2~~ and ~~and these are the ones that are placed inside ~~of. ~~Of this logistic function to, we put in these values to be able to predict on new samples, what we can take a look at, for example, we can take a test sample PD data frame.

Take a look into balance. We'll just pick one balance, say ~~1500, ~~1500. I pick the values that are close to what we can see in the data income. We'll pick like ~~40 K, ~~40 K, for example, and then we'll have. Here student? Yes. It's one and zero. One is student, one is not student. They have same balance and they have ~~same income.~~

~~Yeah, the same balance, the ~~same income. [00:14:00] Let's take a look into our test sample. This looks like this. We have balanced income. We have student yes or one and zero. Based on this one, we'll try and take a look into scale scaled test sample because we need to scale it equals to scaler.

Do transform. Our test sample and then we will do model dot predict proba it. This will give us the probability. Scaled test, sample, take a look into that one. These are the probabilities. What you can see here is that this is for we have no, and then we have, yes.

Let's take a look into our Y bread Y bread probability equals model predict proba for [00:15:00] scale X test. Then we can take a look into widespread probability code non five. You can see here mostly are no. Actually all of them are no. Here is, yes. We have a higher probability of no here. Finally now it's time for us to do some evaluation.

From SK Learn. Dot metrics. Note that here as before, this is 0.93. Here's 0.99. I forgot to say that because here's ~~minus e to the minus one. It's ~~10 to the minus one. It's the probability of it's thing to no. No, in default, that's the probability that it's trying to predict.

While this one is for the Yes. Probability for yes, here ~~is quite low. Probability for yes, ~~is quite low. Okay. Then we do from psychic learn metrics, [00:16:00] imports confusion matrix, accuracy score, ~~confusion, matrix display, ~~and we need classification report as well. These are different things that we're importing from s scaler metrics.

Yed equals to model. ~~Do what? ~~What we could do is that we could ~~take the just ~~take the arg max here, or we could do model dot predict directly we can do scale X test. ~~We'll get widespread. ~~Here you can see it's an array of 0, 0, 0, 0 comm one. It's predicting on whether or not it's defaulting.

~~Zero is default, and yes, it's one is ~~zero is not default and one is default. Then we can do, take a look into the accuracy. It is the accuracy score of y test comma y pre. Take a look into [00:17:00] accuracy and you can see, wow, it's quite high accuracy. This is a super good model. Is it though?

That is what I want to show you here, that when we do Confucian matrix, CM equals Confucian matrix wide test. Y bread labels equals to model classes like this and CM looks like this. We can do let's see. We do display equals to confusion matrix display of. CM and then display labels equals model clause.

Then we do this plot let's see, two equals, okay, this is the Confucian [00:18:00] matrix. What you can see here is that most of them are true negative, and then we have predicted it as a one, but it was zero. We have some false positive here. We have predicted it as zero as negative, but it was a positive.

We have missed a lot of positives this is a false, negative. 

**Kokchun Giang-5:** this means that the accuracy score, it's not very good metric to use as you, you have seen when we many cases that were positive, then how come we get high accuracy? Because accuracy was defined as true positive plus true negative. Are here true negative plus, true positive, divided by total number.

As you can see, the data set is really unbalanced. That's why the accuracy score is not good enough. What we can do is that [00:19:00] we will take a look into the other ones. By doing we can do it manually here, I'll show you. Accuracy, just accuracy equals two. Here we have 3, 1 7, 3 1, 7, 7 plus three.

Three

divided by total, total is 3 1, 7, 7. Plus three. Three plus seven. Seven plus 13. This is the accuracy, and then we can calculate the other ones recall equals to 30 three. It's the, recall is the true let me take a look into the definition. Recall. Is true positive, divided by true positive plus false negative.

We have divided by here, we [00:20:00] have true positive 33 plus false negative is seven, seven.

We can take a look into recall. You can see the recall is quite low, 0.3. This is one that you want to get higher, you want to have higher recall. Then we have precision equals two. It's true pos true positive 33. Divided by 33 plus 13. By the false false positive, we can take a look into precision.

The precision is a little, a bit higher. But in this case, you want to get the recall ~~to get ~~to be higher. ~~There, there's a way to get, ~~and also you have F1 which is a weighted average of both of them. It's ~~two times precision. ~~Two times recall times precision divided by [00:21:00] recall.

Plus precision. ~~Then you have ~~the F1 score is this 1 0 42. ~~This is a weighted mean of those. And ~~the it's ~~harmonic mean not weighted mean. ~~Harmonic mean of those two. ~~But you don't need to cal, this is just to show you how to compute this that which types you're using, which to, to calculate this.~~

But in order to do this quicker now when you know how the underlying calculation works, just do ~~classification report ~~classification report of y test y. ~~Preed ~~and we should get the same values. Here it's impossible to see 'cause this is a string. We need to print it out to get it nicely formatted.

As you can see here you have precision for zero and precision for one. What we did was calculated for one. If you look into this value here, the precision for 1 0 72 is same here. This is just rounded. Here we have recall for one is 0.3. You see this recall here, 0.3 and F1 is 0 42, which we had here, 0 42.

Here [00:22:00] they also have support, like how many of the samples that support this. Then we have here accuracy scores. 0 97 is the one that we calculated ~~here. .~~

In this video we have gone through logistic regression starting with this dataset default csv. Then we did some exploratory data analysis and then followed through the different psychic learn steps as we have always done, and doing logistic regression, but also showing how to do dummy encoding.

Finally we did evaluation to show you and not be misled by the accuracy score because a lot of people may just talk about how high accuracy do we have on this model, but that could be really misleading as this model was actually quite bad for this dataset. ~~We. ~~We didn't solve it quite well using logistic regression.

There's other ways to solve it better. However this is the results that we got, we shouldn't lie about it. We should take a look into the other metrics ~~we. ~~You get to learn more about the [00:23:00] different metrics, how to compute them, and take a look into the confusion matrix and finally the classification report and how to interpret this.

Yes. I hope that you learned a lot in this video and see in the next one ~~by.~~

