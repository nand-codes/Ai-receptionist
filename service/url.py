from django.urls import path, re_path
from service import views

urlpatterns = [
    path('service/', views.service),
    path('viewser/', views.vser),
    re_path(r'^remove/(?P<idd>\w+)$', views.remove),
]
