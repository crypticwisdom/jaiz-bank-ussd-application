# Generated by Django 4.0.3 on 2022-04-05 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_alter_customer_beneficiaries_alter_customerotp_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeraccount',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
