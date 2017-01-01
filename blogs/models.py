from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='post_pics')
    image_1170 = models.ImageField(null=True, blank=True, upload_to='post_pics')
    tags = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    publish_time = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    comment_num = models.CharField(max_length=5, null=True, blank=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publish_time']

class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=120, null=True, blank=True)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    publish_time = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name




class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True)
    posts = models.ManyToManyField(Post)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
