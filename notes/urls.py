from django.urls import path
from .views import NoteListView, NotesDetailView, PopularNotesListView, NotesCreateView, NotesUpdateView, NotesDeleteView, add_like_view, make_public_view, change_visibility_view

urlpatterns = [
    path('', NoteListView.as_view(), name='notes-list'),
    # и так наша функция получила <int:pk> как второй параметр и вернула иммено этот note !
    path('<int:pk>/', NotesDetailView.as_view(), name='notes-detail'),
    path('<int:pk>/edit', NotesUpdateView.as_view(), name='notes-update'),
    path('<int:pk>/delete', NotesDeleteView.as_view(), name='notes-delete'),
    #! Typically, get requests should never modify your system
    path('<int:pk>/add_like', add_like_view, name='notes-like'),
    # path('<int:pk>/make_public/', make_public_view, name='notes-make-public'),
    path('<int:pk>/change_visibility/', change_visibility_view, name='notes-change-visibility'),
    path('popular/', PopularNotesListView.as_view(), name='popular-notes'),
    path('new', NotesCreateView.as_view(), name='notes.new'),
]