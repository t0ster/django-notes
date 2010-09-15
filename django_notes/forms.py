from django import forms
from django.forms.models import modelformset_factory
import tinymce.widgets

from models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        exclude = ('user',)
        widgets = {
            'content': tinymce.widgets.TinyMCE(attrs={'cols': 80, 'rows': 30})
        }
        
class ActionForm(forms.Form):
    action = forms.CharField(initial="delete", widget=forms.HiddenInput())

NoteFormSetBase = modelformset_factory(
    Note,
    extra=0,
    fields=('title',)
)

class NoteFormSet(NoteFormSetBase):
    def add_fields(self, form, index):
        super(NoteFormSet, self).add_fields(form, index)
        form.fields['title'].required = False
        form.fields['is_checked'] = forms.BooleanField(required=False)
