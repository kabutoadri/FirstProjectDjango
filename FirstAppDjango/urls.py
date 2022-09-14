from django.urls import path
from . import views

# Construction d'une URL
urlpatterns = [
    path('', views.my_view, name='my_view'),
]
