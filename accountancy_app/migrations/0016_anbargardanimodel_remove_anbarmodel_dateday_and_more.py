# Generated by Django 4.1.7 on 2024-12-20 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountancy_app', '0015_anbarmodel_dateday_anbarmodel_datemounth_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='anbargardanimodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kalaid', models.CharField(max_length=10)),
                ('value', models.CharField(max_length=20)),
                ('dateyear', models.CharField(max_length=10)),
                ('datemounth', models.CharField(max_length=10)),
                ('dateday', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='anbarmodel',
            name='dateday',
        ),
        migrations.RemoveField(
            model_name='anbarmodel',
            name='datemounth',
        ),
        migrations.RemoveField(
            model_name='anbarmodel',
            name='dateyear',
        ),
    ]
