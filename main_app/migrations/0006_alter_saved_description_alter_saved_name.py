# Generated by Django 4.2 on 2023-05-09 06:21

from django.db import migrations, models
import main_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_saved_description_saved_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saved',
            name='description',
            field=models.TextField(verbose_name=main_app.models.Recipe),
        ),
        migrations.AlterField(
            model_name='saved',
            name='name',
            field=models.CharField(verbose_name=main_app.models.Recipe),
        ),
    ]
