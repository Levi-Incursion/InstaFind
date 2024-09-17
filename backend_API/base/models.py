from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, null=True, blank=True) 
    #null=true for object, blank=true for django

    def __str__(self):
        return self.name


class Handle(models.Model):
    rank = models.IntegerField()
    username = models.CharField(max_length = 200)
    channel_info = models.CharField(max_length=1000)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,blank=True)

    posts = models.CharField(max_length=1000)
    followers = models.CharField(max_length=1000)
    avg_likes = models.CharField(max_length=1000)

    profile_pic = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.username
