from django.urls import path
from . import views

urlpatterns = [
    path('', views.home.as_view(), name='welcome'),
    path('authorized/', views.AuthorizedView.as_view()),
    path('login/', views.LoginInterfaceView.as_view(), name='login'),
    path('logout/', views.LogoutInterfaceView.as_view(), name='logout')
]