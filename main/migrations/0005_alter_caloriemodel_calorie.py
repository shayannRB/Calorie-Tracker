# Generated by Django 5.0.3 on 2024-03-09 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_caloriemodel_options_alter_caloriemodel_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caloriemodel',
            name='calorie',
            field=models.PositiveSmallIntegerField(blank=True, verbose_name='calorie'),
        ),
    ]