from django.urls import path
from . import views

urlpatterns = [
    path('', views.choose_category, name='home'),
]