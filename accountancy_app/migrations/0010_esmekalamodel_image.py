# Generated by Django 4.1.7 on 2024-09-06 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountancy_app', '0009_alter_esmekalamodel_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='esmekalamodel',
            name='image',
            field=models.ImageField(null=True, upload_to='image/homepc'),
        ),
    ]
