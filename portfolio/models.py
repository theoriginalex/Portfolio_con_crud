from django.db import models
from datetime import date

# Create your models here.
class Project(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)
    imagen = models.ImageField(upload_to="static/portfolio/images")
    url = models.URLField(blank=True)
    fecha = models.DateField(default=date.today)

    def __str__(self) -> str:
        return f"{self.titulo}, {self.descripcion}, {self.imagen}, {self.url}, {self.fecha}"

