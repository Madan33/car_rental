# Generated by Django 5.0.6 on 2024-07-11 05:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Car', '0004_rename_user_notification_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='name',
        ),
        migrations.AddField(
            model_name='notification',
            name='booking',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Car.booking'),
        ),
    ]
