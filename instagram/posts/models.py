from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Image(models.Model):
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    image = models.ImageField(upload_to="images")
    caption = models.TextField(max_length=2000)
    publishedDate = models.DateField(auto_now=False, auto_now_add=timezone.now())