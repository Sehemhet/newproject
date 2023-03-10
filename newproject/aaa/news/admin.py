from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'article', 'publish') #отражение полей в админке
    list_display_links = ('id', 'article') #поля ссылка в админке
    search_fields = ('article', 'content') #поле поиска
    list_editable = ('publish',) #публикация
    list_filter = ('publish', 'time_create') # добавление фильтра
    prepopulated_fields = {"slug": ("article",)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
