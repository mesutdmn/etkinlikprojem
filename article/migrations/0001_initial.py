# Generated by Django 4.0.3 on 2022-04-25 20:44

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Katilimci',
            fields=[
                ('tc_no', models.IntegerField(primary_key=True, serialize=False, verbose_name='No')),
                ('isim', models.CharField(max_length=50, verbose_name='İsim')),
                ('soy_isim', models.CharField(max_length=50, verbose_name='Sotİsim')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Başlık')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Açıklama')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('etkinlik_poster', models.FileField(blank=True, null=True, upload_to='', verbose_name='Poster')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Yazar')),
            ],
            options={
                'verbose_name': 'Etkinlik',
                'verbose_name_plural': 'Etkinlikler',
            },
        ),
    ]
