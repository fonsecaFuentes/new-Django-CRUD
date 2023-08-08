from django.contrib import admin
from .models import Pumps, MechanicalSeal, Bearing, Reten

# Register your models here.
admin.site.register(Pumps)
admin.site.register(MechanicalSeal)
admin.site.register(Bearing)
admin.site.register(Reten)
