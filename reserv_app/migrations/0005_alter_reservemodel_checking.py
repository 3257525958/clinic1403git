# Generated by Django 4.1.7 on 2024-06-16 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserv_app', '0004_reservemodel_checking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservemodel',
            name='checking',
            field=models.CharField(default='false', max_length=20),
        ),
    ]