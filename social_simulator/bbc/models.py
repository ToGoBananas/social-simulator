from django.db import models
from django.core.urlresolvers import reverse

from model_utils.fields import AutoCreatedField

from social_simulator.dashboard.models import Post
from social_simulator.users.models import User


class BbcPost(Post):
    header = models.CharField(max_length=100)
    header_image = models.ImageField(upload_to='bbc/')
    short_text = models.CharField(max_length=50, null=True)
    tag = models.CharField(max_length=20, null=True)

    @staticmethod
    def get_url():
        return reverse('bbc:index')

