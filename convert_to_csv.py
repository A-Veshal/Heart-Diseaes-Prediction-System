import pandas as pd

# Define column names
columns = [
    "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
    "thalach", "exang", "oldpeak", "slope", "ca", "thal", "target"
]

# Read data
df = pd.read_csv("processed.cleveland.data", header=None, names=columns)

# Replace missing values
df.replace("?", pd.NA, inplace=True)

# Drop rows with missing values (or handle them as needed)
df.dropna(inplace=True)

# Convert data types
df = df.astype({
    "age": float,
    "sex": int,
    "cp": int,
    "trestbps": float,
    "chol": float,
    "fbs": int,
    "restecg": int,
    "thalach": float,
    "exang": int,
    "oldpeak": float,
    "slope": int,
    "ca": float,
    "thal": float,
    "target": int
})

# Convert target to binary: 0 = No disease, 1 = Disease
df["target"] = df["target"].apply(lambda x: 1 if x > 0 else 0)

# Save to CSV
df.to_csv("heart.csv", index=False)
print("✅ Converted to heart.csv successfully!")
