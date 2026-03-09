from django.shortcuts import render
from django.http import HttpResponse
from .models import Notes
# Create your views here.

def notes(request):
    notes = Notes.objects.all()
    context = {
        'notes': notes
    }

    return render(request, 'notes/notes.html', context)

def checkNotes(req):
    notess = Notes.objects.all()
    return HttpResponse(notess)
print(checkNotes)