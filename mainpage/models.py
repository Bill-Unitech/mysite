from django.db import models

# Create your models here.

class Statics(models.Model):
    title = models.CharField(max_length=20)
    total_times_of_visiting = models.IntegerField(blank=True, null=True)
    ip_addr = models.TextField()
    def __unicode__(self):
        return self.title
    def __str__(self):
        return  self.title




