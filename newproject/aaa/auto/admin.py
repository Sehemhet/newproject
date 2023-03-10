from django.contrib import admin
from .models import *

class CarsAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'slug') #отражение полей в админке
    list_display_links = ('brand',) #поля ссылка в админке
    search_fields = ('brand', 'model', 'year') #поле поиска
    list_filter = ('brand', 'model', 'year') # добавление фильтра
    prepopulated_fields = {"slug": ("model","year",)}

class BrandsAdmin(admin.ModelAdmin):
    list_display = ('brand', 'logo', 'slug') #отражение полей в админке
    list_display_links = ('brand',) #поля ссылка в админке
    search_fields = ('brand',) #поле поиска
    list_filter = ('brand',) # добавление фильтра
    prepopulated_fields = {"slug": ("brand",)}

class TypeDriveAdmin(admin.ModelAdmin):
    list_display = ('id', 'type') #отражение полей в админке
    list_display_links = ('type',) #поля ссылка в админке
    search_fields = ('type',) #поле поиска
    list_filter = ('type',) # добавление фильтра

class TypeEngineAdmin(admin.ModelAdmin):
    list_display = ('id', 'type') #отражение полей в админке
    list_display_links = ('type',) #поля ссылка в админке
    search_fields = ('type',) #поле поиска
    list_filter = ('type',) # добавление фильтра

class TypeRarityAdmin(admin.ModelAdmin):
    list_display = ('id', 'type') #отражение полей в админке
    list_display_links = ('type',) #поля ссылка в админке
    search_fields = ('type',) #поле поиска
    list_filter = ('type',) # добавление фильтра

class CountyAdmin(admin.ModelAdmin):
    list_display = ('type', 'flag') #отражение полей в админке
    list_display_links = ('type',) #поля ссылка в админке
    search_fields = ('type',) #поле поиска
    list_filter = ('type',) # добавление фильтра

class TypeClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'type') #отражение полей в админке
    list_display_links = ('type',) #поля ссылка в админке
    search_fields = ('type',) #поле поиска
    list_filter = ('type',) # добавление фильтра


admin.site.register(Cars, CarsAdmin)
admin.site.register(Brands, BrandsAdmin)
admin.site.register(TypeDrive, TypeDriveAdmin)
admin.site.register(TypeEngine, TypeEngineAdmin)
admin.site.register(TypeRarity, TypeRarityAdmin)
admin.site.register(County, CountyAdmin)
admin.site.register(TypeClass, TypeClassAdmin)

