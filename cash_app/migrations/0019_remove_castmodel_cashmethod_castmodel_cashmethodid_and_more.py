# Generated by Django 4.1.7 on 2024-07-25 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cash_app', '0018_ctmodel_melicod'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='castmodel',
            name='cashmethod',
        ),
        migrations.AddField(
            model_name='castmodel',
            name='cashmethodid',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AddField(
            model_name='castmodel',
            name='cashmethodname',
            field=models.CharField(default='0', max_length=100),
        ),
    ]