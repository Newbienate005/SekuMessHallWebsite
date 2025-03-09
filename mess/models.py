from django.db import models

# Create your models here.

class User(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Worker', 'Worker'),
        ('Student', 'Student'),
    ]
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username
