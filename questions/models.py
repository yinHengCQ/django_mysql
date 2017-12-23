from django.db import models

# Create your models here.
class Question(models.Model):
    title=models.CharField(max_length=100)
    options=models.CharField(max_length=200)
    answer=models.CharField(max_length=2)