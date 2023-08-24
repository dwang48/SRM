from django.urls import path
from . import views

urlpatterns = [
    path('calculate/', views.calculate_material_cost, name='calculate_material_cost'),
]
