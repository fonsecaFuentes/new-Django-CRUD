from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import MotorForm
from django.contrib import messages
from pumpsData.models import Pumps
from .models import Motor


# Create your views here.
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
def motor(request, motor_id):
    motor = get_object_or_404(Motor, pk=motor_id)

    return render(request, 'motor/motor.html', {'motor': motor})


@login_required
def update_motor(request, motor_id):
    print('hola')
    motor = get_object_or_404(Motor, pk=motor_id)
    motor_form = MotorForm(instance=motor)
    if request.method == 'POST':
        print('hola')
        motor_form = MotorForm(request.POST, instance=motor)
        if motor_form.is_valid():
            print('hola')
            motor_form.save()
            messages.success(
                request, '¡Los datos se han almacenado exitosamente!'
            )
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

    if request.method == 'POST':
        if 'confirm_delete' in request.POST:
            motor.delete()
            messages.success(
                request, '¡Los datos se han borrado exitosamente!'
            )
            return redirect('pumps')
        else:
            messages.error(
                request, 'La acción de eliminación no se ha confirmado.'
            )
            return redirect('motor', motor_id=motor_id)

    context = {'motor': motor}
    return render(request, 'motor/motor_delete_conf.html', context)
