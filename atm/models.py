from django.db import models

class RegisterPage(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,unique=True)
    account_number=models.IntegerField()
    balance=models.IntegerField()
    password=models.CharField(max_length=100)


