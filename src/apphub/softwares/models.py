from django.db import models



# Create your models here.


class Software(models.Model):
    software_id = models.AutoField(primary_key=True)
    picture_path = models.CharField(max_length=500, blank=True)
    name = models.CharField(max_length=100)
    # description = models.CharField(max_length=100)
    description = models.TextField()
    size = models.FloatField()


class Platform(models.Model):
    platform_id = models.AutoField(primary_key=True)
    picture_path = models.CharField(max_length=500, blank=True)
    name = models.CharField(max_length=100)


class SoftwarePlatform(models.Model):
    relation_id = models.AutoField(primary_key=True)
    software_id = models.ForeignKey(Software, on_delete=models.CASCADE)
    platform_id = models.ForeignKey(Platform, on_delete=models.CASCADE)
    