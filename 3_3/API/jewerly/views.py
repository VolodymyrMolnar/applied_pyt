from django.shortcuts import render, get_object_or_404, redirect
from .models import Order, Client, Product, Employee, OrderDetails
from .forms import OrderForm, OrderDetailsForm, ClientForm

from .NetworkHelper import NetworkHelper


def add_external_client(request):
    if request.method == 'POST':
        data = {
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'phone': request.POST.get('phone'),
        }
        try:
            response = NetworkHelper.create_item('customers', data)
            return redirect('external_clients_list')
        except Exception as e:
            print(f"Error creating client: {e}")
    return render(request, 'external_app/add_client.html')



def delete_external_client(request, client_id):
    try:
        status_code = NetworkHelper.delete_item('customers', client_id)
        if status_code == 204:
            print("Client deleted successfully")
        else:
            print(f"Failed to delete client. Status code: {status_code}")
    except Exception as e:
        print(f"Error deleting client: {e}")
    return redirect('clients_list')

def external_clients_list(request):
    try:
        clients = NetworkHelper.get_list('customers')
    except Exception as e:
        clients = []
        print(f"Error fetching external clients: {e}")

    return render(request, 'external_app/client_list.html', {'clients': clients})


def show_clients(request):
    clients = Client.objects.all()
    return render(request, 'jewerly/list.html', {'clients': clients})

def client_delete(request, client_id):
    client = get_object_or_404(Client, id=client_id)

    client.delete()

    return redirect('show_clients')

def client_detail(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    back_url = request.META.get('HTTP_REFERER', '/client/')
    return render(request, 'jewerly/client_detail.html', {
        'client': client,
        'back_url': back_url
    })


def client_edit(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('show_clients')
    else:
        form = ClientForm(instance=client)
    return render(request, 'jewerly/client_edit.html', {'form': form, 'form_title': 'Edit Client'})


def client_add(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_clients')
    else:
        form = ClientForm()
    return render(request, 'jewerly/client_edit.html', {'form': form, 'form_title': 'Add New Client'})

def orders_list(request):
    orders = Order.objects.select_related('client', 'employee').all()
    return render(request, 'jewerly/orders_list.html', {'orders': orders})

def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'jewerly/order_detail.html', {'order': order})

def order_add(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orders_list')
    else:
        form = OrderForm()
    return render(request, 'jewerly/order_create.html', {'form': form, 'form_title': 'Create Order'})

def order_edit(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('orders_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'jewerly/order_create.html', {'form': form, 'form_title': 'Edit Order'})

def order_delete(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        order.delete()
        return redirect('orders_list')
    return render(request, 'jewerly/order_confirm_delete.html', {'order': order})

def welcome_page(request):
    return render(request, 'jewerly/welcome.html')
