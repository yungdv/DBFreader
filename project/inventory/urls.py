from django.urls import path
from . import views

urlpatterns = [
    path('', views.hardware_list, name='hardware_list'),
    path('equipment-types/', views.equipment_type_list, name='equipment_type_list'),
    path('equipment-types/create/', views.equipment_type_create, name='equipment_type_create'),

    path('models/', views.model_list, name='model_list'),
    path('models/create/', views.model_create, name='model_create'),

    path('hardware/', views.hardware_list, name='hardware_list'),
    path('hardware/create/', views.hardware_create, name='hardware_create'),
]
