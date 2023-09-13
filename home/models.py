from django.db import models

from account.models import Uye




class Kategoriler(models.Model):
    kategori_adi = models.CharField(max_length=50,null=True,blank=True)
    olusturma_tarihi = models.DateTimeField(auto_now_add=True)
    guncelleme_tarihi = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-id']
        verbose_name = u'kategoriler'
        verbose_name_plural = u'Kategoriler'

    def __str__(self):
        return self.kategori_adi
# Create your models here.
class İhalarModel(models.Model):
    iha=models.CharField(max_length=50,null=True,blank=True)
    kategori = models.ForeignKey(Kategoriler, on_delete=models.PROTECT, blank=True, null=False)
    marka=models.CharField(max_length=50,null=True,blank=True)
    model=models.CharField(max_length=50,null=True,blank=True)
    fiyat = models.IntegerField(max_length=50,null=True,blank=True)
    resim = models.ImageField(upload_to='img/', null=True, blank=True)
    olusturma_tarihi = models.DateTimeField(auto_now_add=True)
    guncelleme_tarihi = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']
        verbose_name = u'İHA'
        verbose_name_plural = u'İHALAR'

    def __str__(self):
        return self.iha
class İhaUyeModel(models.Model):
    ihalar=models.ForeignKey(İhalarModel, on_delete=models.PROTECT, blank=True, null=False )
    uye = models.ForeignKey(Uye, on_delete=models.PROTECT, blank=True, null=False)
    olusturma_tarihi = models.DateTimeField(auto_now_add=True)
    guncelleme_tarihi = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']
        verbose_name = u'uye ihaları'
        verbose_name_plural = u'uye ihaları'

    def __str__(self):
        return self.ihalar