from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=550)

    def __str__(self):
        return self.title
