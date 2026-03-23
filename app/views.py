from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime as d
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView

"""
! FBV !
todo authenticate() проверяет логин/пароль
todo login() создаёт сессию
todo logout() завершает сессию.

# ...existing code...
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

def login_interface_view(request):
    if request.user.is_authenticated:
        return redirect('welcome')  # или нужный route name

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('welcome')  # или request.GET.get('next')
        return render(request, 'home/login.html', {'error': 'Invalid username or password'})

    return render(request, 'home/login.html')


def logout_interface_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('welcome')
    return render(request, 'home/logout.html')
# ...existing code...
"""


#! CBV 
class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'

class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'

#*  Our function recievs request from user
# def home(request):
#     return HttpResponse("Hello, World!")

#* Class bases view(CBVs): в данный момент мы можем заменить функцию home на class home который возвращает только welcome.html и context.  наш класс home унанледуется от TemplateView
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
