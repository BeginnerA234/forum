# Generated by Django 3.2.6 on 2021-08-08 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(db_index=True, help_text='Комментарий превышает 3000 символов', max_length=3000, verbose_name='Комментарий пользователm'),
        ),
    ]
