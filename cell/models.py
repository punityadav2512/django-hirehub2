from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.
class User(AbstractUser):
    is_cell=models.BooleanField(default=False)
    is_company=models.BooleanField(default=False)


class Posts(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    dated=models.DateTimeField(default=datetime.now,blank=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='cell_user')
    image=models.ImageField(default='./static/cell/images/hire.png',upload_to='cell/posts')

    def __str__(self):
        return self.title + ' by ' + self.author.first_name

class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='cell_profile')
    bio=models.TextField()
    image=models.ImageField(default='./static/cell/images/hire.png',upload_to='cell/profile')
    location=models.CharField(max_length=200,default='')
    url=models.URLField(default='')
    dated=models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.user.first_name + ' Profile' 