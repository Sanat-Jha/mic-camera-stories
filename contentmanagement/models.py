from django.db import models
from django.urls import reverse

# Create your models here.

#model for youtube video
class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    thumbnail = models.URLField(max_length=200)
    videoId = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('story') + f'?videoid={self.videoId}'

class Channel(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default="")
    subscribers = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    videos = models.IntegerField(default=0)
    whoarewe = models.TextField(default="")
    story = models.TextField(default="")
    founder = models.TextField(default="")
    DMchannelsubs = models.IntegerField(default=30)

    def __str__(self):
        return self.name

class StorySubmission(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    mobile = models.CharField(max_length=200)
    address = models.TextField()
    organization = models.CharField(max_length=200)
    story = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    feedback = models.TextField(default="")
    status = models.CharField(max_length=200, default="Pending")

    def __str__(self):
        return self.firstname + " " + self.lastname