# libraries
import random
import numpy as np
import pickle
import json
from flask import Flask, render_template, request
from flask_ngrok import run_with_ngrok
import nltk
from keras.models import load_model
from nltk.stem import WordNetLemmatizer
import joblib
import pandas as pd
import recommender as rec

nltk.download('omw-1.4')


lemmatizer = WordNetLemmatizer()

disease_detector = joblib.load(r"D:\VIT\Hackathons\SVNIT - DotSlash 6.0\Chatbot\WebApp\disease.pkl")
df_test = pd.read_csv(r"D:\VIT\Hackathons\SVNIT - DotSlash 6.0\archive1\Testing.csv")
df_train = pd.read_csv(r"D:\VIT\Hackathons\SVNIT - DotSlash 6.0\archive1\Training.csv")
X_test = df_test.drop("prognosis",axis=1)
test = []
for i in range(134):
    test.append(0)
x1 = X_test.columns
y1 = test
d1 = pd.DataFrame(y1,x1)
d1 = d1.T
int_choice = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
p1 = df_train["prognosis"].unique()
temp = []
for i in range(len(p1)):
    temp.append(random.choice(int_choice))
temp
refer = {"Disease":p1,"int":temp}
refer = pd.DataFrame(refer)

# chat initialization
chatbot_model = load_model("chatbot_model.h5")
intents = json.loads(open(r"D:\VIT\Hackathons\SVNIT - DotSlash 6.0\Chatbot\WebApp\intents.json").read())
words = pickle.load(open("words.pkl", "rb"))
classes = pickle.load(open("classes.pkl", "rb"))
count = 0

app = Flask(__name__)
run_with_ngrok(app) 

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get", methods=["POST"])
def chatbot_response():
    msg = request.form["msg"]
    if msg.startswith('my name is'):
        name = msg[11:]
        ints = predict_class(msg, chatbot_model)
        res1 = getResponse(ints, intents)
        res = res1.replace("{n}",name)
    elif msg.startswith('symptoms - '):
        sym = msg[10:]
        sym.split(", ")
        for i in range(len(d1.columns)):
            if d1.columns[i] in sym:
                d1.iloc[0][d1.columns[i]] += 1
        pred = disease_detector.predict(d1)
        pred = str(pred[0])
        out = ""
        for i in range(len(refer)):
            if refer["Disease"][i] == pred:
                out = refer["int"][i]
        sug = rec.recommend(out, "piplod")
        temp = str(sug['name'].iloc[1])
        res = "Your suggested doctor is " + temp
            
    else:
        ints = predict_class(msg, chatbot_model)
        res = getResponse(ints, intents)
    return res


# chat functionalities
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words


# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print("found in bag: %s" % w)
    return np.array(bag)


def predict_class(sentence, chatbot_model):
    # filter out predictions below a threshold
    p = bow(sentence, words, show_details=False)
    res = chatbot_model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list


def getResponse(ints, intents_json):
    tag = ints[0]["intent"]
    list_of_intents = intents_json["intents"]
    for i in list_of_intents:
        if i["tag"] == tag:
            result = random.choice(i["responses"])
            break
    return result


def authentication():
    return 0


if __name__=="__main__":
    app.debug=True
    app.run()
    app.run(debug=True)

