from django.urls import path
from .views import predict_wine_quality

urlpatterns = [
    path("", predict_wine_quality, name="predict"),
]
