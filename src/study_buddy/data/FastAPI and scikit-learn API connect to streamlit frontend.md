FastAPI and scikit-learn API Connect to Streamlit Frontend

Hello and welcome to this video, which is a continuation of the previous video about FastAPI and scikit-learn.

In that video, we created an API to serve a scikit-learn model.

We created a Random Forest classifier and then dumped the model using joblib to save it.

After that, we used FastAPI together with joblib to load the model.

FastAPI created an API with different endpoints.

We had one GET endpoint where we could retrieve the data points.

Then we had a POST endpoint where we could create predictions.

The prediction endpoint required posting data such as:

sepal length
sepal width
petal length
petal width

inside a JSON object.

We tested it in the Swagger UI.

Then we also tested it in Python using a Jupyter notebook and with curl.

It worked correctly.

We could send data to the API and receive a flower prediction in return.

That is how far we came previously.

I’ll show you the code again shortly.

In this video, we will use Streamlit to create the frontend for this application.

In many tutorials, people create Streamlit applications directly connected to machine learning models.

For example, they use scikit-learn directly inside Streamlit.

But the problem with that approach is that everything becomes tightly coupled.

With our approach, where we place an API in between, the frontend becomes loosely coupled.

That means we can easily replace Streamlit with another frontend later on.

The frontend only communicates with the API.

That is the main idea.

I’ll demonstrate it using Streamlit, but you could use any frontend framework you want.

Let’s move on to Visual Studio Code and continue where we left off.

Here in Visual Studio Code, I’ll show you how far we’ve come.

First, I activate my environment.

Then I run:

uvicorn api:app --reload

This starts the FastAPI application.

If we go into the docs page, we can see the API documentation.

We have a GET endpoint.

If we try it out and execute it, we get back all the iris data points.

Then for the POST endpoint, we can send in a request body.

When we execute it, we get back a prediction.

For example:

predicted_flower: Iris setosa

This is where we left off previously.

Now I want to show you the API code itself.

Basically, we have a router.

We can create several endpoints using the router.

We also have request and response schemas.

These schemas validate the input data.

The values must stay within certain ranges.

The ranges were determined during exploratory data analysis when we created the model.

I expanded the ranges slightly beyond the original dataset.

Then we have the output schema, which is simply a string.

We use:

@router.get

and:

@router.post("/predict")

This is where the prediction happens.

The payload is received as an IrisInput object, which performs validation automatically.

Then we use:

model_dump()

to convert it into a pandas DataFrame.

We load the exported Random Forest model and call:

classifier.predict()

Then we return the prediction.

That is basically the entire API.

We also experimented with it earlier.

For example, we explored how the Pydantic model behaves with model_dump().

We also created pandas DataFrames from the payload.

And importantly, we used httpx.

We created a payload dictionary and used:

client.post()

to send requests to the API endpoint.

Of course, the FastAPI server must still be running in the terminal.

Then the API returns a response.

We checked:

response.status_code

which returned:

200 OK

Then:

response.json()

returned the predicted flower.

That is the overall idea.

Now we’ll connect a Streamlit frontend to this API.

We create a new file:

frontend.py

We import Streamlit.

Then we install Streamlit:

uv pip install streamlit

We also import:

httpx
assets path from constants

because we have flower images in the assets folder.

Now let’s create a simple title:

st.markdown("Predict Iris Flower")

Then run the frontend:

streamlit run frontend.py

Good.

Now let’s implement prediction.

We create a function:

predict_flower(payload)

Inside it we use:

httpx.Client(timeout=10)

Then:

client.post()

We send:

the URL
json=payload

The URL points to our FastAPI endpoint.

We also call:

response.raise_for_status()

and return the response.

Now think about the frontend.

We need fields where the user can input:

sepal length
sepal width
petal length
petal width

We can use:

st.number_input()

For example:

“Sepal length in centimeters”

We define:

minimum value
maximum value
default value

If the user enters values outside the allowed range, Streamlit shows validation errors.

The value returned from st.number_input() is already a float.

We repeat this for all four features.

Now we have four variables.

Next, we create a form.

Inside the form, we create a submit button:

st.form_submit_button("Predict")

When the button is pressed, it returns True.

If submitted is True, we create a payload dictionary containing:

sepal_length
sepal_width
petal_length
petal_width

Then we call:

predict_flower(payload)

and receive the response.

We display the response.

Then we extract:

predicted_flower

from the response JSON.

We convert it to lowercase using:

casefold()

Then we display:

“The predicted flower is ...”

We can also show the flower image using:

st.image()

The image path is built dynamically using the flower name.

Now when we press Predict, we receive both:

the flower prediction
the flower image

Very cool.

We can test several examples.

For example:

Iris setosa
Iris versicolor
Iris virginica

By changing the values, we get different predictions and corresponding flower images.

This is now our frontend application.

Now let’s discuss deployment.

Right now the frontend points to:

localhost

That means only my own computer can access the API.

If we want to share this application publicly, we must deploy the API.

One good option is Azure Functions.

Azure Functions are:

serverless
inexpensive
easy to deploy

Once deployed, Azure Functions provides a public URL.

Then we simply replace the localhost URL inside Streamlit with the Azure Functions URL.

After that, we can deploy the Streamlit frontend itself.

We could deploy it:

on Azure
or on Streamlit Cloud

If deploying to Azure, we would likely containerize the application first.

I may create another video later showing the complete deployment process.

In this video, we created a Streamlit frontend connected to a FastAPI application serving a scikit-learn model.

The scikit-learn model was developed separately in a Jupyter notebook.

Then we exported it using joblib.

After that, we loaded the model into our FastAPI endpoint.

Finally, we connected Streamlit and sent payloads to the API endpoint.

At the end, we also discussed how this architecture could be deployed into a real-world environment.

Thank you for watching this video.

I hope you learned a lot.

See you in the next one.

Bye.