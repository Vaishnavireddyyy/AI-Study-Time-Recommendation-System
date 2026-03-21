import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import joblib

# Load dataset
df = pd.read_csv("student_data.csv")

# Features & target
X = df.drop("recommended_study_time", axis=1)
y = df["recommended_study_time"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Build Deep Neural Network
model = Sequential()

model.add(Dense(64, activation="relu", input_shape=(X_train.shape[1],)))
model.add(Dense(32, activation="relu"))
model.add(Dense(1))

model.compile(optimizer="adam", loss="mse", metrics=["mae"])

# Train model
model.fit(X_train, y_train, epochs=50, batch_size=32, verbose=1)

# Save model & scaler
model.save("study_model.h5")
joblib.dump(scaler, "scaler.pkl")

print("Model trained and saved successfully!")
