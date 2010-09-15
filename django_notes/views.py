from django.views.generic.list_detail import object_detail
from django.contrib.auth.decorators import login_required
from django.views.generic.create_update import update_object, delete_object
from django.views.generic.simple import direct_to_template, redirect_to
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from django.contrib import messages

from forms import NoteForm, NoteFormSet, ActionForm
from models import Note

@login_required
def list(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        formset = NoteFormSet(
            request.POST,
            queryset=Note.objects.filter(user=request.user)
        )

        if formset.is_valid():
            if action == u'delete':
                for form in formset.forms:
                    if form.cleaned_data.get('is_checked'):
                        form.save(commit=False).delete()
                        messages.success(request, 'Notes deleted.')
            return HttpResponseRedirect(reverse("django_notes.views.list"))
    else:
        formset = NoteFormSet(
            queryset=Note.objects.filter(user=request.user)
        )

    return render_to_response(
        "django_notes/note_list.html",
        {'action_form': ActionForm(), 'formset': formset,},
        context_instance=RequestContext(request)
    )
        

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
    return direct_to_template(
        request, "django_notes/note_form.html", {"form": form}
    )

@login_required
def delete(request, object_id=None):
    redirect_url = reverse("django_notes.views.list")
    return delete_object(request, Note, redirect_url, object_id)

@login_required
def update(request, object_id=None):
    return update_object(request, form_class=NoteForm, object_id=object_id)
