# How does LLM work?

[00:00:00] Hello and welcome to this video where we'll go into large language models and how do they work. We'll go into the theory and intuition about how models like chat, g, pt, Gemini, Claude, et cetera, how they work, the fundamental theory about it. ~~We will go into to get. ~~To give you intuition on how does it generate language, how can it understand language, et cetera.

This will be really interesting and hopefully that you'll get some intuition. You don't need to understand exactly the details, how it works. However, some basic intuition is good that you, you know that it's not magic, it's just mathematics and statistics. However, we won't go into much math and statistics

we will keep it simple and that you can understand it. Yes. Let's move on to the slides.

**Kokchun Giang-1:** how does she GPT and other language models work? An introduction to large language models? How can we start with [00:01:00] text? How can we represent text for a computer? A naive approach. Start to understand that the computer, it can only understand numbers, it can only understand zero and ones. We need to somehow represent.

The text into numbers that the computer can understand it. This is our starting point. Computer doesn't understand text. It understands numbers, which can be represented in binary as ones and zeros. We need to represent text with numbers. This is our starting point. Suppose our vocabulary has these words.

We have, Hey, ~~Canon ~~fis do, sorry, this is in Swedish, but these are just a few words in Swedish vocabulary. Then one hot encoded vector would look like this. Have a vector. This means that this represent hay. If this is our vocabulary, and then we have zero on all the other ones. This is just the [00:02:00] word, Hey, ~~hay ~~can be represented with this.

In Swedish there's 126,000 words. Then we'll have a very huge vector if we will represent it as in this way. This is a term based approach to represent the words. Then we'll have a one, somewhere to represent one word, and then zero everywhere else. Is this a good approach?

That is the question. Get the very, we'll, get the very sparse vector. That means that we have a lot of zeros and just one, one, but we also want to have some semantic meaning between the words. What does the semantic meaning mean? For example, we have the word hello and the word bi. They should be somewhat close to each other as both are about greeting.

How are you, maybe it should be close as well. While a rabbit and a dog should be somewhat close to each other as both [00:03:00] our pets, a rabbit and a hare should be closer than a rabbit and a dog because they may look. More similar, they have more features that are similar and fish and goldfish should be very similar.

This is what we mean with semantic meaning. This is not captured by using this naive approach as we will only have a one somewhere since we have a rabbit and a dog. They are quite. Far away from each other in the alphabet. Then it means that~~ they, ~~they're not related at all~~ in ~~in the naive approach, but we want to have them more relatable that we can start to get the grasp of the language to start model and understand the language.

Then we'll go further into embeddings. Then 2013 there was ~~a, ~~an article called Word to ve, how to Represent Words with Vector Embeddings that captures semantic meaning. This is a kind of the start [00:04:00] here. Here I have ~~a. ~~A Cartesian coordinate system where we have a size as a feature and we have loves hay as another feature.

This is just 2D but we could expand this to many dimension, but it's impossible to show it. We have here a tiger that ~~is, ~~has a large size, but it doesn't love hay. While we have a rabbit here that is smaller size but loves hay. Where does cow and calf go? That is the question. You can, for example, say that cow, it's quite large in size.

You can say two here. And then it also loves hay. It eats hay. While the calf, it's somewhat smaller in size, but also loves hay. You can see that, and they are closer. They are ~~close to they are in ~~in this place here. This is how you can represent them. These are vectors.

You can draw lines or you can draw arrow to these, and you get vectors. [00:05:00] However, we have larger dimensional embedding vectors of course, because these embedding vectors, they become larger and larger when you have more and more features. ~~If we could have more. Size and love, say we could have domesticated as one feature.~~

We could have for example, mammal as a feature we could have living in water as a feature, et cetera. We could have a lot of features. ~~We can have yeah, there's a lot. ~~To find similar words, we use a dot product, which gives co-sign similarity between the vectors. ~~We take we find the co-sign similarity.~~

The cosign similarity is basically just an angle. We ~~took, ~~take a look at the angles between two vectors and see which one is closest. That is the idea to ~~get then we ~~get the semantic meaning. We can also do an interesting thing is that we can do some calculations with the vectors.

We could add vectors and subtract vectors to get different types of results. That is quite cool. Moving on. In 2017, we have this paper. Attention is all you need. This is the [00:06:00] Transformers architecture, and this is what all language models are based on as of today. We start here, the goal is to predict the next word based on the previous sequence.

You have a sequence of words and you want to predict the next word that is the goal. For example, here in Swedish, there's who I lag it is how are you and who more do if there's two are, then there's lag. Who more than is do it is like, how are, how is. How are you? For this we need to understand the context through the attention.

For example, I am cool. The cool it refers to I, then it means that it's the coolness, I am cool. However, the ice cream is cool. It's referring to the ice cream. If it's referring to the ice cream, then this cool, it means something else. ~~Then this cool up here. ~~This cool [00:07:00] is referring to the person I, and this cool is referring to the ice cream where it's.

Cool as in low temperature. Depending on the context the same word could have different meanings. This is where the attention is. ~~All you need is very very neat. ~~Also here it goes away from previously it was used in RNNA lot recurrent neural network, but here it's go, it's removing that all along.

Here we compute similarities to see which words that determine the context for cool as it has different meanings in different contexts. ~~Computing similarities to see. The words. Okay. Similarities. ~~With the transformer, we can generate text word by word using previous words as contexts. It's jumping around and see the different similarities, scores and see that.

Okay. Is this one that will determine. Cool the most while death and is not determining cool as much. How does it know what is determining it? It depends [00:08:00] on all the training data that this has gone. You have sent in a lot of training data and it has learned this patents. Now we can generate text word by word using previous words as context.

For example, like this, I am cool. I am, and then it looks into its training data and sees like cool, appears a lot of time in the training data, and then it'll predict cool with the highest probability. Then afterwards it predicts the word yo because that is also very common in this training data set that I have thought about in my mind.

Then I am cool. Yo, it comes out. I'm cool. Yo Zap then it's yeah, depending on this training data set. As you can see this what it does is that it. Takes the sequence, send it in, and it'll predict. Cool. Then it'll send in this next sequence with I am Cool. It'll predict yo and we send in all this and then it'll [00:09:00] predict sap.

This is a little bit of simplification. It's not the really words that it predicts. It predicts something called tokens, but it's more more division of the word in different ways. But we don't need to go into that for simplicity. We'll think about it as words. Okay. Then we'll get a little bit further in time.

We get into GPT general pre-trained Transformers, and then this is trained with unsupervised learning on large corpus of text ~~is pre-training, it's trained on. The data ~~from the internet, basically. Using Internet's text, it can predict most probable next word to generate. Then when you train on much data, it become, it becomes something called emergent capability.

It's start to be able to find patterns ~~that you are not ~~that people are not sure about before. Then you can also add. Something called temperature, and we'll get variations and [00:10:00] creativity. What this means is that maybe ~~we don't need to pre, ~~we don't want to predict I am cool instead maybe it predicts I am super because super maybe was the third most probable word.

But since we have temperature, it becomes like, I don't need to pick the most probable word. I can pick some other word with some probability. The higher temperature it gets, the more ~~it. ~~It becomes more wild. That is to say it can pick other words ~~in its core, ~~in its training. Then ~~when ~~we can fine tune it to specific task using supervised learning that you can, for example, chat in a certain format.

You need to train it with a certain format that it should answer in this type of format. Here we have a supervised learning. Then in order to get it to become good to answer in a way that we want it answer, we have something called reinforcement learning with human feedback, [00:11:00] RLHF.

We let the model answer a set of question several times, you can generate a lot of different answers. We have different temperatures, we get different types of answers, and then we let. A lot of humans very lowly paid humans, unfortunately that will score these answers and feed back to the system how good these answers were.

The systems will try to maximize its scores, it gets scores, for example, it, you, it says one a type of answer and you give it back a score of four. But in a scale of 10, and then another answer, it gives seven another answer, five, et cetera, and it'll try to get the highest score all the time to satisfy the humans.

The system will try to maximize its scores. Example, an answer of how to make a bomb will get low scores, for example, and model will try predict which type of answers that humans [00:12:00] like. Then, after RLHF, ~~we have ~~we have come to the part of we have a chat, ~~GPT three point ~~GPT, 3.5. It's like the first chat, GPT to make it very simple.

I've skipped a lot, I've skipped some of the details. But this I think it's the intuition that you need to see that. Yes, now we have a model that we can chat with and ~~then ~~then there's a lot of different improvements in a lot of different models and and then a lot of variations as well that I haven't covered.

But I want to cover one more thing is that we want to make the model become more. Capable and understand more different things and ~~do ~~be able to perform different things. For example, we can send in a video and it'll understand it. ~~We, ~~it can produce a video, it can produce an image, we can send in an image and it'll understand that, et cetera.

How to do that is that we've gone into large multimodal models. LMM. Here LLMs [00:13:00] are language models and not good at, for example, math. It cannot do computation very well because ~~it's, ~~that's not its main purpose. Also it can't answer questions on things that happens after its training cutoff.

Then what you can do is that it can however, use tools to handle this. For example, we can use tools such as a calculator to do computations because that will be much better than using. The raw training data that we have, and we can use Google search to enhance our context.

We can get more context of the things that ~~is ~~outside of our cutoff or more specific things that it becomes visible for the model to use to generate an answer. We can have an image generator to generate image ~~when ~~when someone asks for an image. We can also send, when someone sends an image, we can use~~ i ~~other AI tools such as image recognitions to try to understand the image ~~to ~~to generate text based on it and et [00:14:00] cetera with video ~~et.~~

LMS can also process and understand other inputs such as video, image, audio, et cetera. You can talk to it, it can generate back speech with text to speech. And using the newer it becomes more and more natural as well ~~in, in the text. ~~In the speech. ~~Yes, I.~~

in this video we have gone through LLMs and how do they work and to get some intuition about how it works. We have gone into ~~some ~~some very brief concepts of different parts for an LLM to work and but not gone into all the details. Of course, there's too much and we have tried to skip.

Some of the math that it becomes quite simple to understand. Starting with like how to represent text and then going more towards training on how the attention works. Then going into training on the internet data to get pre-trained, GPT and then going further into supervised learning and reinforcement learning with human feedback that we [00:15:00] can get the chat.

Chatting format that we are used to and then moving further into ~~large ~~large multimodal lang models where it can be more capable to use different types of tools and understand different type of inputs and getting different types of outputs. I hope that you have learned a lot in this video ~~and ~~and see you in the next one.

Bye.

