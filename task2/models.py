from django.db import models

class Information(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.EmailField(max_length = 254)
    mobile_number = models.IntegerField()
    location = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    clint_type = models.CharField(max_length=200)
    avg_Revenue = models.IntegerField()