from django.db import models

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)
    birth_date = models.DateField()
    
    def __str__(self):
        return self.name
