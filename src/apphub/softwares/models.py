from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Platform(models.Model):
    platform_id = models.AutoField(primary_key=True)
    picture_path = models.CharField(max_length=500, blank=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Software(models.Model):
    software_id = models.AutoField(primary_key=True)
    publisher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    picture_path = models.CharField(max_length=500, blank=True)
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=100, blank=True, null=True)
    # description = models.CharField(max_length=100)
    description = models.TextField()
    project_url = models.CharField(max_length=650, blank=True, null=True)
    size = models.FloatField(blank=True, null=True)

    platforms = models.ManyToManyField(Platform, through='SoftwarePlatform')

    def __str__(self):
        return self.name

class SoftwarePlatform(models.Model):
    # relation_id = models.AutoField(primary_key=True)
    software = models.ForeignKey(Software, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = [['software', 'platform']]


class Comment(models.Model):
    software = models.ForeignKey(Software, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.software.name} - {self.user}'
