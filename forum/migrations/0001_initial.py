# Generated by Django 3.2.6 on 2021-08-08 11:29

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
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=125, verbose_name='Раздел')),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True, verbose_name='Ссылка на раздел')),
            ],
            options={
                'verbose_name': 'Раздел',
                'verbose_name_plural': 'Разделы',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='SubSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=125, verbose_name='Подраздел')),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True, verbose_name='Ссылка на подраздел')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='chapter', to='forum.chapter', verbose_name='Раздел')),
            ],
            options={
                'verbose_name': 'Подразел',
                'verbose_name_plural': 'Подразделы',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название темы')),
                ('content', models.TextField(max_length=3000, verbose_name='Текст к теме')),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True, verbose_name='Ссылка на тему')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_theme', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь создавший тему')),
                ('sub_section', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='subsection', to='forum.subsection', verbose_name='Подраздел, где находится тема')),
            ],
            options={
                'verbose_name': 'Тема',
                'verbose_name_plural': 'Темы',
                'ordering': ['update'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(db_index=True, help_text='Комментарий превышает 3000 символов', max_length=3000, verbose_name='Комментарий пользователя')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comment', to=settings.AUTH_USER_MODEL, verbose_name='Владелец комментария')),
                ('quote', models.ForeignKey(blank=True, db_column='quote_id', on_delete=django.db.models.deletion.CASCADE, related_name='quote_comments', to='forum.comment', verbose_name='Ссылки на цитаты комментарев')),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.theme')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'ordering': ['created'],
            },
        ),
    ]