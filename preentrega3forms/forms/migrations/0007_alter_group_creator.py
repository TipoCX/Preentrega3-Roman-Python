# Generated by Django 5.0.4 on 2024-04-23 17:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0006_user_group_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.user'),
        ),
    ]
