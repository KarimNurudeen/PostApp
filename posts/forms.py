from django import forms
from .import models


class CreatePost(forms.ModelForm):
    class Meta:
         model = models.post
         fields = ['title', 'body', 'slug', 'banner']




   