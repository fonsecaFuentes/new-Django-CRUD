from django.shortcuts import render
from .models import Motor


# Create your views here.
def pumps_request(request):
    motor_id_list = Motor.objects.all()

    for motor_id in motor_id_list:
        motor_id.has_motor = Motor.objects.filter(
            motor_id=motor_id
        ).exists()

    return render(
        request, 'pumps/pumps.html', {'motor_id_list': motor_id_list}
    )
