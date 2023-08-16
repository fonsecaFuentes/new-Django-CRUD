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
from .views import add_pump
from .views import pumps
from .views import add_bearing
from .views import add_mechanicalseal
from .views import add_reten
from .views import update_pump
from .views import delete_pump
from .views import update_bearing
from .views import delete_bearing
from .views import update_mechanicalseal
from .views import delete_mechanicalseal
from .views import update_reten
from .views import delete_reten


urlpatterns = [
    # Listar Bombas
    path('pumps/', pumps, name='pumps'),
    # Mannejo de bombas
    path('pumps/add_pump/', add_pump, name='add_pump'),
    path('pumps/update_pump/<int:pump_id>', update_pump, name='update_pump'),
    path(
        'pumps/<int:pump_id>/delete_pump/',
        delete_pump,
        name='delete_pump'
    ),
    # Mannejo de rodamientos
    path(
        'pumps/add_bearing/<int:pump_id>',
        add_bearing,
        name='add_bearing'
    ),
    path(
        'pumps/update_bearing/<int:bearing_id>',
        update_bearing,
        name='update_bearing'
    ),
    path(
        'pumps/<int:bearing_id>/delete_bearing/',
        delete_bearing,
        name='delete_bearing'
    ),
    # Manejo de sellos
    path(
        'pumps/add_mechanicalseal/<int:pump_id>',
        add_mechanicalseal,
        name='add_mechanicalseal'
    ),
    path(
        'pumps/update_mechanicalseal/<int:seal_id>',
        update_mechanicalseal,
        name='update_mechanicalseal'
    ),
    path(
        'pumps/<int:seal_id>/delete_mechanicalseal/',
        delete_mechanicalseal,
        name='delete_mechanicalseal'
    ),
    # Manejo de rodamientos
    path('pumps/add_reten/<int:pump_id>', add_reten, name='add_reten'),
    path(
        'pumps/update_reten/<int:seal_id>',
        update_reten,
        name='update_reten'
    ),
    path(
        'pumps/<int:seal_id>/delete_reten/',
        delete_reten,
        name='delete_reten'
    )
]
