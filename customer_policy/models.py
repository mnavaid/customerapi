from django.db import models
from customer.models import Customer

# Create your models here.
class Policy(models.Model):
    age = models.IntegerField()
    ptype = models.CharField(max_length=150)
    premium = models.FloatField()
    cover = models.FloatField()
    
class CustomerPolicy(models.Model):
    customer_id = models.ForeignKey('customer.Customer', on_delete=models.CASCADE, related_name='customer')
    policy_id = models.ForeignKey('Policy', on_delete=models.CASCADE, related_name='policy')
    policy_status = models.CharField(max_length=50)
    updated_on = models.DateTimeField(auto_now_add=True, blank=True)
