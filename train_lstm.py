import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Load dataset
df = pd.read_csv("lstm_data.csv")

X = df.drop("Consistency", axis=1).values
y = df["Consistency"].values

# Reshape for LSTM: (samples, time_steps, features)
X = X.reshape((X.shape[0], X.shape[1], 1))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build LSTM model
model = Sequential()
model.add(LSTM(64, activation="relu", input_shape=(7,1)))
model.add(Dense(32, activation="relu"))
model.add(Dense(1))

model.compile(optimizer="adam", loss="mse")

# Train
model.fit(X_train, y_train, epochs=30, batch_size=32)

# Save model
model.save("lstm_model.h5")

print("LSTM model trained successfully!")
