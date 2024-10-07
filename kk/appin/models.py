from django.db import models

# Create your models here.

class Datas(models.Model):
    Name=models.CharField(max_length=20,default="")
    Number=models.IntegerField(default="")
    Address=models.CharField(max_length=50,default="")
    Mail=models.CharField(max_length=50,default="")
