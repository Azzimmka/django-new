from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .models import Notes
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from notes.forms import NotesForm
from django.views.decorators.http import require_POST
from django.db.models import F

# Create your views here.

# def create_note(request):
#     if request.method == 'POST':
#         form = NotesForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/smart/notes/')
#     else:
#         form = NotesForm()
#     return render(request, 'notes/notes_form.html', {'form': form})


#todo Create a new Note, will help us CreateView from  django.views.generic
class NotesCreateView(LoginRequiredMixin, CreateView):
    # here we need 3 things
    model = Notes # endpoints understands what is the regarding to
    # Django запрещает одновременно указывать атрибуты fields и form_class.
    # fields = ['title', 'text'] # we allow ther user to fill only this fields which is from out attributes
    success_url = '/smart/' # rerendering после добаления
    form_class = NotesForm
    login_url = '/admin/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())



class NoteListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = 'notes' # это имя переменной которую ты используешь в HTML шаблоне.
    template_name = 'notes/notes.html'
    login_url = '/login/'

    def get_queryset(self):
        return self.request.user.notes.all()

# def notes(request):
#     notes = Notes.objects.all()
#     context = {
#         'notes': notes
#     }

#     return render(request, 'notes/notes.html', context)
# *--------------------------------

class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/'
    form_class = NotesForm


# def checkNotes(req):
#     notess = Notes.objects.all()
#     return HttpResponse(notess)


"""Все параметры после request должны совпадать с тем, что описано в path(...). второй параметр отвечает за primary key то есть первичный ключ    и мы получим этот pk из urls.py и сделаем get запрос что бы представить именно этот note по его первичному ключу!"""
#? Проблема пользователь может вести не существующий pk в наш путь и тогда наше приложения вернет ошикбу DoesNotExist то есть 404 ошибку для того что бы пользователь не увидел это ошибку так как он не будет понимать что эта за ошибку, в том случае мы должны "Обрабоать это исключения" в нашей функции! с помощью конструкции try: except: . если pk найдется успешно то сработает try с в противном случае except и вернет ошибку Http404 from django.http или же ты можешь создать свою кастомную ошибку 404!
# def detail(request, pk):
#     try: 
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404('Note does not exist try another')
#     context = {'note': note}
#     return render(request, 'notes/notes_detail.html', context=context)

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
    
# def popular_notes(request):
#     popular_notes_qs = Notes.objects.filter(likes__gte=1)
#     context = {
#         'popularNote': popular_notes_qs,  # то же имя, что в шаблоне
#     }
#     return render(request, 'notes/popular_notes.html', context)
    

class NotesDeleteView(DeleteView):
    model = Notes
    template_name = 'notes/notes_delete.html'
    success_url = '/smart/'

@require_POST
def like_note(request, pk):
    Notes.objects.filter(pk=pk).update(likes=F('likes') + 1)
    return redirect(request.POST.get('next', 'notes-list')) 


def add_like_view(request, pk):
    if request.method == 'POST':
        note = get_object_or_404(Notes, pk=pk)
        note.likes += 1
        note.save()
        return HttpResponseRedirect(reverse('notes-detail', args=(pk,)))
    return Http404

def change_visibility_view(request, pk):
    if request.method == 'POST':
        note = get_object_or_404(Notes, pk=pk)
        note.is_public = not note.is_public
        note.save()
        return HttpResponseRedirect(reverse('notes-detail', args=(pk,)))
    return Http404



def make_public_view(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    note.is_public = True
    note.save(update_fields=['is_public'])
    return redirect('notes-detail', pk=pk)