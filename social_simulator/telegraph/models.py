from django.db import models
from django.core.urlresolvers import reverse

from social_simulator.dashboard.models import Post


class TelegraphPost(Post):
    header = models.CharField(max_length=50)
    header_image = models.ImageField(upload_to='sky/')

    @staticmethod
    def get_url():
        return reverse('telegraph:index')
