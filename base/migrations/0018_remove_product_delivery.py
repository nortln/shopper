# Generated by Django 4.2.6 on 2023-10-21 09:22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0017_product_delivery"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="delivery",
        ),
    ]
