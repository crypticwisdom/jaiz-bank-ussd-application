# Generated by Django 4.0.3 on 2022-07-08 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0045_alter_customer_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='data_amount',
            field=models.FloatField(default=0.0, max_length=20),
        ),
    ]
