# =============================
# 1. Imports
# =============================
from fastapi import FastAPI
import joblib
import pandas as pd

# =============================
# 2. Initialize App
# =============================
app = FastAPI(title="Sales Prediction API")

# =============================
# 3. Load Model
# =============================



model = joblib.load("model.pkl")

# =============================
# 4. Home Route
# =============================
@app.post("/predict")
def predict(data: dict):

    try:
        df = pd.DataFrame([data])

        # ✅ Feature Engineering (IMPORTANT FIX)
        df["Price_Visibility"] = df["MRP"] * df["ProductVisibility"]
        df["Price_per_Weight"] = df["MRP"] / df["Weight"]

        prediction = model.predict(df)[0]

        return {"prediction": float(prediction)}

    except Exception as e:
        return {"error": str(e)}