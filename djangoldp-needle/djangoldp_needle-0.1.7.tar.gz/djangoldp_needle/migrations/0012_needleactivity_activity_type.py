# Generated by Django 2.2.28 on 2022-12-12 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoldp_needle', '0011_auto_20221125_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='needleactivity',
            name='activity_type',
            field=models.TextField(default='', max_length=255),
        ),
    ]
