# docker setup windows

[00:00:00] Hello and welcome to this video where I will go into installing a docker on my Windows machine. And for that they will need to install WSL, so Windows subsystem for Linux. And then afterwards we'll install the Docker desktop. And when that's done we'll do a test to, create an image from a docker file and ~~then ~~then from that will spin up a container to see that it works. So moving on to my windows virtual machine now.~~ So ~~here I am in my Windows machine. ~~So ~~let's go into the browser. Microsoft Edge, for example. I haven't installed another browser, so I will use this one. ~~So here let's down go in. So ~~you go into this web page, which is also in my GitHub repo, the documentation. ~~So ~~here you find ~~desktop ~~docker desktop for Windows, and I'll pick this one.

And you download it. Yeah, ~~this goes quite quickly, but ~~I have downloaded this before. So I have it here the Docker [00:01:00] desktop installer. So just double click this one.

~~So ~~when installing this, it will take some time. However, it won't work for you immediately ~~when you install it. ~~So it says ~~like this, ~~use WSL2 instead of Hyper V recommended and add shortcut to desktop. So I'll just install this one.

~~So ~~now my installation has finished. ~~So ~~it says ~~here~~ close and restart. So ~~I will, ~~I'll do that. ~~So close and restart. ~~

Okay. Now I've restarted my computer and ~~we'll see that ~~you see that there's ~~a ~~ Docker desktop here. So I'll double click this one

and you can see that. Okay. Just accept this one, read it through and accept it.

And here finish setting up Docker use recommended settings requires administrator password use advanced settings. I'll use recommended. So finish.

Okay. Welcome to Docker. Just skip this one. And yeah, you can skip this one as well.[00:02:00] 

So Docker engine stopped. This is interesting. So let's see what it says here. ~~Starting dock, ~~starting the docker engine.

I think it will fail.

Oh yeah, it's waiting, but I believe it'll fail. Okay, so I'm back here and we can see that we have this ticked on. So use the WSL two based engine. Let's go back to Docker. So here it actually works that is quite interesting. However usually. I think it works. Let's try a PowerShell here so you could do this in git bash.

So just write docker and see what happens. So you have a docker command. Okay, cool. Docker ps to see the containers. So you have container id, image, command, created status, ports, etc. ~~Let's see, because it usually requires WSL, . Oh, this is quite cool. ~~Actually, I looked at it. [00:03:00] So I went into PowerShell and I wrote WSL dash list. You can also do that. And if you see that the Windows subsystem for Linux distribution and it says Docker desktop and default, it means that actually Docker desktop has installed this for me before~~ when before like last.~~

~~Here, I think~~ when I installed ~~the ~~docker in windows, ~~then ~~I needed to install WSL~~ by the f ~~first. So I installed WSL through a command called WSL dash install. So then after installing that. Then you need to like restart, you install some Linux distribution, for example, Ubuntu.

And then~~ after you have done, ~~after I've done that, ~~if it works then ~~I installed Docker desktop and ~~then ~~it will connect to my WSL too. ~~And, ~~but~~ there, ~~there's also a chance that it doesn't work. And then it has to do with~~ how ~~the setting of your computer. If you have hyper V if that is enabled or not, and if it's not enabled, ~~then ~~you need to go into the BIOS [00:04:00] and ~~set so that you ~~allow virtualization.

So that might happen in a windows computer. ~~So ~~some windows computers, it's already set some it's not set. So then you have to do it yourself by going into the BIOS ~~and. Doing that ~~in order to do that, you need to restart the computer. And I think it was F2 ~~that you click ~~or F10 search it up, how you go into the bios and how you enable~~ the how you enable, uh, ~~what's called virtualization?

Yes, search that up in case you need to do that. Otherwise was surprised myself that it worked directly. So I'm very happy for that. ~~So ~~what you should do. Is ~~to ~~try ~~out, ~~to install Docker desktop as I did~~ just install it ~~and see that it installs WSL for you. But if it doesn't and ~~that ~~there's an issue, then you need to install WSL yourself ~~and~~ and maybe fix virtualization.

Yes. So now let's go on to test it out. So let's create a Docker file ~~and ~~and spin up a ~~com ~~container. ~~Okay, so now it's time for us to test out Docker. ~~So I can go into, let's see, ls, I will go [00:05:00] into desktop. ~~And ~~I'll ~~just ~~create the folder ~~here~~ called ~~test docker test, let's see, ~~Python docker ~~like this. ~~So I've created a folder and I will open this folder with code test Python docker.

Okay, so I've opened this one with Visual Studio Code. Yes, I trust the authors. Now, increase this one. ~~Yes, so here, ~~let's open up a terminal, new terminal.

Okay, so I will create ~~a new file. I will do like this, ~~a new file called Dockerfile.

So in the Docker file, I will ~~just~~ copy in the code from my lecture notes. So basically I can explain what it does. So it takes from Python ~~three point ~~11. So it'll take an image that is published in Docker hub, and then it will install the operative system for that it's a Linux distribution.

And based on that, it will install ~~this ~~Python [00:06:00] 3. 11. ~~And then ~~from this image, ~~we have~~ we have a working directory ~~so that I go into ~~the app folder of ~~this ~~this system. ~~So ~~you can see it as an isolated environment, ~~right? And ~~inside ~~of ~~this isolated environment, we have a folder in the root directory ~~that is ~~called app which I've created now.

with this Workdir app. And then I will copy dot. It means I will copy everything from this folder. ~~Into everything ~~into my working directory folder. So everything will go ~~into~~ into the app folder of the docker container. But we will go in later on to investigate that, but this will just test out that it works.

And then I will do run pip install dash R requirements. txt. It means that I will install based on my requirements. txt. So I will create the requirements. Let's do that. Requirements. txt. ~~And ~~what will I put here? I'll just put in pandas to show that it actually installs something. ~~So ~~usually you also, ~~you ~~put in a version ~~also, ~~but for [00:07:00] simplicity, I won't do that.

And then it will do CMD. It's a command that it should run whenever I run this Docker container. So when I spin up this container, this command will run. So what command do I want to run? I want to run Python ~~comma ~~app. py. It means that I will run Python and app. py. And that means I will have ~~a, ~~an app called app.

py. So I'll create that app. py. And inside of this one, I will ~~just I'll ~~just put in from my lecture notes.

~~So I will put in let's see. ~~So this is from my lecture notes. ~~So ~~it's just a simple pandas data frame that we create mock data. And then we also print out the sys. version to ~~see so that you can ~~see the Python version so that it differs from the system. ~~So ~~save this one. ~~And then I will, ~~first of all, I'll do Python dash version so that you can see which version I have.

So I'm in 3. 12. 8. This is the one that is installed in the host system, right? So it's installed on my [00:08:00] computer or on this virtual machine. ~~And then I will do like this Docker. So then I will, ~~I need to be in the same folder as my docker file. ~~So then ~~I will run docker~~ build dash R require, or not the dash R, ~~build and dot ~~basically, ~~or I need to have a tag actually.

I will do a tag to give it a name. So I will call it first Python app, like this, and then dot to show that it's this folder and everything inside of this folder. So I'll run this one, then it will build the image.

Yeah, ~~it takes for the first time, ~~it takes a little bit of time but then afterwards, when you have the image, you can use the image to spin up a container. ~~So you see exporting to image, exporting layers ~~in the theory section, you will understand what these terms mean.

[00:09:00] So now it's installed. ~~So let's see Docker. So ~~if I run Docker image LS, then I will see all the images ~~that have been that, ~~that are stored in my Docker desktop ~~or in~~ or in my system. ~~So ~~we can see ~~that ~~there's. First Python app. ~~So ~~this is the one ~~that ~~I created, ~~so ~~25 seconds ago. ~~So ~~let's run this one.

~~docker run and then, let's see, run,~~

Okay. So now it's time to run the container and it's quite simple. So you just do this Docker run and the name of the image that you want to spin a container from. ~~So ~~first I turn flash app basically like this. And you can see that. Oh, cool. We have three 11 written out. That's because I used here from the Docker file.

We have from Python 3. 11. So this is you can see that this isolated from the host environment. [00:10:00] So also here you can see that the data frame was printed out. So it worked with the installation because I installed pandas, right? Actually, I don't have pandas in my system here. So if I run, for example, if I run Python.

If I do import pandas you can see that it doesn't exist. ~~This is so cool. ~~So ~~you now you have spinned up if you have come this far you have spinned up a docker ~~you have created ~~an docker ~~a docker file ~~and from the docker file you have ~~Built a docker image and from the docker image just spin up a container, but actually the container has closed itself because it's finished running.

~~But ~~however, if you're running, ~~for example, ~~a web server, ~~then ~~it will continue to ~~run in a run and you can have it ~~run in the background. ~~So then you could have a several. ~~You can have several containers to build up a huge system of softwares and then this is super cool. So thank you for watching this video on setting up Docker and see you in the next one.

And we'll go in more into details of theory and going into the Docker container ~~to see ~~to learn more. Yes. Thank you. Bye.

