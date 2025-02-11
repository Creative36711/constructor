# Generated by Django 5.0.4 on 2024-12-09 10:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Режим игры')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Режим игры',
                'verbose_name_plural': 'Режимы игры',
                'ordering': ['id'],
            },
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-time_create', 'title'], 'verbose_name': 'Новости', 'verbose_name_plural': 'Новости'},
        ),
        migrations.CreateModel(
            name='Maps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название карты')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('version', models.CharField(max_length=10, verbose_name='Версия карты')),
                ('content', models.TextField(blank=True, verbose_name='Описание карты')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Изображение')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
                ('author', models.CharField(max_length=50, verbose_name='Автор')),
                ('file', models.FileField(upload_to='maps/%Y/%m/%d/', verbose_name='Карта')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='Просмотры')),
                ('downloads', models.PositiveIntegerField(default=0, verbose_name='Загрузки')),
                ('mode', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.mode', verbose_name='Режим игры')),
            ],
            options={
                'verbose_name': 'Карта',
                'verbose_name_plural': 'Карты',
                'ordering': ['-time_update', 'title'],
            },
        ),
    ]
