# Generated by Django 4.2 on 2023-05-10 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0026_alter_recipeingredients_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredients',
            name='amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='ingredients',
            name='measurement',
            field=models.CharField(max_length=6),
        ),
    ]