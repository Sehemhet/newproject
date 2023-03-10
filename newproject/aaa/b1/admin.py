from django.contrib import admin
from .models import *

class FooterAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon') #отражение полей в админке
    list_display_links = ('url',) #поля ссылка в админке

admin.site.register(Footer)

# Register your models here.
