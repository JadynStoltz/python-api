from django.db import models

# Create your models here.
class User(models.Model):
    age = models.IntegerField()
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name
    
# Employee model to store employee details
class Employee(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    position = models.CharField(max_length=50)
    joinDate = models.DateField()
    
    
    def __str__(self):
        return self.name
    
