# Generated by Django 4.1.7 on 2024-07-28 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserv_app', '0009_searchmodeltest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leavemodel',
            name='leave',
            field=models.CharField(default='0', max_length=10000),
        ),
    ]