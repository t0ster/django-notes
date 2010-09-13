from django.views.generic.list_detail import object_list, object_detail
from django.contrib.auth.decorators import login_required
from django.views.generic.create_update import update_object, delete_object
from django.views.generic.simple import direct_to_template, redirect_to
from django.core.urlresolvers import reverse

from forms import NoteForm
from models import Note

@login_required
def list(request):
    qs = Note.objects.filter(user=request.user)
    return object_list(request, qs)

@login_required
def details(request, object_id):
    return object_detail(
        request, Note.objects.filter(user=request.user), object_id
    )

@login_required
def create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        note = form.save(commit=False)
        note.user = request.user
        note.save()
        return redirect_to(request, note.get_absolute_url())
    else:
        form = NoteForm()
    return direct_to_template(request, "django_notes/note_form.html", {"form": form})

@login_required
def delete(request, object_id=None):
    redirect_url = reverse("django_notes.views.list")
    return delete_object(request, Note, redirect_url, object_id)

@login_required
def update(request, object_id=None):
    return update_object(request, form_class=NoteForm, object_id=object_id)
