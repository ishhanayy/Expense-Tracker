from django.db import models

# Create your models here.
class User(models.Model):
    First_name=models.CharField(max_length=50)
    Last_name=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)
    mobile_number=models.CharField(max_length=10)
    class Meta:
        db_table='user'

class Income(models.Model):
    Date=models.CharField(max_length=10)
    Time=models.CharField(max_length=10)
    Source=models.CharField(max_length=10)
    Amount=models.IntegerField(max_length=10)
    Remark=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        db_table='Income'

class Expense(models.Model):
    Date=models.CharField(max_length=10)
    Time=models.CharField(max_length=10)
    Amount=models.IntegerField(max_length=10)
    Expenses=models.CharField(max_length=10)
    Remark=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        db_table='Expense'


