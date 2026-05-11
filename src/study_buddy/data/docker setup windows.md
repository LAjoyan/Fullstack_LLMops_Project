Docker Setup Windows

Hello and welcome to this video where I will go into installing Docker on my Windows machine.

For that, we will need to install WSL — Windows Subsystem for Linux.

Afterwards, we’ll install Docker Desktop.

When that’s done, we’ll do a test where we create an image from a Dockerfile and then spin up a container to verify that everything works.

So let’s move on to my Windows virtual machine now.

Here I am in my Windows machine.

Let’s open the browser.

I’ll use Microsoft Edge since I haven’t installed another browser.

Go to the Docker Desktop for Windows webpage, which is also linked in my GitHub repository documentation.

Download Docker Desktop for Windows.

I already downloaded it before, so I already have the installer here.

Double-click the Docker Desktop installer.

Installing Docker takes some time.

During installation, it may ask:

Use WSL2 instead of Hyper-V (recommended)
Add shortcut to desktop

I’ll keep the recommended settings and install it.

Now the installation has finished.

It says:

“Close and restart”

So I’ll do that.

Now I have restarted my computer.

You can see Docker Desktop here.

Double-click it.

Accept the agreement.

Then choose:

“Use recommended settings”

This requires administrator permissions.

Click Finish.

Now Docker starts.

You can skip the welcome screens.

Interesting.

It says:

“Docker Engine stopped”

Let’s see what happens.

It’s starting the Docker Engine.

Usually this is where it can fail if WSL is not properly configured.

But in this case it actually works.

That’s interesting.

Let’s open PowerShell.

You could also use Git Bash.

Run:

docker

You can see that the Docker command exists.

Now run:

docker ps

This shows containers.

You can see columns like:

Container ID
Image
Command
Created
Status
Ports

Now let’s check WSL.

Run:

wsl --list

You can see the Linux distributions installed.

If you see something like:

docker-desktop
default

then Docker Desktop has already installed WSL2 automatically for you.

Previously, when I installed Docker on Windows, I had to install WSL manually first using:

wsl --install

After installing WSL, you usually restart your computer and install a Linux distribution such as Ubuntu.

Then Docker Desktop connects to WSL2.

Sometimes Docker still won’t work because virtualization is disabled.

If that happens, you need to enable virtualization in the BIOS.

Some computers already have it enabled and some do not.

To enable virtualization, restart the computer and enter BIOS.

Usually this is done with keys like:

F2
F10
Delete

Search online for your specific computer model.

Then enable virtualization.

Luckily for me, everything worked automatically this time.

So first try installing Docker Desktop directly.

If it fails, then install WSL manually and possibly enable virtualization in BIOS.

Now let’s test Docker.

We’ll create a Dockerfile and spin up a container.

I’ll go into Desktop and create a folder called:

test-python-docker

Then open it with Visual Studio Code.

I trust the authors.

Now let’s open a terminal.

Create a new file called:

Dockerfile

Inside the Dockerfile I’ll paste some code from my lecture notes.

Let me explain what it does.

We start with:

FROM python:3.11

This means Docker downloads a Python 3.11 image from Docker Hub.

The image already contains an operating system and Python installed.

Next:

WORKDIR /app

This creates a working directory called /app inside the container.

You can think of the container as an isolated environment.

Then:

COPY . .

This copies everything from the current folder into the container’s working directory.

Next:

RUN pip install -r requirements.txt

This installs dependencies from requirements.txt.

So let’s create that file.

Create:

requirements.txt

Inside it, I’ll simply write:

pandas

Normally you would also specify a version number, but for simplicity I won’t do that here.

Next:

CMD ["python", "app.py"]

This means that whenever the container starts, it will run:

python app.py

So now we need an app.py file.

Create:

app.py

Inside it, I’ll paste a simple pandas DataFrame example from my lecture notes.

I’ll also print sys.version so that we can see the Python version running inside the container.

Now let’s verify the host system Python version first.

Run:

python --version

You can see I have Python 3.12.8 installed locally on the machine.

Now let’s build the Docker image.

You need to be inside the same folder as the Dockerfile.

Run:

docker build -t first-python-app .

The dot means:

“Build using everything inside the current folder.”

This takes a little time the first time because Docker needs to download layers and dependencies.

You’ll see messages like:

exporting layers
exporting to image

In the theory section we’ll later discuss what Docker layers are.

Now the image has been created.

Run:

docker image ls

This lists all Docker images stored in your system.

You can now see:

first-python-app

That is the image we created.

Now it’s time to run the container.

Run:

docker run first-python-app

You can now see output from the container.

It prints Python 3.11.

That is because inside the Dockerfile we specified:

FROM python:3.11

So even though the host machine uses Python 3.12.8, the container uses Python 3.11.

This demonstrates isolation between the host system and the container.

You can also see that the pandas DataFrame was printed successfully.

That means pandas was installed correctly inside the container.

Actually, pandas does not even exist on my local system.

If I try:

import pandas

locally, it fails.

This is really cool.

So now you have:

created a Dockerfile
built a Docker image
spun up a Docker container

The container stopped automatically because the script finished running.

However, if you run something like a web server, the container would continue running in the background.

Then you could run many containers together to build large software systems.

That is super cool.

Thank you for watching this video on setting up Docker.

See you in the next one where we’ll go deeper into Docker theory and containers.

Thank you.

Bye.