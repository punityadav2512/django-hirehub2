# Generated by Django 4.0.1 on 2022-02-12 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cell', '0002_post'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Posts',
        ),
    ]
