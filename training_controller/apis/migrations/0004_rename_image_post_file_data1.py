# Generated by Django 3.2.3 on 2021-05-27 03:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0003_alter_post_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='file_data1',
        ),
    ]