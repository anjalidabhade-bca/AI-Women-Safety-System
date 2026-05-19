import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

data = pd.read_csv("../distress_dataset.csv")

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data["text"])
y = data["label"]

model = LogisticRegression()
model.fit(X,y)

pickle.dump((model, vectorizer), open("../models/distress_model.pkl","wb"))
print("Distress model trained")