# Generated by Django 3.2.12 on 2022-02-17 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0011_delete_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='security',
            name='yahoo_id',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
