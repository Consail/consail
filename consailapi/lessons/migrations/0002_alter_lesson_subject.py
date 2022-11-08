# Generated by Django 4.1.2 on 2022-11-02 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("lessons", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="subject",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="lessons",
                to="lessons.subject",
                verbose_name="subject",
            ),
        ),
    ]