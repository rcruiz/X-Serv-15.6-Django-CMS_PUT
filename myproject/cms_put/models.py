from django.db import models

# Create your models here.

class Pages(models.Model):
    Name = models.CharField(max_length=32)
    Page = models.TextField()
