from django.db import models

# Create your models here.
class Employee (models.Model):
    username = models.CharField(max_length=100)
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    email = models.CharField(max_length=100, blank=True)
    birthDate = models.CharField(max_length=10)
    basicSalary = models.CharField(max_length=8)
    status = models.CharField(max_length=10)
    group = models.CharField(max_length=10)
    description = models.CharField(max_length=10)

    def __str__(self):
        return self.username