# Generated by Django 4.1 on 2023-03-01 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0061_airtime_pin_tries_cablesubscription_pin_tries_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='data_amount',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
