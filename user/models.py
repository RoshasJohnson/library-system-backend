from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser): 
    email = models.EmailField(unique=True,blank=False)

    USERNAME_FIELD = 'email'    # username field is email
    
    REQUIRED_FIELDS = ['username'] 

    def __str__(self):
        return f"{self.email}"

