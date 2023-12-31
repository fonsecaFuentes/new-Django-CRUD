from django.db import models
from pumpsData.models import Pumps


# Create your models here.
class Motor(models.Model):
    motor_id = models.AutoField(primary_key=True)
    pump = models.ForeignKey(
        Pumps, on_delete=models.CASCADE
    )
    brand = models.CharField(max_length=100, blank=True)
    model = models.CharField(
        max_length=100, blank=True, verbose_name='Carcasa'
    )
    hp = models.CharField(max_length=100, blank=True)
    rpm = models.CharField(max_length=100, blank=True)
    front_bearing = models.CharField(max_length=100, blank=True)
    rear_bearing = models.CharField(max_length=100, blank=True)
    anti_explosive = models.BooleanField(
        default=False, blank=True, verbose_name='Antiexplosivo'
    )
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(
        default='img_motor.png',
        upload_to='img_motor/',
        verbose_name='Imagen de motor',
        blank=True
    )

    def __str__(self):
        return f"Motor - {self.model} - Bomba {self.pump.tag}"
