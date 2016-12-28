from blogs.models import *
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = request
    return render_to_response('./index.html',
                              {
                                'posts': posts,
                              },
                              context)

