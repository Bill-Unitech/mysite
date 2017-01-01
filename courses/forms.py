from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = [
            "name",
            "email",
            "message",
        ]
    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class' : 'text-input span4'})
        self.fields['email'].widget.attrs.update({'class' : 'text-input span4'})
        self.fields['message'].widget.attrs.update({'class' : 'text-input span8'})