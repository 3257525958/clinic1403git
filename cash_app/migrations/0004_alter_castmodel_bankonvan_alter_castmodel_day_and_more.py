# Generated by Django 4.1.7 on 2024-05-15 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cash_app', '0003_castmodel_operatore_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='castmodel',
            name='bankonvan',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='castmodel',
            name='day',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='castmodel',
            name='melicodevarizande',
            field=models.CharField(default='0', max_length=11),
        ),
        migrations.AlterField(
            model_name='castmodel',
            name='mounth',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='castmodel',
            name='operatore',
            field=models.CharField(default='0', max_length=11),
        ),
        migrations.AlterField(
            model_name='castmodel',
            name='persone',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='castmodel',
            name='peyment',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='castmodel',
            name='selectjob',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='castmodel',
            name='year',
            field=models.CharField(default='0', max_length=100),
        ),
    ]
