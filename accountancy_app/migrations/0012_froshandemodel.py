# Generated by Django 4.1.7 on 2024-12-20 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountancy_app', '0011_alter_esmekalamodel_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='froshandemodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('phonnumber', models.CharField(max_length=11)),
            ],
        ),
    ]
