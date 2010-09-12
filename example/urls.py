from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     (r'', include('django_notes.urls')),
     (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'admin/login.html'}),
     (r'^accounts/', include('django.contrib.auth.urls')),
     (r'^admin/', include(admin.site.urls)),
     (r'^tinymce/', include('tinymce.urls')),
)

if settings.SERVE_MEDIA:
    urlpatterns += patterns("",
        (r"", include("staticfiles.urls")),
    )
