# Generated by Django 4.0.4 on 2022-07-07 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_post_options_post_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='slug',
            new_name='tag',
        ),
    ]
