# Generated by Django 4.2.6 on 2023-11-13 10:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0026_blog"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blog",
            name="summary",
        ),
    ]
