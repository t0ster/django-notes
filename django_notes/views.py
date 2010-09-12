from django.views.generic.list_detail import object_list
from django.contrib.auth.decorators import login_required

from forms import NoteForm

from models import Note
from django.http import HttpResponse
from django.views.generic.simple import direct_to_template

@login_required
def list_notes(request):
    qs = Note.objects.filter(user=request.user)
    return object_list(request, qs)


@login_required
def delete(request, note_id=None):
    pass

@login_required
def edit(request, note_id):
    note = Note.objects.get(id=note_id, user=request.user)
    form = NoteForm(instance=note)
    return direct_to_template(
        request,
        "django_notes/note.html",
        {"form": form,},
                              
    )
