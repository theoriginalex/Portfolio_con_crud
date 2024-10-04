from django.urls import path
from . import views

app_name = 'portfolio'
urlpatterns = [
    path('crear-proyecto/', views.project_create, name='crear_project'),
]