import pandas as pd
from sklearn.ensemble import IsolationForest
import pickle

data = pd.read_csv("../crime_dataset.csv")

X = data[["crime_rate","hour"]]

model = IsolationForest(contamination=0.05)
model.fit(X)

pickle.dump(model, open("../models/anomaly_model.pkl","wb"))
print("Anomaly model trained")