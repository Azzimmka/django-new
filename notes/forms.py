from django import forms
from .models import Notes
from django.core.exceptions import ValidationError

class NotesForm(forms.ModelForm):
    is_public = forms.TypedChoiceField(
        label='Visibility',
        choices=((0, 'Private'), (1, 'Public')),
        coerce=lambda x: x == '1',
        widget=forms.RadioSelect(attrs={'class': 'mr-2'}),
        initial=0,
    )

    class Meta:
        model = Notes
        fields = ['title', 'text', 'likes', 'is_public']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full rounded-lg border border-1 border-gray-200 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-yellow-400',
                'placeholder': 'Enter title',
            }),
            'text': forms.Textarea(attrs={
                'class': 'w-full rounded-lg border border-gray-300 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-400',
                'rows': 5,
                'placeholder': 'Enter note text',
            }),
            'likes': forms.NumberInput(attrs={
                'class': 'w-full rounded-lg border border-gray-300 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-400',
                'min': 0,
            }),
        }

# Этот метод clean_title() нужен для валидации поля title в форме перед сохранением.
    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' not in title:
            raise ValidationError("Title must contain 'Django'")
        return title
