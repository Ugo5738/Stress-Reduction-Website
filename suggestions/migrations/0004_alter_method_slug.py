# Generated by Django 3.2.3 on 2021-06-04 20:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('suggestions', '0003_method_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='method',
            name='slug',
            field=models.SlugField(),
        ),
    ]
