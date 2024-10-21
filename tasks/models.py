from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



class UserManager(BaseUserManager):
    def create_user(self, phone_number,password):
        if not phone_number:
            raise ValueError('Users must have a phone number')
        if not password:
            raise ValueError('Users must have a password')
        user = self.model(
            phone_number=phone_number,
            password=password
        )
        user.save(using=self._db)
        return user


class Employer(AbstractBaseUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

class Employee(AbstractBaseUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=10)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name='employees')
    created_at = models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()


class Task(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name='employer')
    assigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employee')
    STATUS_CHOICES = [
        ('started', 'Started'),
        ('finished', 'Finished'),
        ('blocked', 'Blocked'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='started')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
