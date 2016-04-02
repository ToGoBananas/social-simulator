from django.db import models
from social_simulator.users.models import User

from model_utils.models import TimeStampedModel
from ckeditor.fields import RichTextField


class Post(TimeStampedModel):
    user = models.ForeignKey(User)
    text = RichTextField()

    class Meta:
        abstract = True
        ordering = ('-created', )

    def __str__(self):
        return self.user.username

    def provider(self):
        return str(self.__class__.__name__).replace('Post', '')
