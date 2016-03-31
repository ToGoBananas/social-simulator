from django.db import models
from django.utils.functional import cached_property

from social_simulator.dashboard.models import Post
from model_utils.models import TimeStampedModel

from social_simulator.users.models import User
from django.utils.timesince import timesince


class FacebookPost(Post):
    likes = models.PositiveIntegerField(default=0)

    @property
    def posted(self):
        return timesince(self.created) + ' ago'

    @cached_property
    def comments(self):
        return self.comment_set.order_by('-created')


class FacebookPostLikes(models.Model):
    post = models.OneToOneField(FacebookPost, primary_key=True)
    users = models.ManyToManyField(User)

    # def __str__(self):
    #     return self.post.user.


class Comment(TimeStampedModel):
    post = models.ForeignKey(FacebookPost)
    user = models.ForeignKey(User)
    text = models.TextField(max_length=200)

    def __str__(self):
        return self.text[:50]
