from django.db import models
from datetime import datetime


# Create your models here.
class news(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField()
    date=models.DateTimeField(default=datetime.now())
    category=models.CharField(max_length=100)
    newslink=models.CharField(max_length=100)
    Agency=models.CharField(max_length=100)
    def __str__(self):
        return self.title
