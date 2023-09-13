from django.contrib import admin
# Register your models here.

from account.models import Uye

class UyeAdmin(admin.ModelAdmin):
    list_display = ['email', 'isim_soyisim', 'cep_telefonu','olusturma_tarihi']
    search_fields = ['email', 'isim_soyisim', 'cep_telefonu']
    list_filter = ['email', 'is_active',]
admin.site.register(Uye,UyeAdmin)
