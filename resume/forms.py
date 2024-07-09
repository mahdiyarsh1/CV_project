from django import forms
from .models import CommentPost
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']


class Comment(forms.Form):
    name = forms.CharField(max_length=50, min_length=5,
                           label='نام', required=False)
    text = forms.CharField(widget=forms.Textarea, label='توضیحات')
