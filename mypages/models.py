from django.db import models

class Usuarios(models.Model):
    correo = models.EmailField(max_length=100)
