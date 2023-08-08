# Generated by Django 4.2.3 on 2023-08-03 07:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("motorData", "0003_remove_motor_front_serial_number_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="motor",
            name="image",
            field=models.ImageField(
                blank=True,
                default="img_motor.png",
                upload_to="img_motor/",
                verbose_name="Imagen de motor",
            ),
        ),
    ]
