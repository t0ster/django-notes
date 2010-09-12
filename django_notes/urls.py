from django.conf.urls.defaults import *

urlpatterns = patterns('',
     (r'^$', 'django_notes.views.list_notes'),
     (r'^delete/$', 'django_notes.views.delete'),
     (r'^delete/(?P<note_id>\d*)/$', 'django_notes.views.delete'),
     (r'^note/(?P<note_id>\d*)/$', 'django_notes.views.edit'),
)
