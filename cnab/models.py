from django.db import models

# Create your models here.
class Cnab(models.Model):
    titulo = models.CharField(max_length=20)
    fields = models.FileField(upload_to="upload/")
    