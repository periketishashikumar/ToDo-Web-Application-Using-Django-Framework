from django.db import models

# Create your models here.
class List(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)

class History(models.Model):
    new_title = models.CharField(max_length=200)
    new_description = models.CharField(max_length=1000)

