# Generated by Django 4.1.7 on 2024-09-19 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('it_app', '0016_alter_mesaagemodel_textmessage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mesaagemodel',
            name='phonnumber',
        ),
        migrations.AddField(
            model_name='mesaagemodel',
            name='hour',
            field=models.IntegerField(default=0, max_length=2),
        ),
        migrations.AddField(
            model_name='mesaagemodel',
            name='messagemethod',
            field=models.CharField(default='پیامک', max_length=11),
        ),
        migrations.AddField(
            model_name='mesaagemodel',
            name='minute',
            field=models.IntegerField(default=0, max_length=2),
        ),
    ]
