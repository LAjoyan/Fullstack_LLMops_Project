# Logistic regression theory

[00:00:00] Hello and welcome to this video where we've come into logistic regression and we'll use it to classify data. And now we are talking about classification. And before ~~we talked about ~~in previous videos, we have talked about regression. ~~And ~~the difference between classification and regression is that in.

Classification. We have clear labels, , we have two different classes. They, it's discrete values. For example, you belong to number one, you belong to number two, you belong to class three, et cetera. While in linear regression, we predicted a, continuous value. ~~That, ~~that is a difference. ~~And, ~~but both are within the supervised learning.

It's still that we need a label. We need~~ a ~~a ground truth that is to say. Okay. But this will be a theoretical lecture

**Kokchun Giang-1:** here in the slides, we have logistic regression to classify data. Note that we have classification now, when we have labels, we're dealing with supervised learning. It's still [00:01:00] supervised learning. Supervised learning, we have regression, ~~we have. ~~It's quantitative data, it means that~~ what ~~what we want to predict is quantitative that is continuous.

For example, value 3.5, three point 35. Et cetera, 34. And this is in a continuous scale. It's quantitative, continuous label. While in the classification we have qualitative it means that we have categorical labels. ~~We have, you are, ~~you belong to class one, class two, class three. You are letter A, B, C, et cetera.

In linear regression it can deal with categorical features, but not with categorical labels. That is important. The features, ~~they, ~~they can be categorical in linear regression. That is totally fine, but not the label, not the target variable or the ~~predictor ~~predicted value variable.

Categorical labels, [00:02:00] we need classification algorithms. For categorical labels, we need classification. ~~Okay? ~~And for categorical features, they require encoding in order to ~~work with ~~work with them in regression. For example, you have categorical features that look like this. You have animal, and this is the feature name, the column name, and then you have rabbit hair and fish.

And what you need to do is doing something called one hot encoding. One hot encoding means that rabbit becomes the first one here, one, and then it's zero in hair and zero in fish. This means that it's only rabbit and for hair you can see that. It's zero in rabbit, one in hair, and zero for fish and on.

Now this is how you encode it it becomes numerical for the categorical feature. This works in linear regression. That's no problem. And also there's dummy [00:03:00] encoding that also works and for dummy encoding, you have here rabbit and hair. And since you know the last column must be fish, then it means that if we have zero zero, then we have fish.

This is also, okay, inferred to the third category as fish. This is how it works. ~~Okay. ~~And for when we model categorical label with logistic regression, take a look at how that looks like. ~~We have first, ~~we have, for example, here. We have one for malignant and S of benign, and these are tumors, and you have probabilities here.

You have probability for. Malignant ~~you pro ~~you have benign here a zero probability and here one for malignant and you have tumor size, for example. Tumor size is one feature. ~~Okay? You, you, ~~you get a few samples here, for example, you have. A [00:04:00] few samples that are benign and have low tumor size.

Note that benign and malignant is~~ this is the ~~the labels, and. And here ~~when, ~~when it's one, it's malignant and we have a higher tumor size. What you do is that in logistic regression, you have a logistic curve to fit this. ~~If you, ~~if you use. Linear regression, ~~you can see ~~you cannot fit this type of data because you only have one line here and one line then, then it's hard to find if you try to use a threshold to for example, a 0.5 as the threshold, and ~~it's, ~~it's not really correct.

It's kind of hard to do this. That's why you have a sigmoid curve. That is for logistic regression, and here for 0.5, you can see this is ~~the, it's a model with ~~the, it's called Sigmoid Curve or it's called the logistic function also. And the logistic function, it has an [00:05:00] S-curve and takes values from zero to one, which can model the probabilities.

It models the probability between zero and one. The probability of this tumor to be malignant. One means that it is malignant and zero's benign. And then, then there's~~ probability ~~probabilities in between. This is ~~how ~~how the function looks like. We won't go into the details of it, but if you know some calculus, ~~you should you, ~~you can take a look at the limits of it.

For limb X goes to infinity, and for limb X goes to minus infinity. ~~And and, and see what happens and ~~and see if you can approximate this curve. , But~~ we, ~~we won't go into more details about this one, but this is how the function looks like. ~~What, but what, ~~what you can see here is that we still have W zero hat and W one hat.

These are the parameters that need to be estimated. It still is the same procedure, or not the same procedure, but similar procedure that we need to estimate the [00:06:00] parameters. That is what we do when we train the data. ~~We, ~~we train the data, we estimate the parameters, we predict the class. Y hat is equal to one if the probability the P hat is larger equal than this threshold.

And if it's smaller than the threshold, we predict it as zero. Then we say that, okay, for example, we have a pre threshold of say 0.5, then we predict it as~~ if it's 0.5 ~~51, then it's predicted as one. However you, you can choose ~~the ~~the threshold could be different. For example for a simple model, maybe you want to have~~ a ~~a threshold that is more towards saying that it's malignant that you can use~~ some more ~~some other methods that are more accurate to determine.

. Here we ~~Eva ~~to evaluate a classification model. It's not using M-S-E-M-A-E and RMSE as we did before. Instead we need to use [00:07:00] something called a Confucian matrix, and it looks like this. You have number of predicted and you have number of actual, and when ~~it's. Predict. ~~You predict it as ~~one, ~~class one, and ~~then ~~the actual is class one.

Then we get the true positive, this is very good. If we get a predicted of zero and ~~we have ~~actual was one, then we have ~~false negative. It's ~~false negative, and when the prediction is ~~one, we predicted ~~one, but the actual was zero. Then we have false positive. And if the prediction was zero and actual was zero, then we have a true negative.

You want to be in the diagonal here. True, positive and true negative. That is what you want. And. Then you get different metrics depending on how many you get in ~~each of the, ~~each of these fields here. You have ~~true positive ~~number of true positive plus number of true negative divided by total, and you get the accuracy.

This is one [00:08:00] score. And note that the accuracy is not saying everything that for example, ~~if you have an un, ~~if you have an unbalanced set. For example, most of the patients were benign, but a ~~few of them were ~~few of them were malignant then. And then you will get a very, very high accuracy, even if you would have missed those that were malignant.

Because, for example, ~~like this, say ~~true ~~positive is the, , ~~positive is malignant but most of the patients were negative. Zero. If you have predicted. Everything to ~~pre ~~zero. And you will miss the few ones, let's say 2, 3, 4 out of 10,000. Those you will miss. However, since ~~the ~~they are very, very small number, you will still have something like 99% accuracy because of the formula here.

True positive plus true negative divide by total, because the total is very close to the [00:09:00] number of true negatives. That is very bad. ~~You, ~~your model could have no predictive , it cannot predict anything. And, and still you can get very high accuracy, bad for unbalanced data sets.

For precision, this is another metric. You have number of true positive divided by number of true positive plus number of false positive. Number of true positive, divided by true positive plus false positive. And you get the precision. This is good when we want to have low tolerance for false positive.

We want to have low tolerance for false positive that. ~~When, when, ~~when you get few false positive, it means that this precision is high. And when do you want to go for precision. an example when you want to have high precision [00:10:00] is in spam email detection. In spam email detection system, a false positive occurs when a legitimate email is incorrectly classified as spam and sent to the spam folder. ~~This is a false positive. ~~This can lead to, uses missing important communications, which is highly undesirable,

**Kokchun Giang-2:** . I call this ~~ham spam classification, but this is ~~email spam, ~~email ~~detection. , Here, precision is very important and for recall we have, this is another metric here. We have number of true positive, divide by ~~number, ~~true positive plus number of false negative. ~~What we take here is this side here.~~

~~We have number three positive. Divide by true positive plus false negative. And ~~this is good when we have low tolerance for false negative. For example, we have a quick COVID test. What we want here is that ~~we, ~~we don't want to miss someone that is actually sick. ~~If ~~if someone ~~is, ~~is sick.

We don't want to say that. You get negative. We want to minimize false negative. , And then we have F1 score. This is a kind of [00:11:00] average between those. It's combination of precision and recall. ~~It's, ~~it's a harmonic mean of precision and recall.

~~Okay. And ~~this gives~~ a, ~~a score of overall performance and ~~with ~~similarly to~~ when, ~~when we talked about linear regression and the metrics there, it's good that you combine, you use different models and then you compare. The results, the metrics for the different models to see which model is the one that you should pick.

And also in logistic regression, it's important that you can do and should do different types of. Hyper parameter tuning that you can use cross validation for doing that. In logistic regression, there's also possibility to use L one, L two and elastic nets. Ridge less and elastic nets for~~ pin ~~penalizing the weights.

. Okay. And then we have multinomial logistic regression. When we have many classes, for example, we have here, this is very classic, [00:12:00] this flower classification. We have iris, we have VA color. ~~We have, ~~they are zero, one, and two.

. What you have is that you have, here is the prediction. You get 0.7 for zero and 0.1 for one, and 0.2 for two. It means that this correspond to one sample and it means that~~ you, you, you, ~~you need to take the argument Max. Arg max of this p matrix. Y hat is arg max of P hat. It means that ~~we, ~~we get 0.7 here, 0.8, 0.6, and 0.9.

These are the ones that you get in your Y hat. This is the prediction, ~~this is the the predict, the, ~~the ones that~~ you, you, you get or you get, ~~you take the label of each of them, the argument of them. What you get this y hat that looks like this. This first one is zero, and the second one is one.

The third one is one, and the fourth one is. Two. This is your prediction. Zero, Iris, and then S Color, SCO and [00:13:00] Regena

in this video we have gone through the theory section and some intuition about logistic regression, and I hope that you've learned a lot. Here we've gone through starting with supervised learning and division of supervised learning into ~~regression and logistic regression.~~

Regression and classification. And then we saw how to work with categorical labels and then gone into logistic regression to see how the logistic function works, ~~how, ~~how that is used to model probabilities. And then going into some evaluation using classification. These evaluation metrics are used for most, ~~many ~~classification algorithms.

It's not just for. Logistic regression. This is quite useful to learn ~~as. But I, I hope, ~~and then afterwards, ~~we, ~~we took gone into ~~how, ~~how it would look like in multinomial logistic regression. And similarly here, ~~if, ~~if you have other classification. Models that predict multinomial~~ and ~~then ~~it's ~~it'll work as well.

Similar idea. , But I hope that you learned a lot from this video. And thank you, and see you in the next one. [00:14:00] Bye.

