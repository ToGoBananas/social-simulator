from django.db import models
from social_simulator.users.models import User

from model_utils.models import TimeStampedModel


class Post(TimeStampedModel):
    name = models.CharField(max_length=150)
    user = models.OneToOneField(User)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
