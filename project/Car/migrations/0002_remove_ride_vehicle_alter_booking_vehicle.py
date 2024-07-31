# Generated by Django 5.0.6 on 2024-07-04 05:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Car', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ride',
            name='vehicle',
        ),
        migrations.AlterField(
            model_name='booking',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Car.vehicle'),
        ),
    ]