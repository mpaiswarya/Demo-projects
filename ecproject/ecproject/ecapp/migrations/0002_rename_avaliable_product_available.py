# Generated by Django 4.1.3 on 2022-12-09 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='available',
            new_name='available',
        ),
    ]
