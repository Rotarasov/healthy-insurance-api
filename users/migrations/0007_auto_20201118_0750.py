# Generated by Django 3.1.3 on 2020-11-18 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20201118_0749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('unemployed', 'Unemployed'), ('employed', 'Employed'), ('ic_representative', 'Insurance company representative'), ('ec_representative', 'Employer company representative')], default='__all__', max_length=30, verbose_name='role'),
        ),
    ]