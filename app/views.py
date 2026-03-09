from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime as d
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

#*  Our function recievs request from user
# def home(request):
#     return HttpResponse("Hello, World!")

#* Class bases view(CBVs): в данный момент мы можем заменить функцию home в class home который возвращает только welcome.html и context.  наш класс home унанледуется от TemplateView
class home(TemplateView):
    template_name = 'home/welcome.html'
    # но нам нужно дать еще один аттрибут что бы передать context data!
    extra_context = {'today': d.today()}

# todo instead of using HttpResponse  we will use render which is already imported from shortcuts
# we need to pass 3 params to render: 1. request, 2 the name of template, 3 context data
# def home(request):
#     context = {
#         'today': datetime.today()
#     }
#     return render(request, 'home/welcome.html', context=context)

def error(req):
    return HttpResponse('error!')



class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name  = 'home/authorized.html'
    login_url = '/admin/'


# @login_required(login_url='/admin/')
# def authorized(request):
#     return render(request,'home/authorized.html', {})


# Create your views here.
