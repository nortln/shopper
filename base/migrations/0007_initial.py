# Generated by Django 4.2.3 on 2023-10-05 20:53

from django.conf import settings
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("base", "0006_delete_customuser"),
    ]

    operations = [
        migrations.CreateModel(
            name="Blog",
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
                ("created", models.DateField(auto_created=True, auto_now_add=True)),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                (
                    "image",
                    models.ImageField(
                        storage=django.core.files.storage.FileSystemStorage("static"),
                        upload_to="img/blog",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Brand",
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
                ("brand", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Catalog",
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
                ("title", models.CharField(max_length=30)),
                (
                    "image",
                    models.ImageField(
                        storage=django.core.files.storage.FileSystemStorage("static"),
                        upload_to="img/catalog",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CustomerCare",
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
                ("available", models.CharField(max_length=255)),
                ("phone", models.CharField(max_length=255)),
                ("email", models.CharField(max_length=255)),
                ("social_1", models.CharField(blank=True, max_length=255, null=True)),
                ("social_2", models.CharField(blank=True, max_length=255, null=True)),
                ("social_3", models.CharField(blank=True, max_length=255, null=True)),
                ("social_4", models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Image",
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
                    "image",
                    models.ImageField(
                        storage=django.core.files.storage.FileSystemStorage("static"),
                        upload_to="img/products",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("price", models.IntegerField()),
                ("color", models.CharField(max_length=20)),
                (
                    "brand",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="base.brand"
                    ),
                ),
                (
                    "cataglog",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="base.catalog"
                    ),
                ),
                ("images", models.ManyToManyField(to="base.image")),
            ],
        ),
        migrations.CreateModel(
            name="Review",
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
                ("date", models.DateField(auto_created=True, auto_now_add=True)),
                ("title", models.CharField(max_length=50)),
                ("review", models.TextField(max_length=500)),
                ("rating", models.IntegerField()),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="base.product"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="image",
            name="products",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="base.product"
            ),
        ),
        migrations.CreateModel(
            name="AddressBook",
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
                ("phone_number", models.CharField(max_length=20)),
                ("address", models.TextField()),
                (
                    "image",
                    models.ImageField(
                        storage=django.core.files.storage.FileSystemStorage("static"),
                        upload_to="img/users",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
