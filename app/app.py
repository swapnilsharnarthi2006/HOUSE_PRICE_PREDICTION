from flask import Flask, render_template, request
import pandas as pd
import joblib
import os

app = Flask(__name__)

# Project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Model paths
MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "random_forest_model.pkl"
)

SCALER_PATH = os.path.join(
    BASE_DIR,
    "models",
    "Scaler.pkl"
)

# Load model and scaler
model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None

    if request.method == "POST":

        # Get values from form
        MedInc = float(request.form["MedInc"])
        HouseAge = float(request.form["HouseAge"])
        AveRooms = float(request.form["AveRooms"])
        AveBedrms = float(request.form["AveBedrms"])
        Population = float(request.form["Population"])
        AveOccup = float(request.form["AveOccup"])
        Latitude = float(request.form["Latitude"])
        Longitude = float(request.form["Longitude"])

        # Create DataFrame
        new_house = pd.DataFrame({
            "MedInc": [MedInc],
            "HouseAge": [HouseAge],
            "AveRooms": [AveRooms],
            "AveBedrms": [AveBedrms],
            "Population": [Population],
            "AveOccup": [AveOccup],
            "Latitude": [Latitude],
            "Longitude": [Longitude]
        })

        # Scale input
        new_house_scaled = scaler.transform(new_house)

        # Predict
        prediction_value = model.predict(new_house_scaled)[0]

        # Convert to dollars
        prediction = prediction_value * 100000

    return render_template(
        "index.html",
        prediction=prediction
    )


if __name__ == "__main__":
    app.run(debug=True)