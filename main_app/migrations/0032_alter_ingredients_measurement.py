# Generated by Django 4.2 on 2023-05-11 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0031_alter_ingredients_measurement_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredients',
            name='measurement',
            field=models.CharField(choices=[('oz', 'ounce'), ('g', 'gram'), ('lb', 'pound'), ('kg', 'kilogram'), ('pinch', 'pinch'), ('l', 'liter'), ('gal', 'Gallon'), ('pint', 'Pint'), ('qt', 'Quart'), ('ml', 'Mililiter'), ('cup', 'Cup'), ('tbsp', 'tablespoon'), ('tsp', 'teaspoon')], default='oz', max_length=6),
        ),
    ]
