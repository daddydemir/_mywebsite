from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    image = models.CharField(max_length=500 , default='https://images.unsplash.com/photo-1511367461989-f85a21fda167?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80')


class Blogs(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    header = models.CharField(max_length=50)
    content = RichTextUploadingField(max_length=20000)
    image = models.TextField(max_length=1000)
    date = models.DateTimeField(default=timezone.now())