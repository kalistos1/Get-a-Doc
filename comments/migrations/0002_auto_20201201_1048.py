# Generated by Django 3.1.2 on 2020-12-01 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name_plural': 'comments'},
        ),
        migrations.AlterModelTable(
            name='comment',
            table='comments',
        ),
    ]
