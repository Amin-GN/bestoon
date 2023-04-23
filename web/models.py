from django.db import models
#from django.contrib.auth.models import User #shouldn't use User directly
from django.conf import settings

# Create your models here.
class Expense(models.Model):
    text=models.CharField(max_length=255)
    date=models.DateTimeField()
    amount=models.BigIntegerField()
    user= models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    def __Unicode__(self):
        return '{}-{}-{}'.format(self.user,self.date,self.text,self.amount)


class Income(models.Model):
    text=models.CharField(max_length=255)
    date=models.DateTimeField()
    amount=models.BigIntegerField()
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    def __Unicode__(self):
        return '{}-{}-{}'.format(self.user,self.date,self.text,self.amount)