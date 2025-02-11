# Generated by Django 4.0.3 on 2022-07-21 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0057_cablesubscription_status_electricity_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cablesubscription',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='electricity',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('success', 'Success'), ('failed', 'Failed')], default='pending', max_length=50),
        ),
    ]
