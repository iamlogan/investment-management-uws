# Generated by Django 4.0.1 on 2022-02-03 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cashflow',
            name='account',
        ),
        migrations.AddField(
            model_name='event',
            name='account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='portfolioapp.investmentaccount'),
            preserve_default=False,
        ),
    ]
