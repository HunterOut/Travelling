# Generated by Django 3.0.4 on 2020-04-22 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='route',
            old_name='accross_cities',
            new_name='across_cities',
        ),
    ]
