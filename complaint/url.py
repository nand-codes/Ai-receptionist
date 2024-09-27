from django.urls import path, re_path
from complaint import views

urlpatterns = [
    path('complaint/', views.complaint),
    path('reply/', views.reply),
    path('viewcompt/', views.vcom),
    path('viewreply/', views.vre),
    re_path(r'^reply/(?P<idd>\w+)$', views.reply),
]
