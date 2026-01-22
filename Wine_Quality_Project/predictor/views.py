from django.shortcuts import render

# Create your views here.

import joblib
import numpy as np
from django.shortcuts import render
from .forms import WineInputForm
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "wine_model.pkl")
SCALER_PATH = os.path.join(os.path.dirname(__file__), "scaler.pkl")

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

"""def quality_label(score):
    if score <= 4:
        return "Poor"
    elif score <= 6:
        return "Average"
    else:
        return "Good""""

    
def quality_label(pred):
    return "Good" if pred == 1 else "Not Good"


def predict_wine_quality(request):
    prediction = None
    label = None

    if request.method == "POST":
        form = WineInputForm(request.POST)
        if form.is_valid():
            data = [
                form.cleaned_data["fixed_acidity"],
                form.cleaned_data["volatile_acidity"],
                form.cleaned_data["citric_acid"],
                form.cleaned_data["residual_sugar"],
                form.cleaned_data["chlorides"],
                form.cleaned_data["free_sulfur_dioxide"],
                form.cleaned_data["density"],
                form.cleaned_data["pH"],
                form.cleaned_data["sulphates"],
                form.cleaned_data["alcohol"],
            ]

            data = np.array(data).reshape((1, 10))
            data = (scaler.transform(data))

            prediction = model.predict(data)[0]
            label = quality_label(prediction)


            print("PREDICTION:", prediction, label) 
    else:
        form = WineInputForm()

    return render(
        request,
        "predict.html",
        {
            "form": form,
            "prediction": prediction,
            "label": label,
        },
    )




