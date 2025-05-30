# Generated by Django 4.1.7 on 2025-04-27 21:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reserv_app', '0010_fpeseshktestmodel_bankpeyment_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='leav',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.JSONField(help_text='روزهای انتخابی به صورت آرایه')),
                ('times', models.JSONField(help_text='زمان\u200cهای انتخابی به صورت آرایه')),
                ('recurrence_type', models.CharField(choices=[('weekly', 'هفتگی'), ('monthly', 'ماهانه'), ('none', 'بدون تکرار')], default='none', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
