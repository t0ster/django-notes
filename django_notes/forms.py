from django import forms
import tinymce.widgets

from models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        exclude = ('user',)
        widgets = {
            'content': tinymce.widgets.TinyMCE(attrs={'cols': 80, 'rows': 30})
        }
