from django.urls import re_path, include

from doctor import views

urlpatterns = [
    re_path('doct/',views.doctor),
    re_path('view/',views.vdoct),
    re_path('view_dr_user', views.v_doct_user),

]