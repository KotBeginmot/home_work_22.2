# Generated by Django 4.2.4 on 2023-08-26 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_contactdata'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactdata',
            options={'verbose_name': 'Контакт', 'verbose_name_plural': 'Контакты'},
        ),
        migrations.AlterField(
            model_name='contactdata',
            name='phone',
            field=models.TextField(verbose_name='телефон'),
        ),
    ]