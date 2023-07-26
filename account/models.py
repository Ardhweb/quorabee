from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=25, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='users/%Y/%m/%d/',blank=True)
    email = models.EmailField(max_length=50,null=True, blank=True)
    
    
    
   
    
    def __str__(self):
        return f'Profile for user {self.user.username}'