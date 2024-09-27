from django.urls import path
from patient import views

urlpatterns = [
    path('patient/', views.patient),
    path('viewp/', views.vpnt),
    path('view_patient_admin/', views.view_patient_admin),
]
