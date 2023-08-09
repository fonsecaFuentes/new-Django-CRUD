from django.db import models
from pumpsData.models import Pumps
from motorData.models import Motor


# Create your models here.
class Coupling(models.Model):
    coupling_id = models.AutoField(primary_key=True)
    pump = models.ForeignKey(
        Pumps, on_delete=models.CASCADE
    )
    motor = models.ForeignKey(
        Motor, on_delete=models.CASCADE
    )
    types = models.CharField(max_length=100, blank=True)
    model = models.CharField(max_length=100, blank=True)
    motor_side_measure = models.CharField(max_length=100, blank=True)
    pump_side_sizer = models.CharField(max_length=100, blank=True)
    motor_key_measure = models.CharField(max_length=100, blank=True)
    pump_key_measure = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Acolple - Motor {self.motor.model}\
             - Bomba {self.pump.tag}"
