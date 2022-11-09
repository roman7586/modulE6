# Generated by Django 4.0.5 on 2022-11-09 19:12

from django.db import migrations, models
import room.models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatuser',
            name='avatar',
            field=models.ImageField(default='avatars/default.jpg', height_field='150', upload_to=room.models.user_directory_path, width_field='150'),
        ),
    ]
