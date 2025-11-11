from django.urls import path
from . import views

urlpatterns = [
    path('predict/', views.predict_disease, name='predict_disease'),
    path('reports/', views.reports_list, name='reports_list'),
]
