# Generated by Django 3.2.6 on 2021-08-09 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0008_auto_20210808_2207'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subsection',
            options={'ordering': ['id'], 'verbose_name': 'Подразел', 'verbose_name_plural': 'Подразделы'},
        ),
    ]