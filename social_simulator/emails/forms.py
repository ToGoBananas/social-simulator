from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Button

from .models import Message


class MessageCreateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(MessageCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'create/'
        self.helper.form_id = 'create_form'
        self.helper.add_input(Button('send_message', 'Send message', css_class='btn-primary'))

    class Meta:
        model = Message
        fields = ['recipients', 'subject', 'text']
