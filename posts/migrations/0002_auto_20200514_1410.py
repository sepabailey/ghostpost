# Generated by Django 3.0.6 on 2020-05-14 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postitem',
            old_name='likes',
            new_name='results',
        ),
    ]
