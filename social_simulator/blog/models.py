from django.db import models
from django.core.urlresolvers import reverse
from django.utils.functional import cached_property

from model_utils.fields import AutoCreatedField

from social_simulator.dashboard.models import Post
from social_simulator.users.models import User


class BlogPost(Post):
    header = models.CharField(max_length=100)

    @staticmethod
    def get_url():
        return reverse('blog:index')

    @property
    def comments(self):
        return self.blogcomment_set.all()


class BlogComment(models.Model):
    created = AutoCreatedField()
    user = models.ForeignKey(User)
    text = models.TextField(max_length=400)
    post = models.ForeignKey(BlogPost)
    likes = models.PositiveIntegerField(default=0)
