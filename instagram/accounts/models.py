from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.BigIntegerField()
    profilepic=models.ImageField(upload_to='profile')
    bio=models.CharField()
    dateOfBirth = models.DateField(auto_now=False, auto_now_add=False)
    
class following(models.Model):
    u_id=models.ForeignKey(User,on_delete=models.CASCADE)
    f_id=models.BigIntegerField()
class follower(models.Model):
    u_id=models.ForeignKey(User,on_delete=models.CASCADE)
    f_id=models.BigIntegerField()



