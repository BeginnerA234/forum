# Generated by Django 3.2.6 on 2021-08-08 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0007_auto_20210808_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(help_text='Комментарий превышает 5000 символов', verbose_name='Комментарий пользователя'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='content',
            field=models.TextField(help_text='Комментарий превышает 5000 символов', verbose_name='Текст к теме'),
        ),
    ]
