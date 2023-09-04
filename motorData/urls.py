"""
URL configuration for workplaceCRUD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import add_motor
from .views import motor
from .views import update_motor
from .views import delete_motor
from .views import list_motor
from .views import add_list_motor


urlpatterns = [
    path('motor/', list_motor, name='list_motor'),
    path('motor/add_list_motor/', add_list_motor, name='add_list_motor'),
    path('pumps/<int:pump_id>/add_motor/', add_motor, name='add_motor'),
    path('pumps/<int:motor_id>/motor/', motor, name='motor'),
    path(
        'pumps/<int:motor_id>/update_motor/', update_motor, name='update_motor'
    ),
    path(
        'pumps/<int:motor_id>/delete_motor/', delete_motor, name='delete_motor'
    ),
]
