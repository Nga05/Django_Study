from operator import mod
from turtle import title
from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField(default=8)
    content = models.CharField(max_length=255)