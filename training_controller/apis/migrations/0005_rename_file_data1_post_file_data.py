# Generated by Django 3.2.3 on 2021-05-27 03:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0004_rename_image_post_file_data1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='file_data1',
            new_name='file_data',
        ),
    ]
