# Generated by Django 4.1.7 on 2024-03-29 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cantact_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='dataacont',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('melicode', models.CharField(default='0', max_length=20)),
                ('phonnumber', models.CharField(default='0', max_length=20)),
                ('berthday', models.CharField(max_length=100)),
                ('miladiarray', models.CharField(default='0', max_length=5000)),
                ('shamsiarray', models.CharField(default='0', max_length=5000)),
                ('showclandarray', models.CharField(default='0', max_length=5000)),
            ],
        ),
    ]
