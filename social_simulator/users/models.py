# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from model_utils import Choices
from django.conf import settings


@python_2_unicode_compatible
class User(AbstractUser):
    TYPE_CHOICES = Choices('Player', 'Media player', 'Controller')
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    type = models.CharField(choices=TYPE_CHOICES, max_length=20, null=True)
    avatar = models.ImageField(upload_to='avatars', null=True)

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
