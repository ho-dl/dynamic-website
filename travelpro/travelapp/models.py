from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    description=models.TextField()

class Team(models.Model):
    img=models.ImageField(upload_to='team')
    name=models.CharField(max_length=250)
    description=models.TextField()

    def __str__(self):
        return self.name