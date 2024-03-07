from django.db import models

# Create your models here.
class Review(models.Model):
    username = models.CharField(max_length=63)
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)

