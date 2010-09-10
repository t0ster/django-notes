from django.conf.urls.defaults import *

urlpatterns = patterns('',
     (r'^django_notes/', include('django_notes.urls')),
)

