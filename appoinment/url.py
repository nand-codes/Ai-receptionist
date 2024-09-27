from django.urls import re_path, include
from appoinment import views

urlpatterns=[
    re_path('appoint/',views.appoinment),
    re_path('viewapp/',views.vapp),
    re_path('approve/(?P<idd>\w+)',views.approve),
    re_path('reject/(?P<idd>\w+)',views.reject),
    re_path('view_app_appoinment/', views.v_app_appoinment),

]