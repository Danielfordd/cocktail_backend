from django.urls import path
from .views import load_tags

urlpatterns = [
    path("/all", load_tags)
]
