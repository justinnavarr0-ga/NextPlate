# Generated by Django 4.2 on 2023-05-13 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0037_alter_savedrecipes_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredients',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='ingredients',
            name='measurement',
        ),
        migrations.RemoveField(
            model_name='recipeingredients',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='recipeingredients',
            name='measurement',
        ),
        migrations.RemoveField(
            model_name='recipeinstructions',
            name='step',
        ),
    ]
