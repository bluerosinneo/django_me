# me/urls.py
from django.urls import path
from .views import AboutMeView, InterestsMeView

urlpatterns = [
    path("interests/", InterestsMeView.as_view(), name="interests"),
    path("", AboutMeView.as_view(), name="about"),
]
