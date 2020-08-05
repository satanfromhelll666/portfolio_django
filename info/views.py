from django.shortcuts import render

#from .forms import Contact_Form

from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
# Create your views here.


def Home(request):

    context = {

    }

    return render(request,'info/index.html',context)


def add(request):


    val1 = int(request.POST.get('num1','lol' ))
    val2 = int(request.POST.get('num2','lol'))

    result = val1 + val2

    context = {

        'result' : result
    }

    return render(request,'info/test.html',context)

  
def mail(request):
    first_name = request.POST.get('first_name','NONE')
    last_name = request.POST.get('last_name','NONE')
    email = [str(request.POST.get('email','NONE'))]
    message_sub = request.POST.get('message_sub','NONE')
    message = request.POST.get('text_area','NONE')
    send_form = settings.EMAIL_HOST_USER

    send_mail(message_sub,message,send_form,email,fail_silently=False)


    context={

        'fname':first_name,
        'lname':last_name,
        'msg':message,
        'msg_sub':message_sub,
    }

    return render(request,'info/test.html',context)