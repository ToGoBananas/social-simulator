from django.db import models
from django.core.urlresolvers import reverse

from social_simulator.dashboard.models import Post


class SkyPost(Post):
    header = models.CharField(max_length=50)
    header_image = models.ImageField(upload_to='sky/')
    short_text = models.CharField(max_length=100)

    @staticmethod
    def get_url():
        return reverse('sky_news:index')
