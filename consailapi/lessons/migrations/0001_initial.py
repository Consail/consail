# Generated by Django 4.1.2 on 2022-10-29 16:40

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("teachers", "0002_alter_teacher_managers"),
        ("school", "0002_alter_major_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Subject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        db_index=True, default=uuid.uuid4, editable=False, unique=True
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True, db_index=True)),
                ("name", models.CharField(max_length=200, verbose_name="name")),
                (
                    "major",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subjects",
                        to="school.major",
                        verbose_name="major",
                    ),
                ),
            ],
            options={
                "verbose_name": "Subject",
                "verbose_name_plural": "Subjects",
            },
        ),
        migrations.CreateModel(
            name="Lesson",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        db_index=True, default=uuid.uuid4, editable=False, unique=True
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True, db_index=True)),
                (
                    "day",
                    models.CharField(
                        choices=[
                            ("MONDAY", "Monday"),
                            ("TUESDAY", "Tuesday"),
                            ("WEDNESDAY", "Wednesday"),
                            ("THURSDAY", "Thursday"),
                            ("FRIDAY", "Friday"),
                            ("SATURDAY", "Saturday"),
                            ("SUNDAY", "Sunday"),
                        ],
                        max_length=20,
                        verbose_name="day",
                    ),
                ),
                ("start_time", models.TimeField(verbose_name="start time")),
                ("end_time", models.TimeField(verbose_name="end time")),
                ("room", models.CharField(max_length=100, verbose_name="room")),
                (
                    "subject",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="lessons",
                        to="lessons.subject",
                        verbose_name="subject",
                    ),
                ),
                (
                    "teacher",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="lessons",
                        to="teachers.teacher",
                        verbose_name="teacher",
                    ),
                ),
            ],
            options={
                "verbose_name": "Lesson",
                "verbose_name_plural": "Lessons",
            },
        ),
    ]
