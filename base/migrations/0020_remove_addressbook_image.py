# Generated by Django 4.2.6 on 2023-11-04 15:14

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0019_rename_cataglog_product_catalog"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="addressbook",
            name="image",
        ),
    ]