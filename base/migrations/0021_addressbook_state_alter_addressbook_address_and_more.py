# Generated by Django 4.2.6 on 2023-11-04 21:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0020_remove_addressbook_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="addressbook",
            name="state",
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name="addressbook",
            name="address",
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name="addressbook",
            name="phone_number",
            field=models.CharField(default=None, max_length=20),
        ),
    ]
