from django.conf.urls.defaults import *

urlpatterns = patterns('',
     (r'^$', 'django_notes.views.list'),
     (r'^create/$', 'django_notes.views.create'),
     (r'^details/(?P<object_id>\d*)/$', 'django_notes.views.details'),
     (r'^delete/$', 'django_notes.views.delete'),
     (r'^delete/(?P<object_id>\d*)/$', 'django_notes.views.delete'),
     (r'^update/(?P<object_id>\d*)/$', 'django_notes.views.update'),
)
