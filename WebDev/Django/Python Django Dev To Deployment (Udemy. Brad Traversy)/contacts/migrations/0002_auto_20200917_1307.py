# Generated by Django 3.1.1 on 2020-09-17 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='listin_id',
            new_name='listing_id',
        ),
    ]
