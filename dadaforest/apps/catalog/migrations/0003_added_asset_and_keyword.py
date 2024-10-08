# Generated by Django 5.1.1 on 2024-10-08 17:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0002_added_catalog_domain"),
    ]

    operations = [
        migrations.CreateModel(
            name="Asset",
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
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                (
                    "metadata_url",
                    models.CharField(
                        blank=True,
                        help_text="The url used to access/retrieve the metadata.",
                        max_length=1500,
                        null=True,
                        unique=True,
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True,
                        help_text="Name describing the asset",
                        max_length=150,
                        null=True,
                        unique=True,
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        blank=True,
                        help_text="The description of the metadata document.",
                        max_length=3000,
                        null=True,
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        blank=True,
                        help_text="Date metadata was last modified.",
                        null=True,
                    ),
                ),
                (
                    "domain",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="catalog.domain",
                    ),
                ),
            ],
            options={
                "db_table": "assets",
            },
        ),
        migrations.CreateModel(
            name="Keyword",
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
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                ("word", models.CharField(max_length=250)),
                ("assets", models.ManyToManyField(to="catalog.asset")),
            ],
            options={
                "db_table": "keywords",
            },
        ),
    ]
