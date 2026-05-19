import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

data = pd.read_csv("../crime_dataset.csv")

X = data[["crime_rate","hour"]]
y = data["risk_level"]

model = RandomForestClassifier()
model.fit(X,y)

pickle.dump(model, open("../models/risk_model.pkl","wb"))
print("Risk model trained")