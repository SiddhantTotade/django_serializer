from django.db import models

# Create your models here.
class Plan(models.Model):
    monthly_rental = models.IntegerField()
    data_with_rollover = models.IntegerField()
    sms_per_day = models.IntegerField()
    local_std_roaming = models.CharField(max_length=15)
    amazon_prime = models.CharField(max_length=10)