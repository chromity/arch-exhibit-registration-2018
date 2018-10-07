from django.urls import path
from . import views

app_name = "registration"
urlpatterns = [
    path('', views.registration_new, name="index"),
    path('new', views.registration_new, name="registration_new"),
    path('<int:pk>/', views.registration_detail, name="registration_detail"),
    path('<int:pk>/edit/', views.registration_edit, name="registration_edit"),
    path('history', views.registration_history, name="registration_history"),
    path('success', views.registration_success, name="registration_success")
]
