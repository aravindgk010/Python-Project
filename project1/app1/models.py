from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name

class Team(models.Model):
    mem_name = models.CharField(max_length=250)
    dp = models.ImageField(upload_to='pics')
    about = models.TextField()

    def __str__(self):
        return self.mem_name
