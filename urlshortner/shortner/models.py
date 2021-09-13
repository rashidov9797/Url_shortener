from django.db import models


# Create your models here.


class Url(models.Model):
  link = models.CharField(max_length=5000)
  uuid = models.CharField(max_length=10)
