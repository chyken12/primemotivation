# Generated by Django 4.0.4 on 2022-07-07 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_rename_slug_category_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='tag',
            new_name='slug',
        ),
    ]
