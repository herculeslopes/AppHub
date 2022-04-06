from django.db import models

# Create your models here.
class Software(models.Model):
    name = models.TextField()
    description = models.TextField()
    size = models.TextField()
    