from django.db import models

class Bank_Branches(models.Model):
    ifsc = models.TextField("ifsc", max_length=11)
    bank_id = models.BigIntegerField("bank_id")
    branch = models.CharField("branch", max_length=74)
    address = models.TextField("address", max_length=195)
    city = models.CharField("city", max_length=50)
    district = models.CharField("district", max_length=50)
    state = models.CharField("state", max_length=26)
    name = models.CharField("bank_name", max_length=49)
    
