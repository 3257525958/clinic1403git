# Generated by Django 4.1.7 on 2024-12-28 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserv_app', '0009_alter_reservemodel_vaziyatereserv'),
    ]

    operations = [
        migrations.AddField(
            model_name='fpeseshktestmodel',
            name='bankpeyment',
            field=models.CharField(default='-3', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='reservemodel',
            name='bankpeyment',
            field=models.CharField(default='-3', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='reservemodeltest',
            name='bankpeyment',
            field=models.CharField(default='-3', max_length=200, null=True),
        ),
    ]