# Generated by Django 4.0.3 on 2022-05-05 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0015_veritabanisertifikalar_sertifika_mevcut'),
    ]

    operations = [
        migrations.AddField(
            model_name='veritabanisertifikalar',
            name='ad_soyad',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Ad Soyad'),
        ),
    ]
