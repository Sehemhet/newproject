from django import forms
from django.forms import TextInput, Textarea, Select, FileInput

from .models import *
from captcha.fields import CaptchaField
class AddPostForm(forms.ModelForm):
    # captcha = CaptchaField()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'
    class Meta:
        model = Post
        fields = ['article','content', 'cat', 'photo']
        widgets = {
            'article': TextInput(attrs={
                'placeholder':'Название статьи',
            }),
            'content': Textarea(attrs={
                'placeholder': 'Cтатья'
            }),
        }






