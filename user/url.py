from django.urls import path
from user import views

urlpatterns = [
    path('user/', views.user),
    path('viewu/', views.vuser),
]
