# Generated by Django 4.2.6 on 2023-11-04 22:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0021_addressbook_state_alter_addressbook_address_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="addressbook",
            name="country",
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name="addressbook",
            name="state",
            field=models.CharField(default=None, max_length=30),
        ),
    ]
