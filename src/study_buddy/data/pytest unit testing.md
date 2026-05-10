# pytest unit testing

Hello and welcome to this video on unit testing in Python.

We’ll be using pytest.

That means we need to install pytest, and then we will use it to test our vector class that we created in the polymorphism lecture, where we implemented a lot of operator overloading.

We will use pytest to test different methods in the class and show you how to do unit testing.

There are many different methodologies for testing.

For example, one methodology is to write the tests before writing the actual code.

You create tests that initially fail, and those tests act as requirements.

Then you implement the code so that it passes the tests.

This methodology is called TDD — Test Driven Development.

However, in this lecture we will do it the other way around.

We already created the class and implemented the methods, and now we add testing afterwards.

This is somewhat simpler, but TDD is a very good methodology and I definitely recommend learning it.

Okay, let’s move on to Visual Studio Code.

Here I am in Visual Studio Code.

This time the project is not empty.

I already have the vector class from the polymorphism lecture.

If you haven’t watched that lecture, make sure to watch it.

Basically, we created a Vector class.

Using this class, we can instantiate vector instances.

The vector instances have:

* a numbers property
* **add** for addition
* **sub** for subtraction
* multiplication support
* **rmul** for reverse multiplication
* **len** to get the vector length
* **abs** for Euclidean norm
* validate_vectors
* **getitem**
* plot
* static methods
* **repr**

Now let’s set everything up.

First create a virtual environment:

uv venv

Then activate it.

On Linux/macOS:

source .venv/bin/activate

On Windows:

source .venv/Scripts/activate

Now install the required packages:

uv pip install matplotlib pytest

I don’t need ipykernel because I’m not using Jupyter Notebook here.

I’m working directly with Python scripts.

Now create a tests file:

touch tests_vector.py

Import the class:

from vector import Vector

Let’s quickly verify it works.

v = Vector(1, 2, 3)

print(v)

You can see the output:

Vector(1, 2, 3)

Good.

Now import pytest helpers:

from pytest import raises

Now we start writing tests.

All test functions should start with test_.

For example:

def test_init():

Create a vector:

v = Vector(1, 2, 3)

Then assert:

assert v.numbers == [1, 2, 3]

Now run:

pytest

You should see a dot:

.

A dot means the test passed.

Now let’s also test invalid initialization.

def test_invalid_init():

with raises(TypeError):
Vector(1, 2, "3")

This should raise a TypeError.

If the error is not raised, the test fails.

We should also test edge cases.

For example:

with raises(ValueError):
Vector()

Now let’s test addition.

def test_addition():

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

result = v1 + v2

assert result.numbers == [5, 7, 9]

This tests element-wise addition.

We should also test invalid addition.

For example:

with raises(TypeError):
v1 + 5

A vector should not be added to a scalar.

Now subtraction.

def test_subtraction():

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

result = v1 - v2

assert result.numbers == [-3, -3, -3]

Now let’s test length.

def test_length():

v = Vector(1, 2)

assert len(v) == 2

Now absolute value.

Remember:

**abs** returns the Euclidean norm.

For example:

v = Vector(3, 4)

The Euclidean norm is:

sqrt(3² + 4²)

which equals 5.

So:

assert abs(v) == 5

Now let’s test validate_vectors.

def test_validate_vectors():

v1 = Vector(1, 2)
v2 = Vector(3, 4)

assert v1.validate_vectors(v2)

Now test invalid lengths:

v3 = Vector(1, 2, 3)

with raises(TypeError):
v1.validate_vectors(v3)

Also test invalid types:

with raises(TypeError):
v1.validate_vectors(5)

Now let’s test **getitem**.

def test_getitem():

v = Vector(1, 2, 3, 4)

assert v[0] == 1
assert v[1] == 2
assert v[-1] == 4

Finally we test plotting.

For plotting, we should manually verify the visualization itself.

But we can at least verify that plotting executes successfully.

def test_plot():

v1 = Vector(1, 2)
v2 = Vector(2, 3)

v1.plot(v2)

assert True

The assert True acts as a placeholder confirming execution reached this point successfully.

Now when we run pytest, we should see all tests passing.

In this video, you have seen how to work with unit testing using pytest.

We tested:

* initialization
* invalid initialization
* addition
* subtraction
* length
* absolute value
* vector validation
* indexing
* plotting

Testing is extremely important because it makes your code much more robust and reliable.

Make sure you also commit and push your code to GitHub.

Thank you for watching this video and see you in the next one.

Bye.
