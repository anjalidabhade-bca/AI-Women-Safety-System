import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import pickle
import os

# Load dataset
data = pd.read_csv("../crime_dataset.csv")

# Create proper datetime column
data["date"] = pd.to_datetime(
    data["month"].astype(str) + "-2024",
    format="%m-%Y"
)

# Monthly aggregation
monthly = data.groupby("date")["crime_rate"].sum()
monthly = monthly.asfreq("MS")

# Train ARIMA model
model = ARIMA(monthly, order=(1,1,1))
model_fit = model.fit()

# Forecast next 3 months
forecast = model_fit.forecast(steps=3)

# Create models folder safely
base_path = os.path.dirname(os.path.dirname(__file__))
models_path = os.path.join(base_path, "models")
os.makedirs(models_path, exist_ok=True)

# Save forecast
file_path = os.path.join(models_path, "forecast.pkl")
pickle.dump((monthly, forecast), open(file_path, "wb"))

print("✅ forecast.pkl saved successfully in models folder")