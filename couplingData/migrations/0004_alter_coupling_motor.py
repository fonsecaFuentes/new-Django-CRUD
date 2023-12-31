# Generated by Django 4.2.3 on 2023-08-13 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("motorData", "0005_motor_anti_explosive_alter_motor_model"),
        ("couplingData", "0003_coupling_model_coupling_types"),
    ]

    operations = [
        migrations.AlterField(
            model_name="coupling",
            name="motor",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="motorData.motor",
            ),
        ),
    ]
