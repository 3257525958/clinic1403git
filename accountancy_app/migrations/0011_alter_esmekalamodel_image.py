# Generated by Django 4.1.7 on 2024-09-06 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountancy_app', '0010_esmekalamodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='esmekalamodel',
            name='image',
            field=models.ImageField(null=True, upload_to='image/kala'),
        ),
    ]
