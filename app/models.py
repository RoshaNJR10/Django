from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    contact=models.IntegerField()
    roll=models.IntegerField()