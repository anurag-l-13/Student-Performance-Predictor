import joblib
import pandas as pd

model = joblib.load("model/student_model.pkl")

def predict_marks(study, attendance, previous, sleep):

    data = pd.DataFrame([{
        "study_hours": study,
        "attendance": attendance,
        "previous_marks": previous,
        "sleep_hours": sleep
    }])

    prediction = model.predict(data)

    return round(prediction[0], 2)