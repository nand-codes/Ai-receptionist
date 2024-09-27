from django.urls import re_path, include

from department import views

urlpatterns = [re_path('depart/',views.department),
    re_path('viewdept/',views.vdept),
    re_path('viewmgdept/',views.vmgdept),
    re_path('remove/(?P<idd>\w+)',views.remove),
     re_path('reject/(?P<idd>\w+)',views.reject),
    ]

