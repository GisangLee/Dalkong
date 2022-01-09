# Generated by Django 3.2 on 2022-01-09 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_remove_photo_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='posts.post', verbose_name='게시글'),
            preserve_default=False,
        ),
    ]
