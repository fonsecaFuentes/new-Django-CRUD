from django.shortcuts import render, redirect
from .forms import PumpsForm, BearingForm
from .forms import MechanicalSealForm, RetenForm
from .models import Pumps


# Create your views here.
def add_pump(request):
    if request.method == 'POST':
        pump_form = PumpsForm(request.POST)
        if pump_form.is_valid():
            pump_form.save()
            return redirect('pumps')

    else:
        pump_form = PumpsForm()

    return render(request, 'pumps/add_pumps.html', {
        'pump_form': pump_form
    })


def pumps(request):
    pumps_list = Pumps.objects.all()

    for pump in pumps_list:
        pump.has_mechanical_seal = pump.mechanicalseal_set.exists()
        pump.has_reten = pump.reten_set.exists()
        pump.has_bearing = pump.bearing_set.exists()

    return render(request, 'pumps/pumps.html', {'pumps_list': pumps_list})


# def pumps_request(request):
#     pumps_list = Pumps.objects.all()

#     for pump in pumps_list:
#         pump.has_mechanical_seal = MechanicalSealForm.objects.filter(
#             pump=pump
#         ).exists()
#         pump.has_reten = RetenForm.objects.filter(pump=pump).exists()
#         pump.has_bearing = BearingForm.objects.filter(pump=pump).exists()

#         # Agrega puntos de depuración aquí
#         print(
#             f"Pump ID: {pump.id}, \
#                 has_bearing: {pump.has_bearing}, \
#                 has_mechanical_seal: {pump.has_mechanical_seal}, \
#                 has_reten: {pump.has_reten}"
#         )

#     return render(request, 'pumps/pumps.html', {'pumps_list': pumps_list})


def bearing(request):
    return render(request, 'pumps/bearing.html')
