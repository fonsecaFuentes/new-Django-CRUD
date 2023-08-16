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

# Mannejo de bombas
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
def update_pump(request, pump_id):
    pump = get_object_or_404(Pumps, pk=pump_id)
    pump_form = PumpsForm(instance=pump)

    if request.method == 'POST':
        pump_form = PumpsForm(request.POST, instance=pump)
        if pump_form.is_valid():
            pump_form.save()
            messages.success(
                request, '¡Los datos se han almacenado exitosamente!'
            )
            return redirect('pumps')
        else:
            messages.error(request, '¡Hubo un error al almacenar los datos!')
    else:
        pump_form = PumpsForm(instance=pump)

    context = {'pump_form': pump_form, 'pump': pump}

    return render(request, 'pumps/pumps.html', context)


@login_required
def delete_pump(request, pump_id):
    pump = get_object_or_404(Pumps, pk=pump_id)

    if request.method == 'POST':
        if 'confirm_delete' in request.POST:
            pump.delete()
            messages.success(
                request, '¡Los datos se han borrado exitosamente!'
            )
            return redirect('pumps')
        else:
            messages.error(
                request, 'La acción de eliminación no se ha confirmado.'
            )
            return redirect('pumps')

    context = {'pump': pump}
    return render(request, 'pumps/pumps_delete_conf.html', context)


# Mannejo de rodamientos
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

    context = {'bearing_form': bearing_form, 'pump': pump}

    return render(request, 'pumps/add_bearing.html', context)


@login_required
def update_bearing(request, bearing_id):
    bearing = get_object_or_404(Bearing, pk=bearing_id)
    bearing_form = BearingForm(instance=bearing)

    if request.method == 'POST':
        bearing_form = BearingForm(request.POST, instance=bearing)
        if bearing_form.is_valid():
            bearing_form.save()
            messages.success(
                request, '¡Los datos se han almacenado exitosamente!'
            )
            return redirect('pumps')
        else:
            messages.error(request, '¡Hubo un error al almacenar los datos!')
    else:
        bearing_form = BearingForm(instance=bearing)

    context = {'bearing_form': bearing_form, 'bearing': bearing}

    return render(request, 'pumps/pumps.html', context)


@login_required
def delete_bearing(request, bearing_id):
    bearing = get_object_or_404(Bearing, pk=bearing_id)

    if request.method == 'POST':
        if 'confirm_delete' in request.POST:
            bearing.delete()
            messages.success(
                request, '¡Los datos se han borrado exitosamente!'
            )
            return redirect('pumps')
        else:
            messages.error(
                request, 'La acción de eliminación no se ha confirmado.'
            )
            return redirect('pumps')

    context = {'bearing': bearing}
    return render(request, 'pumps/bearing_delete_conf.html', context)


# Manejo de sellos
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

    context = {'mechanicalseal_form': mechanicalseal_form, 'pump': pump}

    return render(request, 'pumps/add_mechanicalseal.html', context)


@login_required
def update_mechanicalseal(request, seal_id):
    mechanicalseal = get_object_or_404(MechanicalSeal, pk=seal_id)
    mechanicalseal_form = MechanicalSealForm(instance=mechanicalseal)

    if request.method == 'POST':
        mechanicalseal_form = MechanicalSealForm(
            request.POST, instance=mechanicalseal
        )
        if mechanicalseal_form.is_valid():
            mechanicalseal_form.save()
            messages.success(
                request, '¡Los datos se han almacenado exitosamente!'
            )
            return redirect('pumps')
        else:
            messages.error(request, '¡Hubo un error al almacenar los datos!')
    else:
        mechanicalseal_form = MechanicalSealForm(instance=mechanicalseal)

    context = {
        'mechanicalseal_form': mechanicalseal_form,
        'mechanicalseal': mechanicalseal
    }

    return render(request, 'pumps/pumps.html', context)


@login_required
def delete_mechanicalseal(request, seal_id):
    mechanicalseal = get_object_or_404(MechanicalSeal, pk=seal_id)

    if request.method == 'POST':
        if 'confirm_delete' in request.POST:
            mechanicalseal.delete()
            messages.success(
                request, '¡Los datos se han borrado exitosamente!'
            )
            return redirect('pumps')
        else:
            messages.error(
                request, 'La acción de eliminación no se ha confirmado.'
            )
            return redirect('pumps')

    context = {'mechanicalseal': mechanicalseal}
    return render(request, 'pumps/mechanicalseal_delete_conf.html', context)


# Manejo de retenes
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

    context = {'reten_form': reten_form, 'pump': pump}

    return render(request, 'pumps/add_reten.html', context)


@login_required
def update_reten(request, seal_id):
    reten = get_object_or_404(Reten, pk=seal_id)
    reten_form = RetenForm(instance=reten)

    if request.method == 'POST':
        reten_form = RetenForm(
            request.POST, instance=reten
        )
        if reten_form.is_valid():
            reten_form.save()
            messages.success(
                request, '¡Los datos se han almacenado exitosamente!'
            )
            return redirect('pumps')
        else:
            messages.error(request, '¡Hubo un error al almacenar los datos!')
    else:
        reten_form = RetenForm(instance=reten)

    context = {
        'reten_form': reten_form,
        'reten': reten
    }

    return render(request, 'pumps/pumps.html', context)


@login_required
def delete_reten(request, seal_id):
    reten = get_object_or_404(Reten, pk=seal_id)

    if request.method == 'POST':
        if 'confirm_delete' in request.POST:
            reten.delete()
            messages.success(
                request, '¡Los datos se han borrado exitosamente!'
            )
            return redirect('pumps')
        else:
            messages.error(
                request, 'La acción de eliminación no se ha confirmado.'
            )
            return redirect('pumps')

    context = {'reten': reten}
    return render(request, 'pumps/reten_delete_conf.html', context)
