# Generated by Django 4.0.3 on 2022-06-19 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_remove_provider_package_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('name', models.CharField(default='', max_length=200)),
                ('description', models.CharField(default='', max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Bill Categories',
            },
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biller_id', models.IntegerField()),
                ('name', models.CharField(default='', max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.billcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biller_id', models.IntegerField()),
                ('name', models.CharField(default='', max_length=200)),
                ('amount', models.CharField(default='', max_length=200)),
                ('payment_code', models.CharField(default='', max_length=200)),
                ('charges', models.CharField(default='', max_length=200)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=50)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.package')),
            ],
        ),
        migrations.AddField(
            model_name='cablesubscription',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.item'),
        ),
        migrations.AddField(
            model_name='electricity',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.item'),
        ),
    ]
