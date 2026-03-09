from django.shortcuts import render
from django.http import HttpResponse
from .models import Notes
from django.http import Http404
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class NoteListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = 'notes' # это имя переменной которую ты используешь в HTML шаблоне.
    template_name = 'notes/notes.html'
    login_url = '/admin/'

# def notes(request):
#     notes = Notes.objects.all()
#     context = {
#         'notes': notes
#     }

#     return render(request, 'notes/notes.html', context)
# *--------------------------------



def checkNotes(req):
    notess = Notes.objects.all()
    return HttpResponse(notess)


"""Все параметры после request должны совпадать с тем, что описано в path(...). второй параметр отвечает за primary key то есть первичный ключ    и мы получим этот pk из urls.py и сделаем get запрос что бы представить именно этот note по его первичному ключу!"""
#? Проблема пользователь может вести не существующий pk в наш путь и тогда наше приложения вернет ошикбу DoesNotExist то есть 404 ошибку для того что бы пользователь не увидел это ошибку так как он не будет понимать что эта за ошибку, в том случае мы должны "Обрабоать это исключения" в нашей функции! с помощью конструкции try: except: . если pk найдется успешно то сработает try с в противном случае except и вернет ошибку Http404 from django.http или же ты можешь создать свою кастомную ошибку 404!
def detail(request, pk):
    try: 
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404('Note does not exist try another')
    context = {'note': note}
    return  render(request, 'notes/notes_detail.html', context=context)

# ! функцую detail на класс detail
class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/notes_detail.html'

class PopularNotesListView(ListView):
    model = Notes
    template_name = 'notes/popular_notes.html'
    context_object_name = 'popularNote'
    # статичный, выполняется один раз при старте сервера:
    # queryset = Notes.objects.filter(likes__gte=1)
    
    #  динамичный, выполняется при каждом запросе:
    def get_queryset(self):
        return Notes.objects.filter(likes__gte=1)