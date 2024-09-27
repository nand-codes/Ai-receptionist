from django.urls import path, re_path
from medical_record import views

urlpatterns = [
    path('medrec/', views.medical_record),
    path('viewm/', views.vmedre),
    re_path(r'^update/(?P<idd>\w+)$', views.update),
    path('viw_med_rept_usr/', views.view_med_report_user),
]
