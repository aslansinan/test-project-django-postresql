# Generated by Django 4.2.5 on 2023-09-13 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_kategoriler_guncelleme_tarihi_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='i̇halarmodel',
            name='kategori',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.PROTECT, to='home.kategoriler'),
            preserve_default=False,
        ),
    ]
