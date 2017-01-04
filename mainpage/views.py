from blogs.models import *
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from .models import Statics
# Create your views here.
def index(request):
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        visitor_ip_addr = request.META['HTTP_X_FORWARDED_FOR']
    else:
        visitor_ip_addr = request.META['REMOTE_ADDR']
    
    stat = Statics.objects.get(pk=1)

    stat.total_times_of_visiting += 1

    times_of_visiting = stat.total_times_of_visiting

    stat.ip_addr += (visitor_ip_addr + ';')

    stat.save()    
    
    posts = Post.objects.all()
    posts_a = posts[0:3]
    posts_b = posts[3:6]
    posts_c = posts[6:9]
    context = request
    return render_to_response('./index.html',
                              {
                                'posts': posts,
                                'posts_a': posts_a,
                                'posts_b': posts_b,
                                'posts_c': posts_c,
                                'times_of_visiting': times_of_visiting,
                                'visitor_ip_addr': visitor_ip_addr,
                              },
                              context)

