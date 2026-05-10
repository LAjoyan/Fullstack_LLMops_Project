Logistic Regression Theory

Hello and welcome to this video where we’ll go into logistic regression and use it to classify data.

Now we are talking about classification.

Previously, we talked about regression.

The difference between classification and regression is that:

In classification, we have discrete labels or classes.
In regression, we predict continuous values.

For example:

Classification:

class 1
class 2
class 3

Regression:

3.5
34.2
102.8

Classification predicts categorical outputs.

Regression predicts continuous outputs.

Both are forms of supervised learning.

That means we need labeled data — a ground truth.

This will be a theoretical lecture.

Logistic Regression to Classify Data

When we have labels, we are dealing with supervised learning.

Supervised learning can be divided into:

regression
classification

Regression works with quantitative continuous labels.

Examples:

house price
temperature
salary

Classification works with qualitative categorical labels.

Examples:

class A
class B
spam
not spam

Linear regression can handle categorical features, but not categorical labels.

That is very important.

Features may be categorical.

Targets cannot.

For categorical labels we need classification algorithms.

Encoding Categorical Features

Suppose we have a categorical feature:

Animal
rabbit
hare
fish

We need to encode these into numbers.

One-hot encoding works like this:

rabbit	hare	fish
1	0	0
0	1	0
0	0	1

This converts categories into numerical form.

Another approach is dummy encoding.

With dummy encoding, we drop one column.

For example:

rabbit	hare
1	0
0	1
0	0

The last row implicitly means “fish”.

This works because if both are zero, we infer the third category.

Logistic Regression

Now let’s model categorical labels using logistic regression.

Suppose we classify tumors as:

benign = 0
malignant = 1

We might use tumor size as a feature.

Small tumors are often benign.

Large tumors are more likely malignant.

If we used linear regression, the prediction line would not model probabilities properly.

Instead we use the logistic function, also called the sigmoid function.

The sigmoid curve looks like an S-curve.

It outputs values between:

0
1

This allows us to model probabilities.

For example:

probability close to 0 → benign
probability close to 1 → malignant

Values in between represent uncertainty.

The Logistic Function

The logistic function contains parameters such as:

w₀
w₁

These parameters are learned during training.

Training means estimating the parameters that best fit the data.

Once trained, we compute probabilities.

Then we apply a threshold.

For example:

If probability ≥ 0.5 → classify as 1

Otherwise → classify as 0

The threshold can be adjusted depending on the application.

For example, in medicine we may want a more cautious threshold.

Evaluation Using Confusion Matrix

Unlike regression, we do not use metrics like:

MSE
MAE
RMSE

Instead we use a confusion matrix.

The confusion matrix contains:

True Positive
False Positive
True Negative
False Negative

Suppose:

prediction = 1
actual = 1

Then we have a True Positive.

If:

prediction = 0
actual = 1

Then we have a False Negative.

If:

prediction = 1
actual = 0

Then we have a False Positive.

If:

prediction = 0
actual = 0

Then we have a True Negative.

We want high values on the diagonal:

True Positives
True Negatives
Accuracy

Accuracy is defined as:

(True Positive + True Negative) / Total

However, accuracy can be very misleading on imbalanced datasets.

For example:

Suppose most patients are healthy.

If the model predicts “healthy” for everyone, it may still achieve 99% accuracy.

But the model completely fails to identify sick patients.

So high accuracy does not necessarily mean a good model.

Precision

Precision is:

True Positive / (True Positive + False Positive)

Precision becomes important when false positives are costly.

Example:

Spam email detection.

A false positive means a legitimate email gets marked as spam.

That is undesirable because users may miss important messages.

So spam classifiers typically prioritize high precision.

Recall

Recall is:

True Positive / (True Positive + False Negative)

Recall becomes important when false negatives are dangerous.

Example:

COVID tests.

We do not want sick people incorrectly classified as healthy.

So we want very low false negatives.

That means high recall is important.

F1 Score

F1 score combines:

precision
recall

It is the harmonic mean of precision and recall.

F1 provides an overall balanced performance measure.

Regularization

Logistic regression also supports regularization methods such as:

L1
L2
Elastic Net

These methods penalize large weights and help prevent overfitting.

Hyperparameter tuning and cross-validation are also important.

Multinomial Logistic Regression

Logistic regression can also handle multiple classes.

For example:

Iris flower classification:

setosa
versicolor
virginica

The model predicts probabilities for each class.

Example:

0.7
0.1
0.2

We choose the class with the highest probability using:

argmax

So the predicted class becomes the one with the maximum probability.

Conclusion

In this video we went through the theory and intuition behind logistic regression.

We discussed:

supervised learning
regression vs classification
categorical features
encoding
logistic function
sigmoid curves
probabilities
confusion matrix
precision
recall
F1 score
multinomial logistic regression

These evaluation metrics are useful not only for logistic regression but for many classification algorithms.

I hope you learned a lot in this video.

Thank you, and see you in the next one.

Bye.