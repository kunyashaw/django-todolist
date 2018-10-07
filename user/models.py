from django.db import models

# Create your models here.

class User(models.Model):
    uname = models.CharField(max_length=200)
    upwd = models.CharField(max_length=200)
    