import pandas as pd
import numpy as np

np.random.seed(42)

data = {
    "study_hours": np.random.uniform(1, 10, 500),
    "attendance": np.random.uniform(40, 100, 500),
    "previous_marks": np.random.uniform(30, 100, 500),
    "sleep_hours": np.random.uniform(4, 10, 500)
}

df = pd.DataFrame(data)

df["final_marks"] = (
    df["study_hours"] * 3 +
    df["attendance"] * 0.2 +
    df["previous_marks"] * 0.4 +
    df["sleep_hours"] * 1.5 +
    np.random.normal(0, 5, 500)
)

df["final_marks"] = df["final_marks"].clip(0, 100)

df.to_csv("data/students.csv", index=False)

print("Dataset generated successfully!")
print(df.head())