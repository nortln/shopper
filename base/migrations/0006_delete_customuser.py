# Generated by Django 4.2.3 on 2023-10-05 18:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0005_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="CustomUser",
        ),
    ]
