# PydanticAI fundamentals - outputting structured pydantic model

[00:00:00] Hello and welcome to this video on ENT AI fundamentals. I've been waiting for making this video. This is about a very nice framework for working with agents, working with LLMs. Creating chatbots, creating rags, et cetera, ~~creating ~~just to make LMS output in a structured way, which is really the essential parts of working with LLM and ~~lms ~~APIs.

Without having structured outputs, then basically it's not very useful. Edan ai, it's developed by the team behind Edan, and if you have followed my videos before, you know how much I love Edan and Edan kind of makes Python into the very structured world, making it really nice to work with.

Let's move directly onto the code and I'll show you how to get started with p ai.

**Kokchun Giang's video recording:** here I'm in Visual Studio Code. Let's start with Git not [00:01:00] Git~~ UV ~~in it. And then I will do or main PI, because I don't want that one. And then I will do UV add pi, D dash ai. What else do I need? IPI kernel, because I work in Jupyter Notebook. , This is a good starting point. Yes.

And it's done good. And then I'll touch den ai. I will call it underscore P under model the type B, because we'll use den AI to produce den model. That will be quite cool. This would be called construct gigantic model from text input. , Text input is quite unstructured. The result from the LLM is quite unstructured, let's make it structured using.

Edan. Here I will change my Python environment to [00:02:00] Edan ai. And then I will, since I will work with Gemini inside of Edan ai, I will choose the Gemini model. I will have a do ENV here. ENV. However, you can choose whatever model you want because that's the beauty with den ai, that it's model agnostic.

You can choose to have whichever model you want. I choose Gemini because it has a very nice free tier and also it's quite capable model. Here I will just call it Google API key equals, and here I will paste in my. API key, but of course I won't show it to you, I'll pause the video and do that.

**Kokchun Giang-1:** . I put in my ~~A ~~API key and let's get started. ~~We need to do from, or actually I need to change this to Python. ~~From Python, I can actually close down my terminal from Python, ~~the, and like this p ai ~~import agent. ~~Agent. , This ~~this is the agent class which we'll be [00:03:00] using, agent equals to agent.

And here you put in which model you pick. ~~The model, ~~I'll pick Google, and here you can ~~see's ~~several ones. I'll pick this one 2.5 flash, and here I'll do result equals to await agent ~~one. ~~And I will put in a prompt. Give me an IT employee working in Sweden. Keep it short. .

Something like this and we'll take a look into result.

Set the Google API key. Yes, I think I did that. In the environment variable. , Restart. Run again. Now it should find ~~it, I think if it doesn't find, yeah, it finds ~~it. Here you can see output Elara Nielsen DevOps engineer in Stockholm, Sweden. , That was short and nice. The agent run results you can probably take a look into that [00:04:00] one.

~~It's , ~~here you can take a look into results dot output.

**Kokchun Giang-2:** Results dot output, and let's see, results, ? , You can see here the output. We get the actual result here, and this one is nice for printing. And here you can see the results. , Let's make it a little bit different. Now. We want to make it structured. This is somewhat, it's unstructured.

Let me show you some other things some way to make it structured. We take from P. Import base model field. And here I will make a class called employee or employee model. And this is a base model. And here we'll have name as string. We'll have say H as in what else do we have?

Salary. We have it as in, and I will have a I will have a limit here. It has to be [00:05:00] greater than. 30 K. But it has to be less than 50 K. It's Sweden. They don't pay much. , Position is a string and results equals to a weight agent run. . Now I'll put in my prompt. Give me an IT employee working in Sweden.

. And I'll have here output type equals to employee model, and then I will have the results.

Now you can see agent results and it's very structured, you can take a look into this one. We can take results dot output, and this is actually an employee model, this is a pedantic model that is really good. For example, we can do like this employee equals to this result output. And we can do [00:06:00] employee we can take out like employee do.

Lemme change this to Python, employee.name and, oh, we have Bjorn. We have employee dot h we get the h employee dot position and you get the position. That is quite cool. It was quite fun that it called it Bjorn and not Bern, but that is fine for me. , Let's continue. We can have, for example you have this employee, ?

You can as easily, because this is a model we can do like dot model dump and you get it into dictionary. And if you want to have a adjacent string, you can as easily do like model jump, Jason, and now you have it as a Jason's drink. That is quite cool. And for this you can, for example, you can do inden equals two if you want.

And then you have some [00:07:00] indentation and it looks weird, but if you print it, it doesn't look that weird. It looks nice like this. There, there's a lot of opportunities while when you have it all, when you have it in a edan model based model. Let's continue and let's, for example, we want to have.

Several employees. We can do like this say like this several employees or list, or a list of employees. To simulate this one, we can do, like this result equals the await agent run. It's, that's why we'll do awai. . Give me 10 employees in. AI and data engineering fields. The like I can say like roles can vary, but salary must be between.

Let me do multi-line string [00:08:00] instead, I can cut this into several lines. ~~. Multi. ~~Must be between 30,000 and 50,000. . That I don't run into an error because of validation. We'll have output type equals to list of employee model, as simple as that. ? And then we can have results dot output.

This is our ~~employees. ~~Employees

and yes, it takes some time for it to run. It needs to call the API and then it needs to create this. Cool. We get 10 employees, to check that we have length of employees, that is 10. We can, for example loop through them. If we want to have all the names and all the ages, that is fine. Four employee in employees, we could print [00:09:00] out employee.name and we can do like an F string here.

Enhanced F string equals to and salary. Employee dot salary. Salary equals to, and here you can see, yeah, employee name. This and the salary are this. Cool. That is really cool. , Let us create some more advanced model. A more complex model, I'll call this a CV model. CV or a resume model.

. A more ~~are ~~complex and nested model. For a cv, you could, for example, have like class. We could have like CV model, it inherits from base model. We start with the [00:10:00] model. We have name string. What else do we have? ~~Inch H ~~inch experience, experiences. This is ~~the ~~list of experience. ? This is a list of experience model.

We can say it like that. And ~~then we have educations. They, it's a list of education model. . ~~Then it requires us to create this experience model and education model. Class experience model. It is a base model as well. And here we can, for example, have title string. We could have company string, we could have description string, we could have like start year in, we could have like end year, it's an ink as well.

. And then I will copy this one and I will make not experience model, but education model. . And education model. What do we have? We have [00:11:00] title as well. We have education area. We could have a description. We could have a school string. . Start here. End here. Yeah. Cool. Now you can see this started to become more advanced.

The CV model. It has a name and age field, and then it has experiences and education. Of course, we can add some validation as well for age and name, et cetera. However, I will skip that. Instead, I will use this to actually to use our model into it. Await agent run. Create a a, like a Swedish person applying for a data engineering position, something like this.

Yeah. And we can say we need to do output type is the CV [00:12:00] model. Then we can have result that output this one should be equals to the to the person or the Yeah. Person person or the resume. I will call it resume. Resume. Like this. . Perfect. Now we have a resume named Astrid Ian. ~~. That is very.~~

Real I guess. We have a resume dot name and you can see Astrid re copy this one. And we have resume dot h. . 30. Resume dot experiences. Actually, I can put it in another cell. And you can see this is a list of experiences to experience models, ? You can pick out like the zero of one, for example, and we can take, do.

Title, for example, and you can see data engineer. , Yes, we can explore [00:13:00] it further. And basically this is quite cool already, but I can show you something like this is optional or it's good to know how to do some. I'll call it optional post processing. There's a lot of things you can do, but I will do some, I will load into load into Duck db and unless it's, that is the idea that I will do.

I will create my terminal and I'll do UV ADD DLT db. I will install this one. , That is it I think. Yes, import, DLT. If you have followed my videos before in data engineering, you know what that is. But if you don't, it's data load tool. It's good for moving data from one place to another place.

And my idea is that I want to move my. Results data into D db [00:14:00] basically. What I want to do is pipeline equals to DLT pipeline, and here I will have pipeline name equals to CV json ~~ddb. . Yeah, destination. Actually I have. Cv, Jason ddb, or I can call it like resume Jason ~~ddb. Destination dlt, DO destinations, DDB and DLT destinations.

Dotb and I will pick with the name CV duck db B. . Comma data set name. I would do staging because here's the landing zone of the data. And info equals to pipeline. Do run data equals to a list. A list of what? List of this resume because we need to send resume, do model dump.

Because if you take a look into, for example, resume is this one, ? We can do that. Model done. And this [00:15:00] is the. Dictionary, I won't show all of it here. Or I can do laptop keys that keep it shorter. . Here we have the data in dictionary, and then we need to take the loader file format.

And this is J lines. J, l. And then we need to have a table name as well. Table name equals to CV entries, and then print info. Yeah, print info. . There is some issue here. Perhaps I forgot the comma. Yes, I did indeed. Yes. Now pipeline has ran. You see that? There's the CV Tech DB here, let's connect to that one we can.

Import duck DB and we can do with duck db. DO connect and we connect to CV duck DB as con. And what you can do is to [00:16:00] do desk equals to con SQL S sgl cvb, for example. DF DF like this and we can take a look at the desk parser error CV db. . Dv. Do connect cv, dob? Yeah.

Wave TB Connect. Yeah let me post the video and debug.

**Kokchun Giang-3:** . The issue was that I had CVB there, I changed to desk, which I want to, and here it says No MOD in mpi. ~~What you just, ~~what you need to do is UV add pandas, because that will give us MPI as well. We need pandas four DB to change to F, ? Here I run this one and you can see the desk.

It will run. Let's see. Yeah. And here you can see in the staging schema we have a lot of tables. However, it's this free that we want. We want CV entries, [00:17:00] educations, CV entries, experiences. This is how DLT loads it and unn the data. What we should do is I want to do CV entries equals two.

Act. Yeah. And then I want to do educations equal to, and I want to do experiences equal to. . And here I want to do

here shift command out down button to do this. And now do con SK. L. Parenthesis, and I'll do from staging.cv entries.

And here I will use these two underscore E. And then here is educations experiences. And then I will do.

Let's see, DF [00:18:00] parenthesis. Perfect. And this one needs to have remove the space. Otherwise, I think it's quite nice. . And now I have these other ones as well. What I can do is, for example, we have CV entries. You can see it's name, age, and DLT load can continue here. What else do I have? I have educations.

And here you can see these are the medications that I have. And what else do I have? Let's see. Experiences. ~~And here are the experiences that they have. ~~And for example, I can join them together. Then I could do like deck db dot sql, and here I will have multiline string. Let's see.

And select.

~~Select ~~from CV entries and if I want to join them together, it's quite cool that we have DLT here. You [00:19:00] see we have DLT parent id. All this parent ID ~~co ~~corresponds to this DLT ID because remember the Jason that we got, it's nested, ? And it's based on, this CV entries is the parent, and inside there we have educations and we have experiences.

. If you want to join them together, then we have the DLT parent id, we can have ~~left join, ~~left, join let's say education, E on cv, dlt, id I would call this cv. CV equals two. E Parco parent, DLT parent id. And then I will copy this one. Let's see. This is experiences e, X, and instead of EI have EX here.

And then basically now I will just copy in [00:20:00] the columns because I don't want to type it out again. It's a lot to type out, but basically this is what I copied in. These are the columns that I pick. And here you can see, we can do DF. And now you can see a data frame where we have this person, Astrid Ling, has been working for Eon, Spotify.

Spotify. And here ~~you can see. ~~You can see , we have experience description, experience start year, experience end year. And then we have title for the education area, et cetera. Oh, they chose the Swedish ones. Cool, cool. . That was cool. Remember now to. Commit ~~and ~~and push your code to GitHub, but make sure that in your gi nor that you are ignoring ENV that your API key don't come with it.

, cool. We have used P AI and learned some fundamentals of it and used it together with p to ~~make it ~~make the output structure. This is the goal. You want to have [00:21:00] output that is structured because there's a lot of things you can do with it. For example, you can do some post-processing as we did to put it into duct DB if we wanted to.

And afterwards, just do some different joints. Of course, you can choose Drdb, but of course you can choose no scale, which may be more suitable for this case. For example, MongoDB for a document database. But the thing is we got it into structured model. We got it into Edan model, and then you can do things after it.

Normal text input into a edan model. Thanks to Edan ai. ~~I think I said DentiCal a little bit too much. ~~I think I will end this video now and in the next video we'll go into using den AI together with fast API to create an API to create different API endpoints and take use of identity ai.

This is super cool and see you in the next video. Thank you. Bye.

