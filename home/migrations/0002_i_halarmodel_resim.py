# Generated by Django 4.2.5 on 2023-09-13 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='i̇halarmodel',
            name='resim',
            field=models.ImageField(blank=True, null=True, upload_to='ihalar/'),
        ),
    ]
