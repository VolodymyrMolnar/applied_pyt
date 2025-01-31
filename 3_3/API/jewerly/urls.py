from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_page, name='welcome_page'),

    path('client/', views.show_clients, name='show_clients'),
    path('client/add/', views.client_add, name='client_add'),
    path('client/<int:client_id>/', views.client_detail, name='client_detail'),
    path('clients/edit/<int:client_id>/', views.client_edit, name='client_edit'),
    path('clients/delete/<int:client_id>/', views.client_delete, name='client_delete'),

    path('orders/', views.orders_list, name='orders_list'),
    path('orders/create/', views.order_add, name='order_add'),
    path('order/detail/<int:order_id>/', views.order_detail, name='order_detail'),
    path('order_edit/<int:order_id>/', views.order_edit, name='order_edit'),
    path('order_delete/<int:order_id>/', views.order_delete, name='order_delete'),

    path('external/clients/', views.external_clients_list, name='external_clients_list'),
    path('external/clients/add/', views.add_external_client, name='add_external_client'),
    path('external/clients/<int:client_id>/delete/', views.delete_external_client, name='delete_external_client'),
]
