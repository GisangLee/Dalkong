# Generated by Django 3.2 on 2022-01-09 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_post_post_photos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='post',
        ),
    ]
