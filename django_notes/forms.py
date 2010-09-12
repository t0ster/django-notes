from django import forms
import tinymce.widgets

from models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
#        title = forms.CharField(max_length=128)
        widgets = {
            'content': tinymce.widgets.TinyMCE()
        }
