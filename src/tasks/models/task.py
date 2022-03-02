from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    owner = models.ForeignKey(
        get_user_model(),
        verbose_name=_("Task owner"),
        related_name='tasks',
        on_delete=models.CASCADE,
    )
    summary = models.CharField(
        _("Task summary"),
        max_length=250,
    )
    body = models.TextField(
        _("Task body"),
        null=True,
    )

    class Meta:
        verbose_name = _("Card")
        verbose_name_plural = _("Cards")
