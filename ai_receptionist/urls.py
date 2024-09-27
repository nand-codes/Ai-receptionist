"""ai_receptionist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import re_path, include

from temp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('appoinment/',include('appoinment.url')),
    re_path('complaint/',include('complaint.url')),
    re_path('department/',include('department.url')),
    re_path('doctor/',include('doctor.url')),
    re_path('login/',include('login.url')),
    re_path('medical_record/',include('medical_record.url')),
    re_path('patient/',include('patient.url')),
    re_path('service/',include('service.url')),
    re_path('user/',include('user.url')),
    re_path('temp/',include('temp.url')),
    re_path('$',views.home)

]
