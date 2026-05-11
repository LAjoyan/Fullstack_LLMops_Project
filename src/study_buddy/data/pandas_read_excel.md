# pandas read excel

Hello and welcome to this video with pandas where we'll go into actually reading from an Excel file. It is similar to when we're reading from CSV files later on, but now we will work with Excel files and you will see how that works.

Before moving on to Visual Studio Code, let's move on to the browser.

So here in the browser I'm inside Kaggle. This webpage is provided in the lecture notes that you can find.

When you're going in there, you should download this by clicking on the download button and also register if you're not registered, otherwise just sign in and download it. You will get a zip file, so just unzip it and take out the Excel file.

When downloading this, you will get both an Excel file and a CSV file. You can see this is the CSV file here. We will actually go into the Excel file here, because you will later work a lot with CSV files. So don't worry, you will learn how to use both of them.

So let's move on to Visual Studio Code.

Here I have put in the data. I have put in calories.xlsx. So let's read that in.

Choose the kernel. Here I have my virtual environment. I have installed the IPython kernel. I have installed pandas. That's it. The rest will install together.

Import pandas as pd.

We'll need matplotlib as well. Import matplotlib.pyplot as plt and we'll also need seaborn as sns.

Seaborn is used for plotting and it's very good for plotting DataFrames.

So let's install that using:

uv pip install matplotlib seaborn

Now we can read this.

df = pd.read_excel()

Let's find the path to this.

In Jupyter Notebook it's quite easy. It's relative to where the notebook is. The notebook is here, so the data folder is a sibling to this notebook file.

So you just type data/calories.xlsx.

Then you can do df.head() to find the first rows.

However, this will generate an error as you'll see.

The first time takes a little time.

Okay, so it says:

Missing optional dependency openpyxl. Use pip or conda to install openpyxl.

Let's do that.

uv pip install openpyxl

Done.

Let's rerun this.

Yes, and it works.

Whenever you don't specify which sheet to use, pandas will pick the first sheet.

We can go into this Excel file to see how it looks. It actually only has one sheet and you can see that it's in tabular form. Excel is a tabular format.

Similarly, when you read it into a DataFrame, it's also tabular.

Using df.head() we get the head of it.

We could do df.head(10) and get the first ten rows.

We could do df.tail(5) to get the last five rows.

That's a little bit about head and tail.

Usually when I start reading some Excel file or CSV file, I want to understand the dataset. To understand it, you usually do some kind of exploratory data analysis.

However, I won't do a complete EDA here. I will just start a little bit so that you can see how I'm working with it. Later on we'll go into more depth regarding EDAs.

So let's do df.info() to get some info.

You can see DataFrame is an instance of the pandas DataFrame class. In this instance it has a method called info. That's why we use parentheses.

tail is a method, head is a method, and info is a method.

Now you see how useful it was that you studied some OOP, so you understand how different libraries work.

df.info() prints this out.

You can see different columns, number of non-null values, and data types.

If some counts are smaller than the total number of entries, then you know that we have null values.

We see the data type object. Object is the most general data type.

Usually when you have strings, lists, or dictionaries, they are represented as objects.

For example, under "per 100 grams" we see values like 100 g. The g makes it a string, so pandas infers it as a string when reading it into the DataFrame.

With object data types we cannot do arithmetic operations like addition or subtraction, so we need to change them to other data types. We need to cast them.

For example, we can cast this to integers so we can do summary statistics on it.

Moving on:

df["food category"]

This gives a Series.

You can see different food categories and you can see they are repeated.

We can find the unique ones using .unique().

If you only do .unique without parentheses, you just get the method itself.

Now we get an array of all unique values.

Let's also check df["per 100"].unique().

We get:

100 g
100 ml

So now we know this column is used both for solids and liquids.

Now let's do some data cleaning.

We should have a strategy.

My strategy is:

* change column names
* convert calories per 100g to integers
* separate liquids and solids into different DataFrames

Usually your strategy depends on your goal and what stakeholders or domain experts want.

Let's rename columns.

First do df.columns.

Then use df.rename().

Nothing happens because rename returns a new DataFrame.

So we reassign:

df = df.rename(...)

Now it persists.

Next, let's fix calories.

We see values like "224 cal".

We can use string slicing.

But to work element-wise we need .str.

Using .str allows vectorized operations, which are much faster than looping through rows manually.

Never loop through a DataFrame unless absolutely necessary.

Now cast to integers using .astype(int).

Now the dtype is int64.

Next, separate liquids and solids.

Using value_counts() we get counts for:

100 g
100 ml

Liquids:

liquids = df[df["per_100"] == "100 ml"]

Solids using query syntax:

solids = df.query('per_100 == "100 g"')

Now let's find top five foods with highest calories.

Use sort_values(by="calories", ascending=False)

Then use .head() to get the top five.

We can do the same for liquids.

Now let's group by category.

df.groupby("food category")["calories"].median()

This gives one median value per category.

Sort it using sort_values(ascending=False).

Take top five using iloc[:5].

Reset index using reset_index().

Now let's plot it using seaborn.

sns.barplot()

This looks a little ugly, but it's a simple example.

Now instead of copy-pasting plotting code multiple times, use loops.

Create subplots with:

fig, axes = plt.subplots()

Create lists for titles, DataFrames, and x columns.

Then loop through them.

Finally save the figure using:

fig.savefig("figures/calories.png", bbox_inches="tight")

That saves the figure correctly.

We will come back to plotting later on, so don't worry if this feels new.

Thank you for watching this video.

You learned about DataFrames, reading Excel files, and processing them.

See you in the next one. Bye.
