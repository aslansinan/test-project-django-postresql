from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.db import models

class UyeManager(BaseUserManager):
    def create_user(self, email, isim_soyisim, password=None):
        if not email:
            raise ValueError('Kullanıcının Mail Adresi Olmalı')

        user = Uye(
            email=UyeManager.normalize_email(email),
            isim_soyisim=isim_soyisim,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, isim_soyisim, password):
        if not email:
            raise ValueError('Kullanıcının Mail Adresi Olmalı')
        user = Uye(
            email=UyeManager.normalize_email(email),
            isim_soyisim=isim_soyisim,
        )
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)

        user.save(using=self._db)
        return user


class Uye(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    isim_soyisim = models.CharField(max_length=255)
    # dogum_gunu = models.DateField(blank = True, null = True)
    cep_telefonu = models.CharField(max_length=15, null=True, unique=True)
    CHOICES = (
        ("erkek", "Erkek"),
        ("kadin", "Kadın")
    )

    is_staff = models.BooleanField('staff status', default=False,
                                   help_text='Designates whether the user can log into this admin site.')

    is_active = models.BooleanField('active', default=True,
                                    help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')
    olusturma_tarihi = models.DateTimeField(auto_now_add=True)
    guncelleme_tarihi = models.DateTimeField(auto_now=True)

    objects = UyeManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['isim_soyisim']
    groups = models.ManyToManyField(Group, verbose_name='groups', blank=True, related_name='uye_set')
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='uye_set',
        help_text='Specific permissions for this user.',
    )
    class Meta:
        verbose_name = u"Üye"
        verbose_name_plural = u"Üyeler"

    def get_full_name(self):
        full_name = '%s' % (self.isim_soyisim)
        return full_name.strip()

    def get_short_name(self):
        return self.isim_soyisim

    def _str_(self):
        full_name = '%s' % (self.isim_soyisim)
        return full_name.strip()