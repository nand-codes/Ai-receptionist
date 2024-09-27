from django.urls import path
from temp import views

urlpatterns = [
    path('admin/', views.admin),
    path('user/', views.user),
    path('doctor/', views.doctor),
    path('home/', views.home),
    path('user_he/', views.user_home),
    path('dr_hme/', views.dr_hme),
    path('admn_hm/', views.admn_hm),
]
