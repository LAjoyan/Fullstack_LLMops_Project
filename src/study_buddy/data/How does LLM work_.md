How Does LLM Work?

Hello and welcome to this video where we'll go into large language models and how they work.

We’ll go into the theory and intuition behind models like ChatGPT, Gemini, Claude, etc.

We’ll cover the fundamental ideas behind how these models generate and understand language.

This will hopefully give you some intuition.

You do not need to understand every detail of how these systems work.

However, some basic intuition is useful so that you understand that it is not magic — it is mathematics and statistics.

We won’t go too deeply into math and statistics though.

We’ll keep it simple and intuitive.

Let’s move on to the slides.

How Does ChatGPT and Other Language Models Work?

An introduction to large language models.

Let’s start with text.

How can we represent text for a computer?

A very naive approach is to remember that computers only understand numbers — ultimately just zeros and ones.

We somehow need to represent text as numbers so that the computer can process it.

That is our starting point.

Computers do not understand text directly.

They understand numbers represented in binary.

So we need numerical representations of words.

Suppose our vocabulary contains words such as:

hej
kanin
fisk
hund

These are Swedish words.

A one-hot encoded vector could represent them.

For example:

“hej” might be represented as:

1, 0, 0, 0

while all the other positions are zeros.

In Swedish there are roughly 126,000 words.

That means the vectors become extremely large and sparse.

A sparse vector means there are mostly zeros and only a single one.

This is called a term-based representation.

But this approach has a problem.

It does not capture semantic meaning.

What do we mean by semantic meaning?

For example:

“hello”
“bye”

should be somewhat related because both are greetings.

Similarly:

rabbit
dog

should also be somewhat related because both are pets.

Rabbit and hare should be even closer because they are more similar.

Fish and goldfish should also be very close semantically.

The naive one-hot approach cannot capture this.

Words become unrelated simply because they are located far apart in the vocabulary ordering.

We need a representation that captures relationships between words.

Then we move into embeddings.

In 2013 there was an important idea called:

Word2Vec.

This introduced vector embeddings that capture semantic meaning.

Imagine a coordinate system with features such as:

size
loves hay

A tiger would have:

large size
does not love hay

A rabbit would have:

small size
loves hay

Now think about cows and calves.

A cow is large and loves hay.

A calf is smaller but also loves hay.

In the embedding space they would appear close together.

These are vectors.

In reality, embeddings are not just two-dimensional.

They may contain hundreds or thousands of dimensions.

For example, we could also include features like:

mammal
domesticated
lives in water
dangerous
furry

and many more.

To find similar words we compare vectors using cosine similarity.

Cosine similarity measures the angle between vectors.

Vectors pointing in similar directions are semantically similar.

An interesting property is that we can also perform arithmetic with embeddings.

We can add and subtract vectors to discover relationships.

That is very cool.

In 2017 we got the famous paper:

“Attention Is All You Need”

This introduced the Transformer architecture.

Modern language models are based on Transformers.

The goal is simple:

Predict the next word based on the previous sequence.

For example:

“How are you?”

The model predicts the next word using context.

Attention is important because words can have different meanings depending on context.

For example:

“I am cool.”

Here “cool” refers to the person.

But:

“The ice cream is cool.”

Now “cool” refers to temperature.

The same word has different meanings depending on context.

Attention mechanisms allow the model to determine which surrounding words matter most.

Before Transformers, people commonly used RNNs — recurrent neural networks.

Transformers improved this significantly.

The model computes similarities between words to determine context.

For example:

“I” strongly influences the meaning of “cool” in the first sentence.
“ice cream” strongly influences “cool” in the second sentence.

The model learns these relationships through training on massive amounts of data.

Using Transformers, the model generates text one token at a time using previous tokens as context.

For simplicity, we can think of tokens as words, even though tokens are actually smaller pieces of text.

For example:

Input:

“I am”

The model predicts:

“cool”

Then the sequence becomes:

“I am cool”

Then it predicts the next token again.

This process repeats continuously.

Next we arrive at GPT:

Generative Pre-trained Transformer.

The model is pre-trained using unsupervised learning on enormous amounts of internet text.

By training on huge datasets, the model develops emergent capabilities.

It starts recognizing patterns and behaviors that researchers did not explicitly program.

We can also introduce something called temperature.

Temperature controls creativity.

Low temperature:

more predictable
safer outputs

High temperature:

more random
more creative

For example, instead of predicting:

“I am cool”

it might predict:

“I am awesome”

because temperature allows less probable words to sometimes be selected.

Higher temperature makes outputs more varied and wild.

Next comes supervised fine-tuning.

We train the model to answer in desired formats.

Then we use something called:

RLHF — Reinforcement Learning from Human Feedback.

Humans evaluate model answers and score them.

The model learns which responses humans prefer.

For example:

If someone asks how to make a bomb, harmful answers receive low scores.

The model learns to avoid generating responses humans dislike.

The system continuously tries to maximize human approval scores.

After RLHF, we eventually arrive at systems like ChatGPT.

This is a simplified overview.

Many details and variations were skipped.

But this gives the basic intuition.

Finally, we move toward Large Multimodal Models.

LLMs are language models, but modern systems can also process:

images
audio
video

Traditional LLMs are not especially good at things like precise mathematics.

So instead they use tools.

For example:

calculators
web search
image generators
speech systems

The model can call external tools to improve performance.

For example:

use Google Search for updated information
use a calculator for exact computations
use image recognition to understand pictures
use image generation models to create images

Modern multimodal systems can also:

understand speech
generate speech
analyze video
describe images

The interactions become increasingly natural.

In this video we went through large language models and gained intuition about how they work.

We discussed:

representing text numerically
embeddings
semantic similarity
Transformers
attention
GPT
pre-training
supervised learning
reinforcement learning with human feedback
multimodal models

We skipped most of the heavy mathematics to keep the explanation intuitive and simple.

I hope you learned a lot in this video.

See you in the next one.

Bye.