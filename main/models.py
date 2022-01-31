from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=15)
    description = models.TextField()
# Create your models here.
