from functools import partial

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


# Shortcuts:
_CharField = partial(models.CharField, max_length=1024)


class TimestampedModel(models.Model):
    """
    Base class with `created` and `modified` fields.
    """
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True


class User(AbstractUser):

    # Authentication fields
    phone = models.CharField(
        _('phone number'),
        blank=True,
        max_length=11,
    )

    # School fields
    school = models.CharField(_('school name'), blank=True, null=True, max_length=100)
    school_address = models.CharField(
        _('school address'),
        blank=True, null=True,
        max_length=300,
    )
    grade = models.IntegerField(blank=True, null=True, default=7)

    # Personal fields
    photo = models.ImageField(_('profile photo'),
                              upload_to='users/%Y/%m/%d',
                              blank=True)
    bio = models.CharField(blank=True, null=True, max_length=250)

    # FIXME: subjects = models.ManyToManyField(Board, related_name="my_boards")

    def __str__(self) -> str:
        return str(self.username)


class Question(TimestampedModel, models.Model):

    author = models.ForeignKey(User, on_delete=models.PROTECT)

    title = _CharField()
    body = models.TextField(blank=True)

    def __str__(self) -> str:
        return f'By {self.author}: {self.title}'