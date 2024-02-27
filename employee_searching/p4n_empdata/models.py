from django.db import models

# Create your models here.

class EmpData(models.Model):
    emp_name = models.CharField(max_lenght=150)
    join_date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=558)

    def __str__(self):
        return self.emp_name