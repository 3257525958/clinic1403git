# Generated by Django 4.1.7 on 2024-09-14 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('it_app', '0011_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='mesaagemodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('melicod', models.CharField(default='0', max_length=11)),
                ('dateyear', models.CharField(default='0', max_length=100)),
                ('datemuonth', models.CharField(default='0', max_length=100)),
                ('dateday', models.CharField(default='0', max_length=100)),
                ('phonnumber', models.CharField(default='0', max_length=100)),
                ('sendermelicod', models.CharField(default='0', max_length=10)),
                ('textmessage', models.TextField(default='0', max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='mesaagecuntermodel',
        ),
    ]