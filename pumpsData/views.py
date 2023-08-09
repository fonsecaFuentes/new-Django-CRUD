from django.shortcuts import render, redirect
from django.db.models import Q
from .forms import PumpsForm
from .models import Pumps
from .models import Bearing
from .models import MechanicalSeal
from .models import Reten
from motorData.models import Motor
from couplingData.models import Coupling


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
    search_query = request.GET.get('search', '')
    pumps_list = Pumps.objects.all()
    bearing_list = Bearing.objects.all()
    mechanicalseal = MechanicalSeal.objects.all()
    reten_list = Reten.objects.all()
    motor_list = Motor.objects.all()
    coupling_list = Coupling.objects.all()

    if search_query:
        pumps_list = pumps_list.filter(
            Q(tag__icontains=search_query) |
            Q(types__icontains=search_query) |
            Q(brand__icontains=search_query) |
            Q(model__icontains=search_query)
        )

    for pump in pumps_list:
        pump.has_mechanicalseal = pump.mechanicalseal_set.exists()
        pump.has_reten = pump.reten_set.exists()
        pump.has_bearing = pump.bearing_set.exists()
        pump.has_motor = Motor.objects.filter(pump=pump).exists()
        pump.has_coupling = Motor.objects.filter(pump=pump).exists()

    context = {
        'pumps_list': pumps_list,
        'bearing_list': bearing_list,
        'mechanicalseal': mechanicalseal,
        'reten_list': reten_list,
        'motor_list': motor_list,
        'coupling_id_list': coupling_list,
        'search_query': search_query
    }

    return render(request, 'pumps/pumps.html', context)
