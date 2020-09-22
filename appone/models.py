from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField("emp_name",max_length=30)
    salary = models.FloatField("emp_sal")
    des = models.CharField("emp_des",max_length=30)
    age = models.IntegerField("emp_age")
    active = models.CharField("active",max_length=30,default='Y')
