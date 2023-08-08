from django.db import models


# Create your models here.
class Pumps(models.Model):
    pump_id = models.AutoField(primary_key=True)
    types = models.CharField(max_length=100, blank=True)
    brand = models.CharField(max_length=100, blank=True)
    model = models.CharField(max_length=100, blank=True)
    tag = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(
        default='pump_1.png',
        upload_to='img_pumps/',
        verbose_name='Imagen de bomba',
        blank=True
    )

    class Meta:
        verbose_name = 'bomba'
        verbose_name_plural = 'bombas'
        ordering = ['tag']

    def __str__(self):
        return f"Bomba - {self.tag} - {self.types} - {self.model}"


class MechanicalSeal(models.Model):
    seal_id = models.AutoField(primary_key=True)
    pump = models.ForeignKey(
        Pumps, on_delete=models.CASCADE
    )
    brand = models.CharField(max_length=100, blank=True)
    types = models.CharField(max_length=100, blank=True)
    extention = models.CharField(max_length=100, blank=True)  # medida
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Sello'
        verbose_name_plural = 'Sellos'
        ordering = ['seal_id']

    def __str__(self):
        return f"Sello - {self.extention} en {self.pump.tag}"


class Bearing(models.Model):
    bearing_id = models.AutoField(primary_key=True)
    pump = models.ForeignKey(
        Pumps, on_delete=models.CASCADE
    )
    types = models.CharField(max_length=100, blank=True)
    amount = models.PositiveIntegerField(null=True, blank=True)
    front_bearing = models.CharField(max_length=100, blank=True)
    rear_bearing = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Rodamiento'
        verbose_name_plural = 'Rodamientos'
        ordering = ['bearing_id']

    def __str__(self):
        return f"Rodamientos - Delantero - {self.front_bearing}\
             - Trasero - {self.rear_bearing} Bomba {self.pump.tag}"


class Reten(models.Model):
    seal_id = models.AutoField(primary_key=True)
    pump = models.ForeignKey(Pumps, on_delete=models.CASCADE)
    front_seal = models.CharField(max_length=100, blank=True)
    rear_seal = models.CharField(max_length=100, blank=True)
    details = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Reten'
        verbose_name_plural = 'Retenes'
        ordering = ['seal_id']

    def __str__(self):
        return f"Retenes {self.front_seal} - {self.rear_seal}\
             en {self.pump.tag}"
