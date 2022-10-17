import random
# import time
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('omw-1.4')

from tensorflow.keras.models import load_model

intents_json = "Realtime-Speech-Chatbot/training_data/intents.json"
words_pkl = "Realtime-Speech-Chatbot/training_data/words.pkl"
classes_pkl = "Realtime-Speech-Chatbot/training_data/classes.pkl"
model_h5 = "Realtime-Speech-Chatbot/training_data/chatbot_model.h5"

print("Initializing bot...")

lemmatizer = WordNetLemmatizer()
intents = json.loads(open(intents_json).read())

words = pickle.load(open(words_pkl, "rb"))
classes = pickle.load(open(classes_pkl, "rb"))

model = load_model(model_h5)


def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words


def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)


def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list


def get_response(intents_list, intents_json):
    tag = intents_list[0]["intent"]
    list_of_intents = intents_json["intents"]
    for i in list_of_intents:
        if i["tag"] == tag:
            result = random.choice(i["responses"])
            return result


def chatbot_response(message):
    ints = predict_class(message)
    res = get_response(ints, intents)
    print(res)
    return res


def chatbot_debug():
    while True:
        message = input("\nEnter your message: ")
        ints = predict_class(message)
        try:
            res = get_response(ints, intents)
            print(res)
        except TypeError:
            print("Could not parse audio...")

