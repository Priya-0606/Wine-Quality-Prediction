from django import forms

class WineInputForm(forms.Form):
    fixed_acidity = forms.FloatField(
        min_value=4.0, max_value=16.0,
        widget=forms.NumberInput(attrs={"class": "form-control", "step": "0.1"})
    )
    volatile_acidity = forms.FloatField(
        min_value=0.1, max_value=1.5,
        widget=forms.NumberInput(attrs={"class": "form-control", "step": "0.01"})
    )
    citric_acid = forms.FloatField(
        min_value=0.0, max_value=1.0,
        widget=forms.NumberInput(attrs={"class": "form-control", "step": "0.01"})
    )
    residual_sugar = forms.FloatField(
        min_value=0.5, max_value=15.0,
        widget=forms.NumberInput(attrs={"class": "form-control", "step": "0.1"})
    )
    chlorides = forms.FloatField(
        min_value=0.01, max_value=0.5,
        widget=forms.NumberInput(attrs={"class": "form-control", "step": "0.01"})
    )
    free_sulfur_dioxide = forms.FloatField(
        min_value=1, max_value=80,
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    density = forms.FloatField(
        min_value=0.990, max_value=1.005,
        widget=forms.NumberInput(attrs={"class": "form-control", "step": "0.001"})
    )
    pH = forms.FloatField(
        min_value=2.8, max_value=4.0,
        widget=forms.NumberInput(attrs={"class": "form-control", "step": "0.01"})
    )
    sulphates = forms.FloatField(
        min_value=0.3, max_value=2.0,
        widget=forms.NumberInput(attrs={"class": "form-control", "step": "0.01"})
    )
    alcohol = forms.FloatField(
        min_value=8.0, max_value=15.0,
        widget=forms.NumberInput(attrs={"class": "form-control", "step": "0.1"})
    )




    
