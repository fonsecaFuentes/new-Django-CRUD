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
from .views import add_coupling
from .views import coupling
from .views import update_coupling
from .views import delete_coupling
from .views import list_coupling
from .views import add_list_coupling


urlpatterns = [
    path('coupling/', list_coupling, name='list_coupling'),
    path(
        'coupling/add_list_coupling/',
        add_list_coupling,
        name='add_list_coupling'
    ),
    path(
        'pumps/add_coupling/<int:pump_id>/<int:motor_id>',
        add_coupling,
        name='add_coupling'
    ),
    path('pumps/<int:coupling_id>/coupling/', coupling, name='coupling'),
    path(
        'pumps/<int:coupling_id>/update_coupling/',
        update_coupling,
        name='update_coupling'
    ),
    path(
        'pumps/<int:coupling_id>/delete_coupling/',
        delete_coupling,
        name='delete_coupling'
    ),
]
