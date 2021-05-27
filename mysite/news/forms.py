from django import forms
from .models import *


class AddNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'photo', 'category', 'is_published']


form = AddNewsForm()
