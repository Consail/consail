# Generated by Django 4.0 on 2022-10-15 20:53

import consailapi.users.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='teacher',
            managers=[
                ('objects', consailapi.users.models.UserManager()),
            ],
        ),
    ]
