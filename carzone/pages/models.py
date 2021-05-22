from django.db import models

# Create your models here.
class Team(models.Model):
    first_name= models.CharField(max_length=200)
    last_name= models.CharField(max_length=200)
    designation= models.CharField(max_length=200)
    photo= models.ImageField(upload_to="photos/%y/%m/%d/")
    fblink=models.URLField(max_length=300)
    instalink=models.URLField(max_length=300)
    linkedinlink=models.URLField(max_length=300)
    created_date= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name