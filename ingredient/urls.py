from django.urls import path
from .views import all_ingredients

urlpatterns = [
    path('all', all_ingredients)
]
