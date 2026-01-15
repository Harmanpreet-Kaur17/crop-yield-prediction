from flask import Flask, render_template, request
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load model & encoder
model = pickle.load(open("model.pkl", "rb"))
item_encoder = pickle.load(open("item_encoder.pkl", "rb"))

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/predict", methods=["POST"])
def predict():
    crop = request.form["crop"].strip()
    year = int(request.form["year"])
    rainfall = float(request.form["rainfall"])
    pesticides = float(request.form["pesticides"])
    temperature = float(request.form["temperature"])

    # INPUT VALIDATION
    error = None

    if not (1960 <= year <= 2025):
        error = "Year must be between 1960 and 2025"

    elif not (0 <= rainfall <= 5000):
        error = "Rainfall must be between 0 and 5000 mm"

    elif not (0 <= pesticides <= 100):
        error = "Pesticides must be between 0 and 100 tonnes"

    elif not (-10 <= temperature <= 50):
        error = "Temperature must be between -10°C and 50°C"

    if error:
        return render_template("index.html", error=error)

    # VALIDATION (THIS IS WHAT YOU WERE ASKING ABOUT)
    if crop not in item_encoder.classes_:
        return render_template(
            "index.html",
            prediction="Error: Crop not found in training data"
        )

    crop_encoded = item_encoder.transform([crop])[0]

    features = np.array([[crop_encoded, year, rainfall, pesticides, temperature]])
    prediction = model.predict(features)[0]

    # Convert hg/ha to tonnes/ha
    prediction_tonnes = prediction / 10000

    return render_template(
        "index.html",
        prediction_hg=round(prediction, 2),
        prediction_tonnes=round(prediction_tonnes, 2)
    )

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 7860))
    app.run(host="0.0.0.0", port=port)