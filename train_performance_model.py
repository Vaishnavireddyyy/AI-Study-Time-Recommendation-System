import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.preprocessing import StandardScaler
import joblib

# Generate synthetic dataset
np.random.seed(42)

n = 1000

data = {
    "previous_marks": np.random.randint(40, 100, n),
    "study_hours": np.random.uniform(1, 6, n),
    "attendance": np.random.randint(50, 100, n),
    "consistency": np.random.uniform(0, 3, n)
}

df = pd.DataFrame(data)

# target
df["predicted_marks"] = (
    df["previous_marks"] * 0.5 +
    df["study_hours"] * 8 +
    df["attendance"] * 0.2 -
    df["consistency"] * 3
)

X = df.drop("predicted_marks", axis=1)
y = df["predicted_marks"]

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

model = Sequential()

model.add(Dense(64,activation="relu",input_shape=(X.shape[1],)))
model.add(Dense(32,activation="relu"))
model.add(Dense(1))

model.compile(
    optimizer="adam",
    loss="mse",
    metrics=["mae"]
)

model.fit(X_train,y_train,epochs=40,batch_size=32)

model.save("performance_model.h5")
joblib.dump(scaler,"performance_scaler.pkl")

print("Performance model trained")