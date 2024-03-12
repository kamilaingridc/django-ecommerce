from django.urls import path
from . import views

urlpatterns = [
    path('clients', views.toList_Clients),
    path('users', views.ClientsView.as_view())
]