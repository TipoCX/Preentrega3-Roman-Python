# Generated by Django 5.0.4 on 2024-04-16 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]
