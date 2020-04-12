from django.db import models

class Detail(models.Model):
    Uid = models.IntegerField(default=None)
    Title = models.CharField(max_length=100)
    Url = models.TextField()
    Author = models.CharField(max_length=100)
    Genre = models.CharField(max_length=100)
