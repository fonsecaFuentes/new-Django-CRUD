from django.shortcuts import render, redirect, get_object_or_404
from .forms import MotorForm
from django.contrib import messages
from pumpsData.models import Pumps


# Create your views here.
def add_motor(request, pump_id):
    pump = get_object_or_404(Pumps, pk=pump_id)
    if request.method == 'POST':
        motor_form = MotorForm(request.POST)
        if motor_form.is_valid():
            motor = motor_form.save(commit=False)
            motor.pump = pump
            motor.save()
            messages.success(
                request, '¡Los datos del motor se han almacenado exitosamente!'
            )
            return redirect('pumps')
        else:
            messages.error(request, '¡Hubo un error al almacenar los datos!')
    else:
        motor_form = MotorForm

    return render(request, 'pumps/add_motor.html', {'motor_form': motor_form})
