# Generated by Django 4.1.7 on 2024-06-27 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_app', '0006_workmodel_vahed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workmodel',
            name='vahed',
            field=models.CharField(default='ندارد', max_length=150),
        ),
    ]