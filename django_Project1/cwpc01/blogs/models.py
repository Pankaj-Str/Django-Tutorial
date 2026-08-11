from django.db import models

# Create your models here.


class UserProfile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15 , null=True)

    # def __str__(self):
    #     return f'{self.first_name} {self.last_name}'