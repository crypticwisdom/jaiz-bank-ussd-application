# Generated by Django 4.0.1 on 2022-02-08 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_customer_phone_remove_customer_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='bvn',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='customer',
            name='msisdn',
            field=models.CharField(default='', max_length=20),
        ),
    ]
