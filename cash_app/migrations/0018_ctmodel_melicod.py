# Generated by Django 4.1.7 on 2024-07-20 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cash_app', '0017_remove_ctmodel_cashmethod_remove_ctmodel_datemiladi_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ctmodel',
            name='melicod',
            field=models.CharField(default='0', max_length=10),
        ),
    ]
