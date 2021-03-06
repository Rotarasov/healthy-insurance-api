# Generated by Django 3.1.3 on 2020-11-30 16:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance_companies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurancecompany',
            name='company_employees_num',
            field=models.PositiveIntegerField(default=100, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='company employees num'),
        ),
        migrations.AlterField(
            model_name='insurancecompany',
            name='company_sale',
            field=models.FloatField(default=0.1, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='company sale'),
        ),
    ]
