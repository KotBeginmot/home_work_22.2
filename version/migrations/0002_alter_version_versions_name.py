# Generated by Django 4.2.4 on 2023-09-05 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('version', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='versions_name',
            field=models.TextField(max_length=150, verbose_name='имя версии'),
        ),
    ]