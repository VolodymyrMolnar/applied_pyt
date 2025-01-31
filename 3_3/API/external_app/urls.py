from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, TechnicianViewSet, RepairViewSet, PartViewSet, FeedbackViewSet, RepairStatusViewSet
from . import views

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'technicians', TechnicianViewSet)
router.register(r'repairs', RepairViewSet)
router.register(r'parts', PartViewSet)
router.register(r'feedbacks', FeedbackViewSet)
router.register(r'repair-statuses', RepairStatusViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('client-list/', views.client_list, name='client_list'),
    path('client-add/', views.client_add, name='client_add'),
    path('delete-client/<int:client_id>/', views.delete_client, name='delete_client'),  # додано шлях для видалення
]
