# Generated by Django 4.1.7 on 2024-05-04 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cantact_app', '0003_rename_berthday_savecodphon_berthdayday_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataacont',
            name='berthday',
        ),
        migrations.RemoveField(
            model_name='dataacont',
            name='melicode',
        ),
        migrations.RemoveField(
            model_name='dataacont',
            name='miladiarray',
        ),
        migrations.RemoveField(
            model_name='dataacont',
            name='shamsiarray',
        ),
        migrations.RemoveField(
            model_name='dataacont',
            name='showclandarray',
        ),
    ]
