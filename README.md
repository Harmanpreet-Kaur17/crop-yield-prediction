# Crop Yield Prediction using Machine Learning

This project predicts agricultural crop yield (hg/ha) using a machine learning model based on historical and environmental data.  
The application is deployed as a web app using Flask and Docker.

## Input Features
- Crop type
- Year
- Average rainfall (mm/year)
- Pesticide usage (tonnes)
- Average temperature (°C)

## Machine Learning Model
- Algorithm: Random Forest Regressor
- Type: Regression
- Reason: Handles non-linear relationships and feature interactions effectively

## Model Performance
- Mean Absolute Error (MAE): ~4562 hg/ha
- R² Score: ~0.98

## Tech Stack
- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- Docker

## Deployment
The project is deployed on Hugging Face Spaces.

🔗 **Live App:** https://huggingface.co/spaces/HarmanpreetKaur06/crop-yield-prediction

## Repository Structure
app.py
Dockerfile
requirements.txt
item_encoder.pkl
templates/index.html
README.md

## Note on Model Files
The trained model file (`model.pkl`) is not included in this repository due to GitHub file size limitations.  
The complete working project including the trained model is available in the deployed Hugging Face Space.

## Author
Harmanpreet Kaur
