from django.db import models

# Create your models here.

class User(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Worker', 'Worker'),
        ('Student/Staff', 'Student/Staff'),
    ]
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username
class Menu(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Announcement(models.Model):
     message = models.TextField()
     timestamp = models.DateTimeField(auto_now_add=True)

     def __str__(self):
        return self.message[:50]  # Returns the first 50 characters for readability
    

class Order(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    items = models.JSONField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - User {self.user.id}"
    

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report {self.id} - User {self.user.id}"
    
