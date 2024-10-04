from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("", views.post_normal, name='posts'),
    path("<int:post_id>", views.detalle_post, name='detalle_post'),
]





