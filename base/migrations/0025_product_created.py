# Generated by Django 4.2.6 on 2023-11-09 08:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0024_verification"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="created",
            field=models.DateTimeField(auto_created=True, auto_now_add=True, null=True),
        ),
    ]
