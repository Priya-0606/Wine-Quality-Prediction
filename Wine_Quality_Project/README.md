# Wine Quality Prediction Web Application

## Overview
This project is a machine learning-based web application that predicts wine quality based on physicochemical properties. The model is trained using supervised learning techniques and deployed using Django for real-time user interaction.

## Tech Stack
- Python
- Django
- Scikit-learn
- XGBoost
- Pandas, NumPy
- Bootstrap

## Dataset
The dataset contains physicochemical attributes of wine such as acidity, alcohol content, pH, and sulphates, along with quality labels.

## Machine Learning Approach
- Performed data preprocessing and normalization using MinMaxScaler
- Trained and evaluated multiple classification models
- Selected XGBoost as the final model based on validation ROC-AUC performance
- Serialized the trained model and scaler using joblib

## Web Application
- Users input wine parameters via a web form
- Backend validates inputs and applies the same preprocessing used during training
- The trained ML model predicts wine quality in real time

## Project Structure
ml/
└── train_model.py
predictor/
├── views.py
├── forms.py
├── wine_model.pkl
├── scaler.pkl
templates/
└── predict.html


## How to Run
1. Train the model:
   ```bash
   python ml/train_model.py

2. Start the Django server:
python manage.py runserver

3. Open browser and access the prediction page.

Output

The application predicts wine quality and categorizes it as:

Poor

Average

Good