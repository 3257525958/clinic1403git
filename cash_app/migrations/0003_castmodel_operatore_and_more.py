# Generated by Django 4.1.7 on 2024-05-15 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cash_app', '0002_bankmodel_delete_bank_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='castmodel',
            name='operatore',
            field=models.CharField(default=1, max_length=11),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='castmodel',
            name='melicodevarizande',
            field=models.CharField(max_length=11),
        ),
    ]