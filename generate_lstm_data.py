import numpy as np
import pandas as pd

np.random.seed(42)

data = []

for _ in range(1000):
    week = np.random.randint(1, 8, 7)  # 7 days study hours
    consistency = np.std(week)  # variation = consistency measure
    data.append(list(week) + [consistency])

columns = ["Day1","Day2","Day3","Day4","Day5","Day6","Day7","Consistency"]

df = pd.DataFrame(data, columns=columns)
df.to_csv("lstm_data.csv", index=False)

print("LSTM dataset created!")
