from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    """Task model."""

    owner = models.ForeignKey(
        get_user_model(),
        verbose_name=_('Task owner'),
        related_name='tasks',
        on_delete=models.CASCADE,
    )
    summary = models.CharField(
        _('Task summary'),
        max_length=250,
    )
    body = models.TextField(  # noqa: DJ01
        _('Task body'),
        null=True,
    )

    class Meta:
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')
        ordering = ('id', )
