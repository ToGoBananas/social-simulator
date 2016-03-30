from django.db import models
from django.utils.functional import cached_property

from social_simulator.dashboard.models import Post
from ckeditor.fields import RichTextField
from model_utils.models import TimeStampedModel

from social_simulator.users.models import User


class FacebookPost(Post):
    text = RichTextField()
    likes = models.PositiveIntegerField(default=0)

    @cached_property
    def comments(self):
        return self.comment_set.all()


class FacebookPostLikes(models.Model):
    post = models.OneToOneField(FacebookPost, primary_key=True)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.post.name


class Comment(TimeStampedModel):
    post = models.ForeignKey(FacebookPost)
    user = models.OneToOneField(User)
    text = models.TextField(max_length=200)

    def __str__(self):
        return self.text
