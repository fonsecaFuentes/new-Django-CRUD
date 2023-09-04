from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import CouplingForm
from django.contrib import messages
from pumpsData.models import Pumps
from motorData.models import Motor
from .models import Coupling


# Create your views here.
@login_required
def list_coupling(request):
    search_query = request.GET.get('search', '')
    coupling_list = Coupling.objects.all()

    if search_query:
        coupling_list = coupling_list.filter(
            Q(pump__tag__icontains=search_query) |
            Q(types__icontains=search_query) |
            Q(model__icontains=search_query) |
            Q(motor_side_measure__icontains=search_query) |
            Q(pump_side_sizer__icontains=search_query) |
            Q(motor_key_measure__icontains=search_query) |
            Q(pump_key_measure__icontains=search_query)
        )

    context = {'coupling_list': coupling_list}

    return render(request, 'coupling/list_coupling.html', context)


@login_required
def coupling(request, coupling_id):
    coupling = get_object_or_404(Coupling, pk=coupling_id)

    return render(request, 'coupling/coupling.html', {'coupling': coupling})


@login_required
def add_coupling(request, pump_id, motor_id):
    pump = get_object_or_404(Pumps, pk=pump_id)
    motor = get_object_or_404(Motor, pk=motor_id)

    if request.method == 'POST':
        coupling_form = CouplingForm(request.POST)
        if coupling_form.is_valid():
            coupling = coupling_form.save(commit=False)
            coupling.pump = pump
            coupling.motor = motor
            coupling.save()
            messages.success(
                request, '¡Los datos se han almacenado exitosamente!'
            )
            return redirect('pumps')
        else:
            messages.error(request, '¡Hubo un error al almacenar los datos!')
    else:
        coupling_form = CouplingForm()

    context = {'coupling_form': coupling_form, 'pump': pump, 'motor': motor}

    return render(request, 'coupling/add_coupling.html', context)


@login_required
def add_list_coupling(request):
    if request.method == 'POST':
        coupling_form = CouplingForm(request.POST)
        if coupling_form.is_valid():
            coupling = coupling_form.save(commit=False)

            selected_pump = request.POST.get('pump', None)
            selected_motor = Motor.objects.get(pump=selected_pump)
            print(selected_pump)
            print(selected_motor.motor_id)
            # selected_pump2 = Pumps.objects.get(pk=selected_pump)
            # print('selected_pump2:', selected_pump2)
            # print('selected_pump:', selected_pump)
            # print('selected_pump:', selected_pump)

            if selected_pump:
                print('1')
                selected_pump = Pumps.objects.get(pk=selected_pump)
                coupling.pump = selected_pump

                coupling.motor = selected_motor
                coupling.save()

                messages.success(
                    request, '¡Los datos se han almacenado exitosamente!'
                )
                return redirect('list_coupling')
            else:
                print('2')
                messages.error(request, '¡Debe seleccionar una bomba!')
        else:
            messages.error(request, '¡Hubo un error al almacenar los datos!')
    else:
        coupling_form = CouplingForm()

    pumps_with_motor_and_coupling = Pumps.objects.filter(
        motor__isnull=False, coupling__isnull=True
    )

    context = {
        'available_pumps': pumps_with_motor_and_coupling
    }

    return render(request, 'coupling/add_list_coupling.html', context)


@login_required
def update_coupling(request, coupling_id):
    coupling = get_object_or_404(Coupling, pk=coupling_id)
    coupling_list_param = request.POST.get('coupling_list_param')
    coupling_form = CouplingForm(instance=coupling)

    if request.method == 'POST':
        coupling_form = CouplingForm(request.POST, instance=coupling)

        if coupling_form.is_valid():
            coupling_form.save()
            messages.success(
                request, '¡Los datos se han almacenado exitosamente!'
            )
            if coupling_list_param == 'true':
                return redirect('list_coupling')
            else:
                return redirect('coupling', coupling_id=coupling_id)
        else:
            messages.error(request, '¡Hubo un error al almacenar los datos!')
    else:
        coupling_form = CouplingForm(instance=coupling)

    context = {'coupling_form': coupling_form, 'coupling': coupling}

    return render(request, 'coupling/coupling.html', context)


@login_required
def delete_coupling(request, coupling_id):
    coupling = get_object_or_404(Coupling, pk=coupling_id)
    coupling_list_param = request.GET.get('coupling_list')

    if request.method == 'POST':
        if 'confirm_delete' in request.POST:
            coupling.delete()
            messages.success(
                request, '¡Los datos se han borrado exitosamente!'
            )
            if coupling_list_param == 'true':
                return redirect('list_coupling')
            else:
                return redirect('pumps')
        else:
            messages.error(
                request, 'La acción de eliminación no se ha confirmado.'
            )
            return redirect('coupling', coupling_id=coupling_id)

    context = {'coupling': coupling}
    return render(request, 'coupling/coupling_delete_conf.html', context)
