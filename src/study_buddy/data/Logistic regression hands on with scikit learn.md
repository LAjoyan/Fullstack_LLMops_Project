# Logistic Regression Hands-on with scikit-learn

Hello and welcome to this video where we’ll go into hands-on logistic regression with scikit-learn in Python.

Here we’ll do classification.

Previously, you learned the theory and intuition behind logistic regression, and now we’ll move into the code.

We’ll also perform some exploratory data analysis on the dataset.

Then we’ll train a logistic regression model and finally evaluate it using different classification metrics so that you can see how classification evaluation works in practice.

---

Before going into the code, let’s first find the dataset.

I’m on the website:

`statlearning.com`

specifically from:

“An Introduction to Statistical Learning”

Inside the resources section for ISLR Second Edition, we can find datasets.

We’ll use the dataset called:

`Default.csv`

Download the ZIP file containing all CSV datasets.

Inside it, you’ll find `Default.csv`.

---

Now I’m in Visual Studio Code.

You can see the `Default.csv` file.

If we open it in preview mode, it looks like a spreadsheet.

We have the columns:

* default
* student
* balance
* income

Our goal is to predict the `default` column, which can be either:

* yes
* no

---

First we set up the environment.

Create a virtual environment:

`uv venv`

Then activate it.

On Linux or macOS:

`source .venv/bin/activate`

On Windows it uses `Scripts` instead of `bin`.

Now install the required libraries:

* ipykernel
* scikit-learn
* pandas

We may install more later if needed.

---

Now create a new Jupyter notebook called:

`logistic_regression.ipynb`

Switch to the Python environment.

Import libraries:

* pandas as pd
* numpy as np

---

# Exploratory Data Analysis

We start with EDA.

Read the CSV file:

`pd.read_csv("Default.csv")`

Then:

`df.head()`

This is our dataset.

Now check:

`df.info()`

We can see:

* 10,000 non-null rows
* `default` and `student` are objects
* `balance` and `income` are floats

Now look at summary statistics using:

`df.describe()`

This shows:

* mean
* standard deviation
* min/max values
* quartiles

Now let’s inspect the target column.

`df["default"].value_counts()`

We can see the dataset is highly imbalanced.

Most entries are:

`No`

Very few are:

`Yes`

This is important later when discussing evaluation metrics.

Now inspect:

`df["student"].value_counts()`

This is less imbalanced.

---

Now let’s visualize the data.

Import seaborn.

If seaborn is not installed:

`uv pip install seaborn`

Now create a scatterplot.

We plot:

* balance on x-axis
* income on y-axis

Then we color by `default`.

We can see that people with higher balances have a higher chance of defaulting.

Now let’s create boxplots.

Import matplotlib.

Seaborn is built on top of matplotlib.

Create subplots for:

* balance
* income

against the default label.

The boxplots show:

* Higher balances strongly correlate with defaulting
* Income does not appear to matter as much

This gives us intuition about the dataset.

---

# Encoding Categorical Features

Now we need to encode categorical features.

We learned in theory that we can use:

* one-hot encoding
* dummy encoding

We’ll use dummy encoding.

Use:

`pd.get_dummies()`

on the columns:

* default
* student

Initially this produces columns like:

* default_yes
* student_yes

with boolean values.

To avoid redundancy we use:

`drop_first=True`

This is dummy encoding.

Then we convert booleans to integers:

`astype(int)`

Now the values become:

* 0
* 1

---

# Logistic Regression

Now it’s finally time for logistic regression.

Import:

* LogisticRegression
* train_test_split
* StandardScaler

We prepare:

* X = features
* y = target

Drop the target column from X.

Then split into:

* X_train
* X_test
* y_train
* y_test

Next we standardize the data using `StandardScaler`.

For training data we use:

`fit_transform()`

For test data we only use:

`transform()`

because the scaler should learn statistics only from the training set.

---

Now create the model:

`LogisticRegression(penalty=None)`

We disable regularization to keep the model simple and close to the original logistic regression formulation.

Then fit the model using:

* scaled X_train
* y_train

Now inspect:

* model coefficients
* intercept

These correspond to the weights in the logistic regression equation.

---

# Predicting Probabilities

Let’s create a test sample.

For example:

* balance = 1500
* income = 40000
* student_yes = 1 or 0

Then scale the sample using the scaler.

Now predict probabilities using:

`model.predict_proba()`

The model returns probabilities for:

* No default
* Yes default

Most samples have very low probability of defaulting.

---

# Evaluation

Now it’s time for evaluation.

Import metrics such as:

* confusion_matrix
* accuracy_score
* classification_report
* ConfusionMatrixDisplay

Generate predictions:

`y_pred = model.predict()`

Now calculate accuracy.

We get a very high accuracy score.

At first glance this may seem like an excellent model.

But is it really?

That is the important lesson here.

---

# Confusion Matrix

Create a confusion matrix.

When we visualize it, we can see:

* many true negatives
* very few true positives
* many false negatives

This is because the dataset is highly imbalanced.

The model predicts “No default” most of the time.

That produces high accuracy even though the model misses many actual defaults.

So accuracy alone is misleading.

---

# Recall, Precision, and F1 Score

Now we compute additional metrics.

Recall:

True Positive / (True Positive + False Negative)

Recall tells us:

“How many actual positives did we correctly identify?”

The recall here is very low.

That means the model misses many defaults.

Precision:

True Positive / (True Positive + False Positive)

Precision is somewhat better.

Then we compute F1 score.

F1 score is the harmonic mean of:

* precision
* recall

Instead of computing these manually every time, we can use:

`classification_report()`

This gives us:

* precision
* recall
* F1-score
* support

for each class.

We also see the same accuracy score as before.

---

# Conclusion

In this video we went through logistic regression using the `Default.csv` dataset.

We performed:

* exploratory data analysis
* encoding
* preprocessing
* logistic regression training
* evaluation

Most importantly, we learned that accuracy can be very misleading on imbalanced datasets.

Even though the model had high accuracy, it performed poorly at detecting actual defaults.

That is why we must also inspect:

* confusion matrix
* recall
* precision
* F1-score
* classification report

I hope that you learned a lot in this video.

See you in the next one.

Bye.
