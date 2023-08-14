from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from .forms import PumpsForm
from .forms import BearingForm
from .forms import MechanicalSealForm
from .forms import RetenForm
from .models import Pumps
from .models import Bearing
from .models import MechanicalSeal
from .models import Reten
from motorData.models import Motor
from couplingData.models import Coupling


# Create your views here.
@login_required
def add_pump(request):
    if request.method == 'POST':
        pump_form = PumpsForm(request.POST)
        if pump_form.is_valid():
            pump_form.save()
            messages.success(
                request, '¡Los datos se han almacenado exitosamente!'
            )
            return redirect('pumps')
        else:
            messages.error(request, '¡Hubo un error al almacenar los datos!')
    else:
        pump_form = PumpsForm()

    return render(request, 'pumps/add_pumps.html', {
        'pump_form': pump_form
    })


@login_required
def add_bearing(request, pump_id):
    pump = get_object_or_404(Pumps, pk=pump_id)
    if request.method == 'POST':
        bearing_form = BearingForm(request.POST)
        if bearing_form.is_valid():
            bearing = bearing_form.save(commit=False)
            bearing.pump = pump
            bearing.save()
            messages.success(
                request, '¡Los datos se han almacenado exitosamente!'
            )
            return redirect('pumps')
        else:
            messages.error(request, '¡Hubo un error al almacenar los datos!')
    else:
        bearing_form = BearingForm()

    return render(request, 'pumps/add_bearing.html', {
        'bearing_form': bearing_form
    })


@login_required
def add_mechanicalseal(request, pump_id):
    pump = get_object_or_404(Pumps, pk=pump_id)
    if request.method == 'POST':
        mechanicalseal_form = MechanicalSealForm(request.POST)
        if mechanicalseal_form.is_valid():
            mechanicalseal = mechanicalseal_form.save(commit=False)
            mechanicalseal.pump = pump
            mechanicalseal.save()
            messages.success(
                request, '¡Los datos se han almacenado exitosamente!'
            )
            return redirect('pumps')
        else:
            messages.error(request, '¡Hubo un error al almacenar los datos!')
    else:
        mechanicalseal_form = MechanicalSealForm()

    return render(request, 'pumps/add_mechanicalseal.html', {
        'mechanicalseal_form': mechanicalseal_form
    })


@login_required
def add_reten(request, pump_id):
    pump = get_object_or_404(Pumps, pk=pump_id)
    if request.method == 'POST':
        reten_form = RetenForm(request.POST)
        if reten_form.is_valid():
            reten = reten_form.save(commit=False)
            reten.pump = pump
            reten.save()
            messages.success(
                request, '¡Los datos se han almacenado exitosamente!'
            )
            return redirect('pumps')
        else:
            messages.error(request, '¡Hubo un error al almacenar los datos!')
    else:
        reten_form = RetenForm()

    return render(request, 'pumps/add_reten.html', {
        'reten_form': reten_form
    })


@login_required
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
        pump.has_coupling = Coupling.objects.filter(pump=pump).exists()

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
