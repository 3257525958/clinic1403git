# Generated by Django 4.1.7 on 2024-06-17 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cash_app', '0010_remove_castmodel_pardakht'),
    ]

    operations = [
        migrations.AddField(
            model_name='castmodel',
            name='beyane',
            field=models.CharField(default='0', max_length=100),
        ),
    ]
