from django import forms
from . import models



class CreateNewPost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ["author","title", "description", "body"]






