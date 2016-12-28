from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "name",
            "email",
            "content",
        ]
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class' : 'text-input span4'})
        self.fields['email'].widget.attrs.update({'class' : 'text-input span4'})
        self.fields['content'].widget.attrs.update({'class' : 'text-input span8'})