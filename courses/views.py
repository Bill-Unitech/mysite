from .models import *
from django.shortcuts import render_to_response, render, get_object_or_404
from .forms import MessageForm
from django.views.decorators.csrf import csrf_protect
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


# python tutorials:
@csrf_protect
def my_course_index(request):
    a =1
    context = request
    return render_to_response('./courses/course_base.html',
                              {'a': a},
                              context)

@csrf_protect
def my_contact(request):
    theform = MessageForm()
    c = {
        'the_form': theform,

    }
    return render(request, './contact.html', c)

@csrf_protect
def email(request):
    if request.method == "POST":
      print(request.POST.get("name"))
      print(request.POST.get("email"))
      print(request.POST.get("message"))


    if request.method == "POST":
        send_mail(
            "Greetings, here is a message from a client sent by unitech.site",
            "name: "+ request.POST.get("name")+';\n'+
            "mail: " + request.POST.get("email") + ';\n' +
            "message: " + request.POST.get("message") + '.\n' +
            "tech support - Unitech - Bill ",
            settings.EMAIL_HOST_USER,
            ['314046334@qq.com'],
            fail_silently=False,
        )
      
    theform = MessageForm()  
    c = {
        'the_form': theform,

    }
    return render(request, './contact.html', c)