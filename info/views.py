from django.shortcuts import render

#from .forms import Contact_Form

from django.core.mail import send_mail

# Create your views here.


def Home(request):

    context = {

    }

    return render(request,'info/result.html',context)


def add(request):


    val1 = int(request.POST.get('num1','lol' ))
    val2 = int(request.POST.get('num2','lol'))

    result = val1 + val2

    context = {

        'result' : result
    }

    return render(request,'info/test.html',context)

  
