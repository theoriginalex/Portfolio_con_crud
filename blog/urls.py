from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("", views.post_normal, name='posts'),
    path("<int:post_id>", views.detalle_post, name='detalle_post'),
    path('crear-post/', views.post_create, name='crear_post'),
]





