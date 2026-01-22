# 🍷 Wine Quality Prediction Web App

A machine learning powered Django web application that predicts wine quality based on chemical properties such as acidity, alcohol, sulphates, density, and more.

This project combines data science and full-stack development by training an ML model and deploying it through a user-friendly web interface.

---

## 🚀 Features

- Predicts wine quality as **Good** or **Not Good**
- Uses an XGBoost Machine Learning model
- MinMaxScaler used for data normalization
- Django web interface with validated input ranges
- Clean and responsive UI using Bootstrap

---

## 🧠 Machine Learning

The model is trained using the Wine Quality Dataset with the following features:

- Fixed acidity  
- Volatile acidity  
- Citric acid  
- Residual sugar  
- Chlorides  
- Free sulfur dioxide  
- Density  
- pH  
- Sulphates  
- Alcohol  

Target:
- Wine Quality (Binary: Good / Not Good)

---

## 🛠️ Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- XGBoost
- Django
- Bootstrap
- Joblib

---

## ▶ How to Run

1. Clone the repository  

2. Install dependencies  

3. Run the Django server  

4. Open in browser  

---

## 📊 Model Training

The model was trained using a separate script (`train_model.py`) and saved using Joblib.  
Both the trained model and scaler are loaded inside the Django app for real-time predictions.

---

## 📌 Project Purpose

This project was created to demonstrate:
- Practical Machine Learning
- Model deployment
- Django integration
- Real-world data preprocessing

## 📷 Screenshot


<img width="1854" height="853" alt="Screenshot 2026-01-22 181553" src="https://github.com/user-attachments/assets/264e0d47-927a-4137-a5f8-8a5f4b8c0569" />

<img width="1874" height="855" alt="Screenshot 2026-01-22 181841" src="https://github.com/user-attachments/assets/b4acfbdd-ac54-4e40-b920-fef8a370be91" />

