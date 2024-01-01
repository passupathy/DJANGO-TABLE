from django.db import models

# Create your models here.
class form(models.Model):
    NAME=models.CharField(max_length=20,default="")
    AGE=models.CharField(max_length=20,default="")
    MAIL=models.CharField(max_length=20,default="")
    ADDRESS=models.CharField(max_length=20,default="")
