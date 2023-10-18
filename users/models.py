from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Group(models.Model):
    '''Group model'''

    name = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'

class User(AbstractUser):
    '''User model'''

    group = models.ForeignKey(to=Group, on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)


