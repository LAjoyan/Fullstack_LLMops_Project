# Azure static web app deploy react app

[00:00:00] Hello and welcome to this video on react application that we will serve on Azure Static Web app. ~~So we'll deploy it in Azure Static Web app. So ~~this is a very simple way of deploying a SPA. Single page application because with React~~ which ~~it will create some static files.

It'll create this H-T-M-L-C-S-S Java script as static files. And then this can easily be deployed in Azure's static web app. And it's so simple. We'll just show you how to do that in this video.

**Kokchun Giang-2:** Okay, let's start in my GitHub repository, or in my GitHub we'll create a new repository. So this new button here new repository. And here I will just call it Demo React App. Deploy. Yeah, something like this. Demo React app, deploy Azure I was called a static web apps. Yeah. It became a little [00:01:00] bit long.

I'll remove the demo. React app deploys static web apps. Yeah. Something like this. Yeah. I can't put it public. It's fine. And then we'll have a read Me get, ignore. We can skip that. Okay. Create repository. And now I have a re repository. Why do I need this? I need this because I will use GitHub for deployment.

So when I will link my GitHub repository and I'll choose link, my GitHub account, and I'll choose this re repository so that it can find my react code and then build it and deploy it into static web app in Azure. So just. Clone this one, copy it, and then go into your terminal.

**Kokchun Giang-3:** Inside your terminal, navigate to where you want to be. So for me, I wouldn't want to be in documents slash deployments. Okay. I'll put it there. Fine. And then we do. Get clone and you [00:02:00] paste in what you copied before. So you clone it in. And then this means that we have this repository. So you can either open up this studio code and file open to this repository.

Or you can do if you have this command installed and you can do code. And then you can see what it's called, react app. And then you do a tab for autocomplete. So React app deploy static web apps. Yes, it's this one.

So I opened this one in vicious Studio

Code so you can see in my vicious to your code.

Now increase this one and removing co-pilot. Okay, now let's create a new terminal and it's time to start. Okay? So take a look that you have node dash V that you have your node installed. NPN dash V [00:03:00] Yes, they're installed. NPX dash v. It's installed as well. So if it's not, install and install this.

So you can search Google search on it and find them. Okay. And now let's create a React app. So NPX create Dash, react dash app. And what should this be called? Cool react app. I will call it. Okay. So I will pause this video now and then come back when it's finished.

**Kokchun Giang-4:** Yes, it's finished and you can see here NPM start to start it and happy hacking. Cool. Okay, so let's continue now. Let's go. We have our Ulu React app, so CD into this one Ulu React app. Cool Ellis. And we will do [00:04:00] NPM start. So you need to be in inside of this folder. And then you do NPM start and you can see this is our React application.

Very cool. Yeah. And you, it's the default react application that started. So let us just change a little bit so that you can see. If you go into source after JS and let's just create a H one here and say, so Cool app.

Okay. And then we go back to our React app and you can see so cool app. Cool. Okay. So that is everything I want to do with this app before I'm finished. Okay. So I'll just. Close this down. Control C. So you can see that if I click on this one, I cannot reach the webpage. Good. [00:05:00] This means that it's not it's not open anymore.

Okay. Now let's push this to GitHub. So here I clear my terminal and what I want to do is CD out. Git at dot git commit dash MI will push it to my main my main branch and to simplify, I won't create other branches. I will just use the main branch. Okay? So I push this Cool React app, create that.

**Kokchun Giang-5:** Or, I have committed this, not pushed. So to push it just do git like this. Now I have pushed it to GitHub, so now we can go into GitHub to check.

**Kokchun Giang-6:** Yes. Here you can see my key type repository and you can see here is my React application. And you can see yes, this I haven't changed at all. But source, you can see app js and you can see here. So cool app in H one. And this is what I created. So [00:06:00] let's move on to Asher now.

**Kokchun Giang-7:** So here I am in Azure. So let's ~~create a Azure a resource. So ~~create a resource and you search for static web app. So here we have static web app, and click on this one ~~static web app, ~~and I will create my static web app. Okay, so you choose here your resource group. If you don't have one already for this, you can create a new one here and the one I will create, I'll call it.

~~Cool. Portfolio. Cool. ~~Cool Apple. That is quite cool. Okay. So cool Apple. And let's do it like this. Static web app details. Enter a name for your static web app, or actually this one I should not create let's see. Yeah, it may have created a new, actually this is the resource group, so Apple dash RG for resource group.

Okay. [00:07:00] So yes, I can see, yeah. Good. So cool. Apple Dash RG for resource group and then I will call the name for this. It's cool Apple. Okay. And for my tier, I'll choose free. So this is my free for hobby or personal projects. Of the standard is offering more things, but it costs. So we'll go with the free one.

Deployment details. Choose GitHub and the GitHub account. You choose your own account and here you can change account. So I have already connected to mine.

**Kokchun Giang-8:** Okay, so let's scroll down here. For organization, I'll choose ~~tion. It's ~~my own GitHub account, and then repository, I will choose here react app deploys static web app. So I'll choose this one.

**Kokchun Giang-9:** Yes. So here [00:08:00] the Repository React app, deploy static web apps and Branch Main. Yes, I only had this branch and then the build presets, it already detected React. That is very cool and ~~it protected that ~~it detected that it's inside this app application. Do slash ulu dash react dash app. Totally correct.

An output location is build. Remember, you can create this, build yourself by doing NPM run build. ~~But this is ~~it will do this automatic for us ~~when we. ~~When we create this one. So ~~it ~~basically what it does is that we'll have a workflow file inside of our GitHub. So it's ~~a ~~GitHub actions.

You'll see that I'll show that later on, but let's click on next here. Instead of deployment token, I'll have GitHub here and then next advanced, you can choose depending on where it should be West west Europe for me closest. But this is where Azure functions, and I'm not using that one here. So this is totally okay for me.

[00:09:00] And I will do review and create.

So it takes a little bit of time. ~~So this is a free, okay, ~~so click create.

And now it's deploying it's deployment in progress. Beautiful or beautiful and beautiful. It's not beautiful yet. I'll show you. Go to resource. Okay, so here is the resource and I can click on my URL. So visit your site, click here. Congratulations on your new site. It's not showing my site yet.

**Kokchun Giang-10:** In the meantime, when we're waiting for my app to be deployed let's look into ~~in my GitHub repository or ~~my Git repository, ~~I will, ~~I do the Git ~~poll ~~so that this will give me the workflows file. ~~So this is GitHub. ~~So this is GitHub actions, basically. So here you have this YAML file. You see this created by.

~~Get by ~~Azure static web apps. So here, [00:10:00] there's a lot of things that make it possible to create this react app and then~~ and then or ~~deploy~~ build ~~this react app ~~when ~~when there's a push to main, basically. Okay, so I won't go through this one.

**Kokchun Giang-11:** ~~Okay, take a look now. ~~Now I'm in a browser and let's click on this URL. Yes, it's a little bit weird. It's orange, ocean, blah, blah, blah, but click on this one. And yes, so cool app. And you may have noticed one thing. AP not a PP. Why is that? That is because the, I'll show you here in back in vicious Studio Code.

I changed it to AP and then CICD we're kicking in. Thanks to this workflows here. So this GitHub actions, what it does is that it will automatically build and deploy it. So what I did is that I pushed while waiting before I, I tried it and pushed a new change. So I just pushed it by Changing APE [00:11:00] and we can change it like this.

Cool app. Okay, so if I save this one. And I will do Git at dot git commit dash M changed app. Okay, Git push. So now it deploys. So we go back to the browser and I will close down this one. 

**Kokchun Giang-12:** So here I am in my browser in GitHub. So take a look into actions here. So when you push, two minutes ago, so I pushed I call the changed app. So you go into here and you can see what happens. It has built and deployed the job. So we have CICD, right? And then you can take a look into the React app.

So this is called Cool App Now. So that is really cool. So ~~it ~~it will deploy it automatically whenever you push it to main. So ~~this ~~now you have [00:12:00] CICD.

So this was super cool. We have created our React application. We have pushed it up to GitHub, and then we have created a static web app in Azure. This resource we have connected to our GitHub. To the main branch of our repository. And then we saw that it created a workflow file for GitHub action.

~~So we have CICD. ~~So then we changed our React app a little bit and we saw that it deployed a new application. And so it's super cool and you can see that it's very simple to work in this way in Azure with static web apps. If you are working with, modern frontend frameworks such as React.

And if you want, you can connect to the backend via, for example, Azure functions, so serverless computing and then you could have a backend that is serverless and connected to this frontend. So it's quite a need to do but thank you for watching this video and see you in the next one.

[00:13:00] Bye.

