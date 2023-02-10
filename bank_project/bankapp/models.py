from django.db import models
from django.db.models import CASCADE


# Create your models here.
class District(models.Model):
     name = models.CharField(max_length=30)

     def __str__(self):
         return self.name


class Branch(models.Model):
    district = models.ForeignKey(District,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
         return self.name



class application(models.Model):
    name=models.CharField(max_length=250)
    dob=models.DateField(null=True, blank=True)
    age=models.IntegerField()
    gender=models.CharField(max_length=250)
    phone=models.BigIntegerField()
    email=models.TextField(blank=True)
    address=models.TextField(blank=True)
    district=models.ForeignKey(District,on_delete=models.SET_NULL,blank=True,null=True)
    branch=models.ForeignKey(Branch,on_delete=models.SET_NULL,blank=True,null=True)
    accounttype=models.CharField(max_length=250)
    # materials=models.CharField()

    def __str__(self):
        return self.name

