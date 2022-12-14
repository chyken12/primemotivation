# Generated by Django 4.0.4 on 2022-06-30 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_category_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-date',)},
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
