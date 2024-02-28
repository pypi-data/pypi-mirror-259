from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Notification(models.Model):
    """
    Stores a single notification entry, related to user model.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=128, verbose_name=_("title"))
    content = models.TextField(verbose_name=_("content"))
    is_read = models.BooleanField(default=False, db_index=True, verbose_name=_("read"))
    is_important = models.BooleanField(default=False, verbose_name=_("important"))
    url = models.URLField(max_length=200, blank=True, null=True, verbose_name=_("link"))
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name=_("created at"))
