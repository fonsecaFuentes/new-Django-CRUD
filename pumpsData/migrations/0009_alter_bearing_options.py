# Generated by Django 4.2.3 on 2023-08-04 00:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "pumpsData",
            "0008_alter_bearing_options_alter_mechanicalseal_options_and_more",
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="bearing",
            options={
                "ordering": ["bearing_id"],
                "verbose_name": "Rodamiento",
                "verbose_name_plural": "Rodamientos",
            },
        ),
    ]
