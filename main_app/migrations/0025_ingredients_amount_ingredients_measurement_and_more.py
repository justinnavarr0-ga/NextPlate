# Generated by Django 4.2 on 2023-05-10 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0024_alter_recipeingredients_ingredient'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredients',
            name='amount',
            field=models.FloatField(default=1),
        ),
        migrations.AddField(
            model_name='ingredients',
            name='measurement',
            field=models.CharField(default='', max_length=6),
        ),
        migrations.AlterField(
            model_name='recipeingredients',
            name='amount',
            field=models.FloatField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='recipeingredients',
            name='ingredient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.ingredients'),
        ),
        migrations.AlterField(
            model_name='recipeingredients',
            name='measurement',
            field=models.CharField(blank=True, max_length=6),
        ),
    ]
