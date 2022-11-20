from tabnanny import verbose
from tkinter import CASCADE
from unicodedata import category
from django.db import models
from django.forms import NullBooleanField
from django.utils import timezone
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation



class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category',args=[self.slug])
    


class Post(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.CharField(max_length=150)
    slug = models.SlugField(max_length=250)
    header_image = models.ImageField(blank=False, null=True, upload_to='images/')
   

    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):
        return reverse('detail_page', args=[self.slug])
    
    
    
    class Meta:
        ordering = ('-date',)



class Video(models.Model):
    subject =  models.CharField(max_length=150)
    url = EmbedVideoField(max_length=140, blank=False, null=True)

    def __str__(self):
        return self.subject
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=255)
    status = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('date',)
    
    def __str__(self):
        return f'Comment By {self.name}'
    
    
class Subscribers(models.Model):
    email = models.EmailField()
    
    def __str__(self):
        
        return self.email
    
    class Meta:
        verbose_name_plural = 'Subsrcibers'


class Newsletter(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField(max_length=255,null=True)
    
    def __str__(self):
        return self.title

  
    