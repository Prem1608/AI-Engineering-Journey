from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "MacBook M2 is ready for AI", "day": 1}

@app.get("/predict/{number}")
def predict(number: int):
    # This simulates a model predicting the square of a number
    result = number * number
    return {"input": number, "prediction": result}