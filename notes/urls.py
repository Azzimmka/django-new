from django.urls import path
from .views import notes, detail

urlpatterns = [
    path('', notes),
    # и так наша функция получила <int:pk> как второй параметр и вернула иммено этот note !
    path('notes/<int:pk>/', detail)
]