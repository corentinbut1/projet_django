from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('machines/', views.machine_list_view, name='machines'),
    path('personnels/', views.personnel_list_view, name='personnels'),
    path('machine-detail/<pk>', views.machine_detail_view, name='machine-detail'),
    path('personnel-detail/<pk>', views.personnel_detail_view, name='personnel-detail'),
    path('add-machines', views.machine_add_form, name='add-machines'),
    path('delete-machine', views.delete_machine, name= 'delete-machine'),
    path('delete-personnel', views.delete_personnel, name= 'delete-personnel'),
    path('add-personnels', views.personnel_add_form, name='add-personnels'),
    
]