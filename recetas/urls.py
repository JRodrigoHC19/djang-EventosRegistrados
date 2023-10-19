from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('usuario', views.form_user, name='form_user'),
    path('evento', views.form_event, name='form_event'),
    path('registro', views.form_item, name='form_item'),
    path('registar_user', views.register_user, name='register_user'),
    path('registar_event', views.register_event, name='register_event'),
    path('registar_item', views.register_item, name='register_item'),
]