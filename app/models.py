from django.db import models

# Create your models here.
class Book(models.Model):       
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.IntegerField()    

    def __str__(self):
        return self.name 
    

class Mobile(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    year = models.IntegerField()    

    def __str__(self):
        return self.name