from django.db import models
from django.utils.timesince import timesince

from social_simulator.users.models import User

from model_utils.models import TimeStampedModel
from ckeditor.fields import RichTextField


class Post(TimeStampedModel):
    user = models.ForeignKey(User, null=True, blank=True)
    text = RichTextField()

    class Meta:
        abstract = True
        ordering = ('-created', )

    def __str__(self):
        try:
            self.header
        except AttributeError:
            pass
        else:
            return self.header
        try:
            self.theme
        except AttributeError:
            pass
        else:
            return self.theme
        try:
            self.user
        except AttributeError:
            pass
        else:
            return self.user.username
        return self.text[:10]

    @property
    def provider(self):
        return str(self.__class__.__name__).replace('Post', '')

    @property
    def class_name(self):
        return str(self.__class__.__name__)

    @property
    def time_since(self):
        return timesince(self.created)
