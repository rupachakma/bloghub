from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    user_type = models.CharField(max_length=20)

class Blogpost(models.Model):
    blogger = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="image",blank=True,null=True)

class Profile(models.Model):
    user_profile = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profilepic = models.ImageField(upload_to="image",blank=True,null=True)
    bio = models.TextField(blank=True)
    address = models.TextField()

    def __str__(self):
        return self.user_profile.username
    