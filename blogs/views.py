from .models import *
from django.shortcuts import render_to_response, render, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from .forms import CommentForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import datetime


# python tutorials:
def my_blog_index(request):
    posts = Post.objects.all()
    posts_list = Post.objects.all()

    paginator = Paginator(posts_list, 5)
    page = request.GET.get('page')

    try:
        posts_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts_list = paginator.page(paginator.num_pages)

    comments = Comment.objects.all()
    tags = Tag.objects.all()
    context = request
    return render_to_response('./blogs/my_blog_index.html',
                              {
                                'posts': posts,
                                'comments': comments,
                                'tags': tags,
                                'posts_list': posts_list,
                              },
                              context)

@csrf_protect
def my_blog_post(request, id):
    post = get_object_or_404(Post, id=id)
    posts = Post.objects.all()
    comments = Comment.objects.all()
    tags = Tag.objects.all()
    
    comment_num = Comment.objects.filter(post=post).count()
    post.comment_num = comment_num
    post.save()
    

    comment_form =  CommentForm()
    
    if request.method == "POST":
      print(request.POST.get("name"))
      print(request.POST.get("email"))
      print(request.POST.get("content"))

      name = request.POST.get("name")
      email = request.POST.get("email")
      content = request.POST.get("content")

      new_comment = Comment.objects.create()
      
      new_comment.name = name
      new_comment.email = email
      new_comment.content = content
      new_comment.post = post
      new_comment.publish_time = datetime.datetime.now()

      now = datetime.datetime.now()
      print('---------------------')
      print(datetime.datetime.now().date())
      #print( datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
      print(datetime.datetime.now().strftime("%H:%M:%S"))
      print('---------------------')
      new_comment.save()

    c = {
        'post': post,
        'posts': posts,      
        'comments': comments,  
        'comment_form': comment_form,   
        'comment_num': comment_num,  
        'tags': tags,          
      }

    return render(request, './blogs/my_blog_post.html', c)

