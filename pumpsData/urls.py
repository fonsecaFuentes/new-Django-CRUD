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


urlpatterns = [
    path('pumps/add_pump/', add_pump, name='add_pump'),
    path('pumps/', pumps, name='pumps'),
    path(
        'pumps/add_bearing/<int:pump_id>',
        add_bearing,
        name='add_bearing'
    ),
    path(
        'pumps/add_mechanicalseal/<int:pump_id>',
        add_mechanicalseal,
        name='add_mechanicalseal'
    ),
    path('pumps/add_reten/<int:pump_id>', add_reten, name='add_reten'),
]
