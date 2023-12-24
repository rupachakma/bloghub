from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    user_type = models.CharField(max_length=20)

class Blogpost(models.Model):
    blogger = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to="image",blank=True,null=True)

class Blogger_Profile(models.Model):
    user_profile = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profilepic = models.ImageField(upload_to="image",blank=True,null=True)
    bio = models.TextField(blank=True)
    
    def __str__(self):
        return self.user_profile.username
    
class Viewer_Profile(models.Model):
    user_profile = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profilepic = models.ImageField(upload_to="image",blank=True,null=True)
    bio = models.TextField(blank=True)
    
    def __str__(self):
        return self.user_profile.username