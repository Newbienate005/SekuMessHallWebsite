from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Worker', 'Worker'),
        ('Student', 'Student'),
    ]
    registration_number = models.CharField(max_length=20, unique=True)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    
    REQUIRED_FIELDS = ['email', 'registration_number', 'role']

    def __str__(self):
        return self.username
    

class MenuItem(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)  # Availability Status

    def __str__(self):
        return self.name

