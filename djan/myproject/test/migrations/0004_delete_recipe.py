# Generated by Django 5.1.1 on 2024-11-04 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0003_rename_recipes_recipe'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Recipe',
        ),
    ]