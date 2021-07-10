from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    dob = models.CharField(max_length=150)

    def __srt__(self):
        return self.first_name
