from django.db import models
from django.core.urlresolvers import reverse

from model_utils.models import TimeStampedModel

from social_simulator.dashboard.models import Post
from social_simulator.users.models import User


class TwitterPost(Post):
    retweets = models.PositiveIntegerField(default=0)

    @staticmethod
    def get_url():
        return reverse('twitter:index')


class TwitterPostTwitts(models.Model):
    post = models.OneToOneField(TwitterPost, primary_key=True)
    users = models.ManyToManyField(User)
