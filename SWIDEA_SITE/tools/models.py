from django.db import models

# Create your models here.
class Tool(models.Model):
    name = models.CharField(max_length=50)
    kindof = models.CharField(max_length=50)
    descrip = models.CharField(max_length=50)