# Generated by Django 4.1.2 on 2022-11-25 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "consultations",
            "0004_alter_consultation_options_alter_reservation_options_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="reservation",
            name="was_absent",
            field=models.BooleanField(default=False, verbose_name="was absent"),
        ),
    ]
