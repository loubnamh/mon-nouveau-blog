# Generated by Django 2.2.28 on 2024-11-16 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20241115_1700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attraction',
            name='capacite',
        ),
        migrations.AddField(
            model_name='attraction',
            name='capacitemaximal',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='attraction',
            name='nbractuelle',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
