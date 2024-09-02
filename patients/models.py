from django.db import models

class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100, unique=True)
    gender=models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth =models.DateField()
    phone_number=models.CharField(max_length=20)
    address=models.CharField(max_length=200)
    allergies = models.TextField(blank=True, null=True)
    address=models.TextField()
    current_medications = models.TextField(blank=True, null=True)
    medical_history=models.TextField(blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"