# from django.urls import path
# from . import views

# urlpatterns = [
#     path('predict/', views.predict_disease, name='predict_disease'),
#     path('reports/', views.reports_list, name='reports_list'),
# ]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('select_symptoms/', views.select_symptoms, name='select_symptoms'),
    path('blank/', views.blank, name='blank'),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('dietary_plans/', views.dietary_plans, name='dietary_plans'),
    path('login/', views.login, name='login'),
    path('medicine_recommendation/', views.medicine_recommendation, name='medicine_recommendation'),
    path('mental_health/', views.mental_health, name='mental_health'),
    path('reports/', views.reports_list, name='reports_list'),  # renamed to match your view
    path('signup/', views.signup, name='signup'),
    path('predict/', views.predict_disease, name='predict_disease'),
]
