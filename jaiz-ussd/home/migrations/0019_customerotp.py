# Generated by Django 4.0.2 on 2022-03-31 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_airtime_customer_account_airtime_network'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerOTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.CharField(default='24608', max_length=4)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.customer')),
            ],
        ),
    ]
