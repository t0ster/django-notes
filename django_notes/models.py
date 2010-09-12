from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class Note(models.Model):
    title = models.CharField( _('title'), max_length = 128)
    content = models.TextField(_('content'))
    user = models.ForeignKey(User, verbose_name=_('user'))
    
    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _('note')
        verbose_name_plural = _('notes')
