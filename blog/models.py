from django.db import models

# Create your models here.
import datetime
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="static/blog/images")
    fecha = models.DateField(default=datetime.date.today)

    def __str__(self) -> str:
        return f"{self.titulo}, {self.descripcion}, {self.imagen}, {self.fecha}"
    
