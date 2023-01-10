# Generated by Django 4.1.2 on 2022-12-20 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0004_student_major"),
        ("teachers", "0002_alter_teacher_managers"),
        ("chats", "0001_initial"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="thread",
            unique_together={("teacher", "student")},
        ),
    ]