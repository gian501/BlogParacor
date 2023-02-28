#from django.contrib import admin
from django.urls import path
from . import views
from .views import login_request
#from django.contrib.auth.views import LogoutView
 

urlpatterns = [
    path('', views.inicio, name='Inicio'), # esta conectado con views
    path('pulseras/', views.pulseras, name='Pulseras'),
    path('login', views.login_request, name='Login'),
    path('register', views.register, name='Register'),

    
    path('curso/list', views.PulseraList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.PulseraDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.PulseraCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.PulseraUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.PulseraDelete.as_view(), name='Delete'),


]   


#path('login', views.login_request, name='Login'),
#path('register', views.register, name='Register'),