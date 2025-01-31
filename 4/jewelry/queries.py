from django.db.models import Sum, Count, Min, Avg
from jewelry.models import Order, OrderDetails


def total_orders_per_client():
    return (
        Order.objects.values('client__first_name', 'client__last_name')
        .annotate(total_spent=Sum('total_price'))
        .order_by('-total_spent')
    )


def top_employees_by_orders():
    return (
        Order.objects.values('employee__first_name', 'employee__last_name')
        .annotate(order_count=Count('id'))
        .order_by('-order_count')
    )


def most_popular_product_type():
    return (
        OrderDetails.objects.values('product__type')
        .annotate(total_quantity=Sum('quantity'))
        .order_by('-total_quantity')
    )


def high_spending_clients():
    return (
        Order.objects.values('client__first_name', 'client__last_name')
        .annotate(total_spent=Sum('total_price'))
        .filter(total_spent__gt=1000)
        .order_by('-total_spent')
    )


def min_products_per_order():
    return (
        OrderDetails.objects.values('order__client__first_name', 'order__client__last_name')
        .annotate(min_quantity=Min('quantity'))
        .order_by('min_quantity')
    )


def avg_price_per_product_type():
    return (
        OrderDetails.objects.values('product__type')
        .annotate(avg_price=Avg('product__price'))
        .order_by('-avg_price')
    )
