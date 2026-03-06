from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

#  Our function recievs  request
# def home(request):
#     return HttpResponse("Hello, World!")

# todo instead of using HttpResponse  we will use render which is already imported from shortcuts
# we need to pass 3 params to render 1. request, 2 the name of template, 3 context data
def home(request):
    context = {
        'today': datetime.today()
    }
    return render(request, 'home/welcome.html', context=context)

def error(req):
    return HttpResponse('error!')



# Create your views here.
