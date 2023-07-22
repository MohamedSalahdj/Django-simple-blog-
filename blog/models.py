from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=1500)
    created_date = models.DateTimeField(default=timezone.now())
    draft = models.BooleanField(default=True)
    author  = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,blank = True,related_name='post_user')
    tags = TaggableManager()
    image = models.ImageField(upload_to="post") 

    def __str__(self):
        return self.title

class Comment(models.Model):
    pass