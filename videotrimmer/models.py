from django.db import models

# Create your models here.
class Video(models.Model):
    
    content = models.BinaryField()
