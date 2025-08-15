# train_model.py

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Step 1: Load the dataset
df = pd.read_csv("heart.csv")  # Make sure heart.csv is in the same folder

# Step 2: Split data
X = df.drop("target", axis=1)
y = df["target"]

# Step 3: Train the model
model = RandomForestClassifier()
model.fit(X, y)

# Step 4: Save the trained model
joblib.dump(model, "heart_model.pkl")
print("✅ Model trained and saved as heart_model.pkl")
