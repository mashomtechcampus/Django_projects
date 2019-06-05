from django import forms
from .models import Topic,Post


class NewTopicForm (forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={
        'row':5 , 'placeholder' : 'what is the message'

    }),max_length=5000,help_text='the max length is 5000')
    class Meta :
        model =Topic
        fields = ['subject', 'message']


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['message']