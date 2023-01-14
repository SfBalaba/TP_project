# Generated by Django 4.1.4 on 2023-01-14 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Demand",
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
                ("title", models.CharField(max_length=50)),
                ("html_file", models.TextField(default="")),
                ("file", models.ImageField(upload_to="statistics\\images")),
                ("html_excel", models.TextField(default="")),
                ("excel", models.FileField(upload_to="statistics\\excel")),
            ],
        ),
        migrations.CreateModel(
            name="Geography",
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
                ("title", models.CharField(max_length=50)),
                ("html_file", models.TextField(default="")),
                (
                    "file",
                    models.ImageField(default=None, upload_to="statistics\\images"),
                ),
                ("html_excel", models.TextField(default="")),
                (
                    "excel",
                    models.FileField(default=None, upload_to="statistics\\excel"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Home",
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
                ("title", models.CharField(max_length=50)),
                ("file", models.ImageField(upload_to="home/images")),
                ("html", models.TextField(default="")),
            ],
        ),
        migrations.CreateModel(
            name="Skills",
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
                ("title", models.CharField(max_length=50)),
                ("html_file", models.TextField(default="")),
                ("file", models.ImageField(upload_to="statistics\\images")),
                ("html_excel", models.TextField(default="")),
                ("excel", models.FileField(upload_to="statistics\\excel")),
            ],
        ),
    ]
