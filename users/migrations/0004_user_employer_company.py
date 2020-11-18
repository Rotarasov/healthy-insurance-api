# Generated by Django 3.1.3 on 2020-11-17 23:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employer_companies', '0001_initial'),
        ('users', '0003_auto_20201117_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='employer_company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employees', related_query_name='employee', to='employer_companies.employercompany'),
        ),
    ]