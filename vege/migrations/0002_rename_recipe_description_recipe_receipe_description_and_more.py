# Generated by Django 5.1.4 on 2025-01-02 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='recipe_description',
            new_name='receipe_description',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='recipe_image',
            new_name='receipe_image',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='recipe_name',
            new_name='receipe_name',
        ),
    ]
