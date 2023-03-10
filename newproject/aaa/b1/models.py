from django.db import models

class Footer(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    url = models.CharField(max_length=50, verbose_name='URL')
    icon = models.ImageField(upload_to='icon', verbose_name='Иконка')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Партнеры'
        verbose_name_plural = 'Партнеры'
        ordering = ['name']

# Create your models here.
