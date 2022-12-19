# Generated by Django 4.0.4 on 2022-07-10 23:18

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("obpages", "0002_feedbacknote"),
    ]

    operations = [
        migrations.AddField(
            model_name="usersequence",
            name="create_timestamp",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                help_text="When the sequence was created.",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="usersequence",
            name="update_timestamp",
            field=models.DateTimeField(
                auto_now=True,
                help_text="When the sequence was last updated.",
                verbose_name="update date",
            ),
        ),
    ]
