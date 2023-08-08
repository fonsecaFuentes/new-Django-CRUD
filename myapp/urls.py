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
from .views import home, sing_up, section
from .views import data, tasks, observations
from .views import exit, activate, password_change
from .views import password_reset_request
from .views import passwordResetConfirm
from .views import profile

urlpatterns = [
    path("", home, name='home'),
    path("singup/", sing_up, name='singup'),
    path('section/', section, name='section'),
    path("data/", data, name='data'),
    path("tasks/", tasks, name='tasks'),
    path("observations/", observations, name='observations'),
    path("logout/", exit, name='exit'),
    path("profile/", profile, name='profile'),
    path("accounts/password_change/", password_change, name='password_change'),
    path('activate/<uidb64>/<token>', activate, name='activate'),
    path(
        "accounts/password_reset/",
        password_reset_request,
        name="password_reset"
    ),
    path(
        'accounts/reset/<uidb64>/<token>/',
        passwordResetConfirm,
        name='password_reset_confirm'
    ),
]
