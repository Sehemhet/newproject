from xmlrpc.client import DateTime
from captcha.fields import CaptchaField

from django import forms
from django.forms import TextInput, Textarea, DateInput

from .models import *
class AddCarsForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Cars
        fields = '__all__'
        # widgets = {
        #     'model': TextInput(attrs={
        #         'placeholder':'модель',
        #     }),
        #     'year': DateInput(attrs={
        #         'placeholder': 'год'
        #     }),
        # }





