# Generated by Django 4.1.7 on 2024-09-05 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('it_app', '0009_remove_homeimgmodel_size_remove_homemobilemodel_size'),
    ]

    operations = [
        migrations.DeleteModel(
            name='homeimgmodel',
        ),
        migrations.DeleteModel(
            name='homemenosarimodel',
        ),
        migrations.DeleteModel(
            name='homemobilemodel',
        ),
        migrations.DeleteModel(
            name='mesaagecuntermodel',
        ),
        migrations.DeleteModel(
            name='mesaagetextmodel',
        ),
    ]
