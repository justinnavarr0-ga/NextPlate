# Generated by Django 4.2 on 2023-05-10 01:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_remove_savedrecipes_recipes_savedrecipes_recipes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='savedrecipes',
            name='name',
        ),
    ]
