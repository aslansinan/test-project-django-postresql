from django.contrib import admin

from home.models import İhalarModel, İhaUyeModel, Kategoriler


# Register your models here.
class İhalarAdmin(admin.ModelAdmin):
    list_display = ['iha','resim', 'olusturma_tarihi', 'guncelleme_tarihi']


admin.site.register(İhalarModel, İhalarAdmin)

class KategorilerAdmin(admin.ModelAdmin):
    list_display = ['kategori_adi', 'olusturma_tarihi', 'guncelleme_tarihi']


admin.site.register(Kategoriler, KategorilerAdmin)

class İhaUyeAdmin(admin.ModelAdmin):
    list_display = ['ihalar','uye', 'olusturma_tarihi', 'guncelleme_tarihi']


admin.site.register(İhaUyeModel, İhaUyeAdmin)