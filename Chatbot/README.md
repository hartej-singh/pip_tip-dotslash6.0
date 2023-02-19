# Bank Chatbot using keras

#### What is a Chatbot?
A chatbot is an AI-based software designed to interact with humans in their natural languages. These chatbots are usually converse via auditory or textual methods, and they can effortlessly mimic human languages to communicate with human beings in a human-like manner. A chatbot is arguably one of the best applications of natural language processing.

Chatbots can be categorized into two primary variants – **Rule-Based and Self-learning**.

### 1. Rule-Based Conversational Chatbot
The Rule-based approach trains a chatbot to answer questions based on a set of pre-determined rules on which it was initially trained. These set rules can either be very simple or very complex. While rule-based chatbots can handle simple queries quite well, they usually fail to process more complicated queries/requests.

### 2. Self-Learning Chatbots

self-learning bots are chatbots that can learn on their own. These leverage advanced technologies like Artificial Intelligence and Machine Learning to train themselves from instances and behaviours. Naturally, these chatbots are much smarter than rule-based bots. 

Self-learning bots can be further divided into two categories – **Retrieval Based and Generative.**

### 2.1. Retrieval-based Chatbots

A retrieval-based chatbot is one that functions on predefined input patterns and set responses. Once the question/pattern is entered, the chatbot uses a heuristic approach to deliver the appropriate response. The retrieval-based model is extensively used to design goal-oriented chatbots with customized features like the flow and tone of the bot to enhance the customer experience.

Retrieval based bots work on the principle of directed flows or graphs.The bot is trained to rank the best response from a finite set of predefined responses. The responses here are entered manually, or based on a knowledge base of pre-existing information.

Eg. What are your store timings?
Answer: 9 to 5 pm

These systems can be extended to integrate with 3rd Party systems as well.

Eg. Where is my order?
Answer: It’s on its way and should reach you in 10 mins

Retrieval based bots are the most common types of chatbots that you see today. They allow bot developers and UX to control the experience and match it to the expectations of our customers. They work best for goal-oriented bots in customer support, lead generation and feedback. We can decide the tone of the bot, and design the experience, keeping in mind the customer’s brand and reputation.

### 2.2 Generative Chatbots
Unlike retrieval-based chatbots, generative chatbots are not based on predefined responses – they leverage seq2seq neural networks. This is based on the concept of machine translation where the source code is translated from one language to another language. In seq2seq approach, the input is transformed into an output.

### How To Make A Chatbot In Python?

To build a chatbot in Python, we have to import all the necessary packages and initialize the variables to use in your chatbot project. Also, remember that when working with text data, we need to perform data preprocessing on we dataset before designing an ML model.

This is where tokenizing helps with text data – it helps fragment the large text dataset into smaller, readable chunks (like words). Once that is done, we can also go for lemmatization that transforms a word into its lemma form. Then it creates a pickle file to store the python objects that are used for predicting the responses of the bot. 

Another vital part of the chatbot development process is creating the training and testing datasets.

## Output
![1](https://github.com/rjnp2/Bank_Chatbot_using_keras/blob/main/images/1.png)
