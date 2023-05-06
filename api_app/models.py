from django.db import models



class Student(models.Model):
    name =  models.CharField(max_length=255)
    email =  models.EmailField(unique=True)
    age   = models.PositiveIntegerField()
    course =  models.CharField(max_length=255)
    


