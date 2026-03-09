from django.urls import path
from .views import detail, NoteListView, NotesDetailView,PopularNotesListView

urlpatterns = [
    path('', NoteListView.as_view(), name='notes-list'),
    # и так наша функция получила <int:pk> как второй параметр и вернула иммено этот note !
    path('<int:pk>/', NotesDetailView.as_view(), name='notes-detail'),
    path('popular/', PopularNotesListView.as_view(), name='popular-notes'),
]