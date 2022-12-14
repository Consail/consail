# Generated by Django 4.0 on 2022-10-15 20:53

import consailapi.users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_email'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', consailapi.users.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='deleted_at'),
        ),
    ]
