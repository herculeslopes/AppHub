from django.db import models

# Create your models here.
class Software(models.Model):
    software_id = models.AutoField(primary_key=True)
    picture_path = models.CharField(max_length=500, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    size = models.FloatField()
    