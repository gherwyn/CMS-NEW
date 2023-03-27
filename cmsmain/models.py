from django.db import models
from datetime import datetime
import os, random 
from django.utils import timezone
from django.utils.html import mark_safe
# Create your models here.

now = timezone.now()

def image_path(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    randomstr = ''.join((random.choice(chars)) for x in range(10))
    _now = datetime.now()

    return 'profile_pic/{year}-{month}-{imageid}-{basename}-{randomstring}{ext}'.format(imageid = instance, basename=basefilename, randomstring = randomstr, ext=file_extension, year=_now.strftime('%Y'), month=_now.strftime('%m'), day=_now.strftime('%d'))


class Projects(models.Model):
    user_fname = models.CharField(max_length=200, verbose_name='firstname')
    user_lname = models.CharField(max_length=200, verbose_name='lastname')
    user_email = models.EmailField(unique=True, max_length=200, verbose_name='email')
    user_position = models.CharField(max_length=200, verbose_name='position' )
    user_image = models.ImageField(upload_to=image_path, default='profile_pic/image.jpg')
    
    def image_tag(self):
        return mark_safe('<img src="/cmsmain/media/%s" width="50" height="50"/>'%(self.user_image))


    pub_date = models.DateField(default=now)

    def __str__(self):
        return self.user_email

class Comment(models.Model):
    projects = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField(default='null')
    body = models.TextField(default='null')
    created_on = models.DateTimeField(default=now)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']
    
    def __str__(self):
        return 'Comment {} by  {}'.format(self.body, self.name)






