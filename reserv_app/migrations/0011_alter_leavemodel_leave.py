# Generated by Django 4.1.7 on 2024-08-02 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserv_app', '0010_alter_leavemodel_leave'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leavemodel',
            name='leave',
            field=models.TextField(default='0', max_length=10000000000),
        ),
    ]
