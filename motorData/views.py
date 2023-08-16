from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import MotorForm
from django.contrib import messages
from pumpsData.models import Pumps
from .models import Motor


# Create your views here.
@login_required
def list_motor(request):
    search_query = request.GET.get('search', '')
    motor_list = Motor.objects.all()
    pumps_list = Pumps.objects.all()

    if search_query:
        motor_list = motor_list.filter(
            Q(tag__icontains=search_query) |
            Q(types__icontains=search_query) |
            Q(brand__icontains=search_query) |
            Q(model__icontains=search_query)
        )

    context = {
        'pumps_list': pumps_list,
        'motor_list': motor_list,
    }

    return render(request, 'motor/list_motor.html', context)


@login_required
def motor(request, motor_id):
    motor = get_object_or_404(Motor, pk=motor_id)

    return render(request, 'motor/motor.html', {'motor': motor})


@login_required
def add_motor(request, pump_id):
    pump = get_object_or_404(Pumps, pk=pump_id)
    if request.method == 'POST':
        motor_form = MotorForm(request.POST)
        if motor_form.is_valid():
            motor = motor_form.save(commit=False)
            motor.pump = pump
            motor.save()
            messages.success(
                request, '¡Los datos se han almacenado exitosamente!'
            )
            return redirect('pumps')
        else:
            messages.error(request, '¡Hubo un error al almacenar los datos!')
    else:
        motor_form = MotorForm()

    context = {'motor_form': motor_form, 'pump': pump}

    return render(request, 'motor/add_motor.html', context)


@login_required
def update_motor(request, motor_id):
    motor = get_object_or_404(Motor, pk=motor_id)
    motor_list_param = request.POST.get('motor_list_param')
    motor_form = MotorForm(instance=motor)

    if request.method == 'POST':
        motor_form = MotorForm(request.POST, instance=motor)

        if motor_form.is_valid():
            motor_form.save()
            messages.success(
                request, '¡Los datos se han almacenado exitosamente!'
            )
            if motor_list_param == 'true':
                return redirect('list_motor')
            else:
                return redirect('motor', motor_id=motor_id)
        else:
            messages.error(request, '¡Hubo un error al almacenar los datos!')
    else:
        motor_form = MotorForm(instance=motor)

    context = {'motor_form': motor_form, 'motor': motor}

    return render(request, 'motor/motor.html', context)


@login_required
def delete_motor(request, motor_id):
    motor = get_object_or_404(Motor, pk=motor_id)
    motor_list_param = request.GET.get('motor_list')

    if request.method == 'POST':
        if 'confirm_delete' in request.POST:
            motor.delete()
            messages.success(
                request, '¡Los datos se han borrado exitosamente!'
            )
            if motor_list_param == 'true':
                return redirect('list_motor')
            else:
                return redirect('pumps')
        else:
            messages.error(
                request, 'La acción de eliminación no se ha confirmado.'
            )
            return redirect('motor', motor_id=motor_id)

    context = {'motor': motor}
    return render(request, 'motor/motor_delete_conf.html', context)
