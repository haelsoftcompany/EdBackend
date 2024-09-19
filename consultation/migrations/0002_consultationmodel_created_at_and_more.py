# Generated by Django 5.1 on 2024-09-19 11:58

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultationmodel',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='consultationmodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
