from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):

    image= models.ImageField(upload_to='avatars',default = 'avatars/anonymous.png', null=True, blank=True)
    user= models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    # if user is deleted, delete the profile
    # related_name creates the link to the user
    
    def __str__(self):
        return '{0}'.format(self.user.username)
        
        # sets profile value to username 