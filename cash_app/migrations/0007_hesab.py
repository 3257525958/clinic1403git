# Generated by Django 4.1.7 on 2025-01-06 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cash_app', '0006_castmodel_bankpeyment'),
    ]

    operations = [
        migrations.CreateModel(
            name='hesab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('onvansherkat', models.CharField(max_length=50, null=True)),
                ('shomarehesabd', models.CharField(max_length=50, null=True)),
                ('shomarekart', models.CharField(max_length=50, null=True)),
                ('shomaresheba', models.CharField(max_length=50, null=True)),
                ('idfroshander', models.CharField(max_length=5, null=True)),
            ],
        ),
    ]
