from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class ProfilePicture(models.Model):
	photo = models.ImageField(upload_to='profile_pictures')
	user = models.OneToOneField(User, on_delete=models.CASCADE)
