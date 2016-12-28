from django.contrib import admin
# Register your models here.
from .models import Post, Tag, Category, Comment

admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)