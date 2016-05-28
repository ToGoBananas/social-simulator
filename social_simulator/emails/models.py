from django.db import models
from social_simulator.users.models import User
from model_utils.fields import StatusField, AutoCreatedField
from model_utils import Choices
from model_utils.models import TimeStampedModel


class Message(models.Model):
    STATUS = Choices('read', 'send')
    sender = models.ForeignKey(User, related_name='message_senders')
    recipients = models.ManyToManyField(User, related_name='message_recipients')
    status = StatusField(default='send')
    created = AutoCreatedField()
    subject = models.CharField(max_length=50)
    text = models.TextField(max_length=500)

    def str(self):
        return self.sender.username + ' ' + self.subject
