# Generated by Django 5.0.3 on 2024-03-09 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_caloriemodel_created_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caloriemodel',
            name='calorie',
            field=models.PositiveSmallIntegerField(blank=True, max_length=250, verbose_name='calorie'),
        ),
    ]
