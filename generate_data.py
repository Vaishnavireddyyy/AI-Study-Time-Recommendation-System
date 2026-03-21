import pandas as pd
import numpy as np

np.random.seed(42)

n = 1000

data = {
    "marks": np.random.randint(40, 100, n),
    "attendance": np.random.randint(50, 100, n),
    "sleep_hours": np.random.uniform(4, 9, n),
    "distraction_level": np.random.randint(1, 10, n),
    "stress_level": np.random.randint(1, 10, n),
    "study_sessions": np.random.randint(1, 6, n),
}

df = pd.DataFrame(data)

# Create realistic target: recommended study time
df["recommended_study_time"] = (
    8
    - (df["sleep_hours"] * 0.3)
    + (df["distraction_level"] * 0.4)
    + (df["stress_level"] * 0.3)
    - (df["marks"] * 0.02)
    - (df["attendance"] * 0.01)
)

df.to_csv("student_data.csv", index=False)

print("Dataset generated successfully!")
