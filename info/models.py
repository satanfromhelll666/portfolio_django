from django.db import models

# Create your models here.

class ContactForm(models.Model):
    first_name = models.CharField(max_length=200,null=True)
    last_name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null= True)
    sub_of_massage = models.CharField(max_length=100,null=True)
    massage = models.CharField(max_length=1000,null=True)


