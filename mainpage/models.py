from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    def __unicode__(self):
        return self.title
    def __str__(self):
        return  self.title




class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True)
    posts = models.ManyToManyField(Post)
    def __unicode__(self):
        return self.name
    def __str__(self):
        return  self.name
