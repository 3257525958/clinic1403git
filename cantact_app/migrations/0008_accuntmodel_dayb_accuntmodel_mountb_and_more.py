# Generated by Django 4.1.7 on 2024-05-12 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cantact_app', '0007_alter_phonnambermodel_lastname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='accuntmodel',
            name='dayb',
            field=models.CharField(default='0', max_length=3),
        ),
        migrations.AddField(
            model_name='accuntmodel',
            name='mountb',
            field=models.CharField(default='0', max_length=20),
        ),
        migrations.AddField(
            model_name='accuntmodel',
            name='yearb',
            field=models.CharField(default='0', max_length=5),
        ),
    ]
