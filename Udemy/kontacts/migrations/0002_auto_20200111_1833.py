# Generated by Django 3.0.2 on 2020-01-11 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kontacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kontact',
            old_name='listing_it',
            new_name='listing_id',
        ),
    ]