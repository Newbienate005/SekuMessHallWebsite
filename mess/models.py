from django.db import models

# Define choices for the role field
ROLE_CHOICES = [
    ('worker', 'Worker'),
    ('student', 'Student'),
    ('admin', 'Admin'),
]

class CustomUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Store hashed passwords in production
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    registration_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.username