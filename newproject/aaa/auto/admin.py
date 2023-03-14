from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

class CarsAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'slug', 'get_html_photo1')   #отражение полей в админке
    list_display_links = ('brand',)                     #поля ссылка в админке
    list_filter = ('brand',)                            # добавление фильтра
    prepopulated_fields = {"slug":("model","year",)}   #slug формирование

    def get_html_photo1(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=100px>")
 
class BrandsAdmin(admin.ModelAdmin):
    list_display = ('brand', 'get_html_photo2', 'slug')
    prepopulated_fields = {"slug": ("brand",)}

    def get_html_photo2(self, object):
        if object.logo:
            return mark_safe(f"<img src='{object.logo.url}' width=70px>")

class TypeDriveAdmin(admin.ModelAdmin):
    list_display = ('id', 'type')

class TypeEngineAdmin(admin.ModelAdmin):
    list_display = ('id', 'type')

class TypeRarityAdmin(admin.ModelAdmin):
    list_display = ('id', 'type')

class CountyAdmin(admin.ModelAdmin):
    list_display = ('type', 'get_html_photo3')

    def get_html_photo3(self, object):
        if object.flag:
            return mark_safe(f"<img src='{object.flag.url}' width=70px>")

class TypeClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'type')

admin.site.register(Cars, CarsAdmin)
admin.site.register(Brands, BrandsAdmin)
admin.site.register(TypeDrive, TypeDriveAdmin)
admin.site.register(TypeEngine, TypeEngineAdmin)
admin.site.register(TypeRarity, TypeRarityAdmin)
admin.site.register(County, CountyAdmin)
admin.site.register(TypeClass, TypeClassAdmin)

