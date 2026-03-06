from django.shortcuts import render

from .models import Notes
# Create your views here.

def notes(request):
    notes = Notes.objects.all()
    context = {
        'notes': notes
    }

    return render(request, 'notes.html', context)