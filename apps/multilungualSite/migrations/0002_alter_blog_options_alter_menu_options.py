# Generated by Django 4.2.7 on 2023-11-06 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multilungualSite', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name': 'Blog', 'verbose_name_plural': 'Blog'},
        ),
        migrations.AlterModelOptions(
            name='menu',
            options={'verbose_name': 'Menu', 'verbose_name_plural': 'Menu'},
        ),
    ]
