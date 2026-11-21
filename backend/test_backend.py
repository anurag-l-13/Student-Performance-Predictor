from predictor import predict_marks

result = predict_marks(
    study=5,
    attendance=85,
    previous=75,
    sleep=7
)

print("Predicted Marks:", result)