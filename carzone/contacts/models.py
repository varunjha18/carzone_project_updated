from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    car_id=models.IntegerField()
    customer_needs=models.CharField(max_length=200)
    car_title=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    phone=models.CharField(max_length=200)
    message=models.TextField(max_length=200,blank=True)
    user_id=models.IntegerField()
    created_date=models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.email