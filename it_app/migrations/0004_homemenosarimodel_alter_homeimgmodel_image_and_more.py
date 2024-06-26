# Generated by Django 4.1.7 on 2024-05-23 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('it_app', '0003_homeimgmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='homemenosarimodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='0', max_length=100, null=True)),
                ('image', models.ImageField(null=True, upload_to='menosari/home')),
            ],
        ),
        migrations.AlterField(
            model_name='homeimgmodel',
            name='image',
            field=models.ImageField(null=True, upload_to='image/home'),
        ),
        migrations.AlterField(
            model_name='homeimgmodel',
            name='name',
            field=models.CharField(default='0', max_length=100, null=True),
        ),
    ]
