from datetime import datetime
from distutils.command.upload import upload
from email.policy import default
from django.db import models
from cell.models import User
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    dated=models.DateTimeField(default=datetime.now,blank=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='company_user')
    image=models.ImageField(default='./static/company/images/hire.png',upload_to='company/post')

    def __str__(self):
        return self.title + ' by ' + self.author.first_name

class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='company_profile')
    bio=models.TextField()
    image=models.ImageField(default='./static/company/images/hire.png',upload_to='company/profile')
    location=models.CharField(max_length=200,default='')
    url=models.URLField(default='')
    dated=models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.user.first_name + ' Profile'