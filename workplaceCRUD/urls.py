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
from django.contrib import admin
from django.urls import path
from django.urls import include
from myapp.views import password_change, password_reset_request
from myapp.views import passwordResetConfirm

urlpatterns = [
    path('', include('myapp.urls')),
    path("admin/", admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path("password_change/", password_change, name='password_change'),
    path("password_reset", password_reset_request, name="password_reset"),
    path(
        'reset/<uidb64>/<token>',
        passwordResetConfirm,
        name='password_reset_confirm'
    ),
]
