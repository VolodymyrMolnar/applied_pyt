from rest_framework import viewsets
from .models import Customer, Technician, Repair, Part, Feedback, RepairStatus
from .serializers import CustomerSerializer, TechnicianSerializer, RepairSerializer, PartSerializer, FeedbackSerializer, RepairStatusSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import models
from django.shortcuts import get_object_or_404, redirect



from django.shortcuts import render, redirect

def client_list(request):
    clients = Customer.objects.all()

    if request.method == "POST":
        client_id = request.POST.get('client_id')
        if client_id:
            try:
                client = Customer.objects.get(id=client_id)
                client.delete()
            except Customer.DoesNotExist:
                pass

        return redirect('client_list')

    return render(request, "external_app/client_list.html", {"clients": clients})


def delete_client(request, client_id):
    """Функція для видалення клієнта."""
    client = get_object_or_404(Customer, id=client_id)
    client.delete()
    return redirect('client_list')

def client_add(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        if name and email and phone:
            new_client = Customer.objects.create(name=name, email=email, phone=phone)
            return redirect('client_list')

    return render(request, "external_app/add_client.html")

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class TechnicianViewSet(viewsets.ModelViewSet):
    queryset = Technician.objects.all()
    serializer_class = TechnicianSerializer

class RepairViewSet(viewsets.ModelViewSet):
    queryset = Repair.objects.all()
    serializer_class = RepairSerializer

    @action(detail=False, methods=['get'])
    def report(self, request):
        data = Repair.objects.values('status').annotate(count=models.Count('id'))
        return Response(data)

class PartViewSet(viewsets.ModelViewSet):
    queryset = Part.objects.all()
    serializer_class = PartSerializer

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class RepairStatusViewSet(viewsets.ModelViewSet):
    queryset = RepairStatus.objects.all()
    serializer_class = RepairStatusSerializer