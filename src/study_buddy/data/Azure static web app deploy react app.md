Azure Static Web Apps Deploy React App

Hello and welcome to this video on a React application that we will serve on Azure Static Web Apps.

This is a very simple way of deploying a SPA, a Single Page Application, because with React it will create some static files.

It'll create HTML, CSS, and JavaScript static files, and then these can easily be deployed in Azure Static Web Apps.

It's very simple, and I’ll show you how to do that in this video.

Okay, let's start in GitHub.

We’ll create a new repository.

Click the “New” button and create a new repository.

I will call it:

react-app-deploy-static-web-apps

Something like that.

I can make it public, that’s fine.

We can skip README and .gitignore.

Okay, create repository.

Now I have a repository.

Why do I need this?

I need this because I will use GitHub for deployment.

I will link my GitHub repository to Azure Static Web Apps so that it can find my React code, build it, and deploy it automatically.

Copy the repository URL and then go into your terminal.

Inside your terminal, navigate to where you want the project to be.

For me, it will be:

Documents/deployments

Then do:

git clone

and paste in the repository URL.

This means that we now have this repository locally.

You can either open it manually in Visual Studio Code or, if you have the code command installed, you can simply type:

code react-app-deploy-static-web-apps

and open it directly.

Now I opened it in Visual Studio Code.

Let’s create a new terminal.

Take a look and verify that you have Node installed:

node -v

Then:

npm -v

And:

npx -v

If they are not installed, search online and install them first.

Now let’s create a React app.

Run:

npx create-react-app cool-react-app

I will pause the video now and come back when it’s finished.

Yes, it’s finished.

You can see here:

npm start

to start it.

Happy hacking.

Cool.

Now let’s continue.

Go into the React app folder:

cd cool-react-app

Then run:

npm start

You need to be inside this folder.

Now you can see the default React application.

Very cool.

Let us change it a little bit.

Go into:

src/App.js

and create an <h1> element:

“So Cool App”

Go back to the browser and you can see:

“So Cool App”

Cool.

That is everything I want to do with this app before deployment.

Now I close it down using:

Ctrl + C

You can see that the webpage is no longer reachable because the local server has stopped.

Now let’s push this to GitHub.

Clear the terminal.

Then go back out if needed and run:

git add .

git commit -m "Initial React app"

To simplify things, I will only use the main branch.

Now push it:

git push

I committed it before, but now I pushed it to GitHub.

Let’s go into GitHub and check.

Here you can see my GitHub repository.

Inside src/App.js you can see the <h1> with “So Cool App”.

That is what I created.

Now let’s move on to Azure.

Here I am in Azure.

Let’s create a resource.

Search for:

“Static Web Apps”

Click on it and create a new Static Web App.

Choose your resource group.

If you don’t already have one, create a new one.

I will call mine:

apple-rg

Then choose a name for the Static Web App.

I’ll call it:

cool-apple

For the pricing tier, I’ll choose Free.

The Free tier is enough for hobby or personal projects.

Deployment details:

Choose GitHub.

Connect your GitHub account.

For organization, choose your GitHub account.

Then choose the repository:

react-app-deploy-static-web-apps

And branch:

main

The build presets automatically detected React, which is very cool.

It also detected that the application is inside:

cool-react-app

The output location is:

build

Remember, you can manually create this by running:

npm run build

But Azure will do it automatically for us.

What Azure creates is basically a GitHub Actions workflow file.

I’ll show that later.

Click Next.

Then choose your region.

For me, West Europe is closest.

This is mainly for Azure Functions, but we are not using them here.

Now click:

“Review + Create”

Then click:

“Create”

Now it’s deploying.

Deployment in progress.

Go to resource.

Here is the resource.

You can click on the URL to visit your site.

At first it may still show the default page because deployment is still running.

While we are waiting for deployment, let’s look into the GitHub repository.

Run:

git pull

This will fetch the workflow file that Azure created automatically.

Inside .github/workflows you can see a YAML file.

It says:

“Created by Azure Static Web Apps”

This is GitHub Actions.

This workflow makes it possible to automatically build and deploy the React app whenever there is a push to the main branch.

I won’t go through the whole file in this video.

Now let’s go back to the browser and click the URL again.

Now we can see:

“So Cool App”

You may notice one thing:

It says “App” with a capital A.

That is because I changed it locally before and pushed a new update.

CI/CD kicked in automatically thanks to the workflow file and GitHub Actions.

Now let’s change it again.

Inside App.js change it to:

“Cool App”

Save it.

Then:

git add .

git commit -m "Changed app"

git push

Now it deploys automatically again.

Go into GitHub Actions.

You can see the workflow running.

It built and deployed the application automatically.

That means we now have CI/CD.

Continuous Integration and Continuous Deployment.

If we refresh the website, we can now see:

“Cool App”

Very cool.

Every time we push to the main branch, it deploys automatically.

This was super cool.

We created our React application.

We pushed it to GitHub.

Then we created a Static Web App in Azure.

We connected it to the GitHub repository and the main branch.

Then we saw that Azure automatically created a GitHub Actions workflow file.

After that, we changed the React app and saw that it deployed automatically.

You can see that it’s very simple to work this way in Azure with Static Web Apps if you are working with modern frontend frameworks such as React.

If you want, you can also connect it to a backend using Azure Functions for serverless computing.

Then you could have a serverless backend connected to this frontend.

That is a really neat thing to do.

Thank you for watching this video.

See you in the next one.

Bye.