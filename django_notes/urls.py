from django.conf.urls.defaults import *

urlpatterns = patterns('',
     (r'^/$', 'django_notes.views.empty_view'),
)
