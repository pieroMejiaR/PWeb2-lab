from django.contrib import admin
from django.urls import path
from Apps.destinations.views import destination_list, add_destination, update_destination, delete_destination

urlpatterns = [
    path('', destination_list, name='destination_list'),
    path('list/', destination_list, name='destination_list'),
    path('add/', add_destination, name='add_destination'),
    path('update/<int:destination_id>/', update_destination, name='update_destination'),
    path('delete/<int:destination_id>/', delete_destination, name='delete_destination'),
]
