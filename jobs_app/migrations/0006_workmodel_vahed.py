# Generated by Django 4.1.7 on 2024-06-26 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_app', '0005_workmodel_idjob'),
    ]

    operations = [
        migrations.AddField(
            model_name='workmodel',
            name='vahed',
            field=models.CharField(default='0', max_length=150),
        ),
    ]