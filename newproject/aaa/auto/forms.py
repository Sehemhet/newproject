from xmlrpc.client import DateTime
from captcha.fields import CaptchaField

from django import forms
from django.forms import TextInput, Textarea, DateInput, SlugField, NumberInput, FloatField

from .models import *
class AddCarsForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Cars
        fields = '__all__'
        widgets = {
            'model': TextInput(attrs={
                'placeholder':'модель',
            }),
            'year': DateInput(attrs={
                'placeholder': 'год'
            }),
            'slug': TextInput(attrs={
                'placeholder': 'URL'
            }),
            'level': NumberInput(attrs={
                'placeholder': 'Уровень'
            }),
            'price': NumberInput(attrs={
                'placeholder': 'Цена'
            }),
            'speed': NumberInput(attrs={
                'placeholder': 'Скорость',
                'step':'0.1'
            }),
            'control': NumberInput(attrs={
                'placeholder': 'Управление',
                'step':'0.1'
            }),
            'acceleration': NumberInput(attrs={
                'placeholder': 'Ускорение',
                'step':'0.1'
            }),
            'start': NumberInput(attrs={
                'placeholder': 'Разгон',
                'step':'0.1'
            }),
            'brake': NumberInput(attrs={
                'placeholder': 'Торможение',
                'step':'0.1'
            }),
            'kW': NumberInput(attrs={
                'placeholder': 'кВт',
            }),
            'Hp': NumberInput(attrs={
                'placeholder': 'Л.с.',
            }),
            'Hm': NumberInput(attrs={
                'placeholder': 'Н/м',
            }),
            'weight': NumberInput(attrs={
                'placeholder': 'Вес',
            }),
            'center': NumberInput(attrs={
                'placeholder': 'Фронтальная нагрузка',
            }),
            'volume': NumberInput(attrs={
                'placeholder': 'Объем',
            }),
            'top_speed': NumberInput(attrs={
                'placeholder': 'макс. скорость',
            }),
            'start097': NumberInput(attrs={
                'placeholder': '0-97км/ч',
            }),
            'start161': NumberInput(attrs={
                'placeholder': '0-161км/ч',
            }),
            'brake097': NumberInput(attrs={
                'placeholder': '97-0 км/ч',
            }),
            'brake161': NumberInput(attrs={
                'placeholder': '161-0 км/ч',
            }),
            'load97': NumberInput(attrs={
                'placeholder': 'нагрузка 97 км/ч',
            }),
            'load193': NumberInput(attrs={
                'placeholder': 'нагрузка 193 км/ч',
            }),
            }





