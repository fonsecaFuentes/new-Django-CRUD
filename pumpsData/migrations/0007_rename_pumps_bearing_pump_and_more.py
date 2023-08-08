# Generated by Django 4.2.3 on 2023-08-03 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("pumpsData", "0006_alter_pumps_image"),
    ]

    operations = [
        migrations.RenameField(
            model_name="bearing",
            old_name="pumps",
            new_name="pump",
        ),
        migrations.RenameField(
            model_name="mechanicalseal",
            old_name="pumps",
            new_name="pump",
        ),
        migrations.CreateModel(
            name="Reten",
            fields=[
                ("seal_id", models.AutoField(primary_key=True, serialize=False)),
                ("front_seal", models.CharField(blank=True, max_length=100)),
                ("rear_seal", models.CharField(blank=True, max_length=100)),
                ("details", models.TextField(blank=True, null=True)),
                (
                    "pump",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pumpsData.pumps",
                    ),
                ),
            ],
        ),
    ]
