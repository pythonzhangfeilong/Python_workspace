from django.db import models

# Create your models here.
class UserInfo(models.Model):
    user=models.CharField(max_length=20)
    pwd=models.CharField(max_length=20)