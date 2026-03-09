from django.urls import path
from . import views

urlpatterns = [
    path('', views.home.as_view()),
    path('authorized/', views.AuthorizedView.as_view()),
]