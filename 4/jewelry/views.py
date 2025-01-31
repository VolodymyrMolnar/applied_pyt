from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated

from django.http import Http404

from .models import Client, Employee, Product, Order, OrderDetails
from .serializers import ClientSerializer, EmployeeSerializer, ProductSerializer, OrderSerializer, OrderDetailsSerializer

from django.db.models import Avg, Min, Max, Count, Sum
from jewelry.models import Product, OrderDetails, Order
from django.db.models import Avg
from jewelry.models import Product

from dash.query1_dashboard_v1 import create_query1_chart
from dash.query2_dashboard_v1 import create_query2_chart
from dash.query3_dashboard_v1 import create_query3_chart
from dash.query4_dashboard_v1 import create_query4_chart
from dash.query5_dashboard_v1 import create_query5_chart
from dash.query6_dashboard_v1 import create_query6_chart

from dash.query1_dashboard_bokeh import create_query1_bokeh_chart
from dash.query2_dashboard_bokeh import create_query2_bokeh_chart
from dash.query3_dashboard_bokeh import create_query3_bokeh_chart
from dash.query4_dashboard_bokeh import create_query4_bokeh_chart
from dash.query5_dashboard_bokeh import create_query5_bokeh_chart
from dash.query6_dashboard_bokeh import create_query6_bokeh_chart




from rest_framework.views import APIView

from jewelry.queries import (
    total_orders_per_client,
    top_employees_by_orders,
    most_popular_product_type,
    high_spending_clients,
    min_products_per_order,
    avg_price_per_product_type,
)


class TotalOrdersPerClientAPI(APIView):
    def get(self, request, format=None):
        data = list(total_orders_per_client())
        df = pd.DataFrame(data)
        return Response(df.to_dict(orient='records'))


class TopEmployeesByOrdersAPI(APIView):
    def get(self, request, format=None):
        data = list(top_employees_by_orders())
        df = pd.DataFrame(data)
        return Response(df.to_dict(orient='records'))


class MostPopularProductTypeAPI(APIView):
    def get(self, request, format=None):
        data = list(most_popular_product_type())
        df = pd.DataFrame(data)
        return Response(df.to_dict(orient='records'))


class HighSpendingClientsAPI(APIView):
    def get(self, request, format=None):
        data = list(high_spending_clients())
        df = pd.DataFrame(data)
        return Response(df.to_dict(orient='records'))


class MinProductsPerOrderAPI(APIView):
    def get(self, request, format=None):
        data = list(min_products_per_order())
        df = pd.DataFrame(data)
        return Response(df.to_dict(orient='records'))


class AvgPricePerProductTypeAPI(APIView):
    def get(self, request, format=None):
        data = list(avg_price_per_product_type())
        df = pd.DataFrame(data)
        return Response(df.to_dict(orient='records'))

def queries_dashboard(request):
    context = {
        'total_orders_per_client': total_orders_per_client(),
        'top_employees_by_orders': top_employees_by_orders(),
        'most_popular_product_type': most_popular_product_type(),
        'high_spending_clients': high_spending_clients(),
        'min_products_per_order': min_products_per_order(),
        'avg_price_per_product_type': avg_price_per_product_type(),
    }
    return render(request, 'queries_dashboard.html', context)


def query1_dashboard_plotly(request):
    sort_order = request.GET.get('sort', 'default')
    data = Product.objects.values('type').annotate(avg_price=Avg('price')).order_by('type')
    chart, stats = create_query1_chart(data, sort_order)
    if not chart:
        return render(request, 'query1_dashboard.html', {'error': "Дані для графіка відсутні."})
    return render(request, 'query1_dashboard.html', {'chart': chart, 'stats': stats})


def query1_dashboard_bokeh(request):
    sort_order = request.GET.get('sort', 'default')
    data = Product.objects.values('type').annotate(avg_price=Avg('price')).order_by('type')
    script, div, stats = create_query1_bokeh_chart(data, sort_order)
    if not script or not div:
        return render(request, 'query1_dashboard_bokeh.html', {'error': "Дані для графіка відсутні."})
    return render(request, 'query1_dashboard_bokeh.html', {'script': script, 'div': div, 'stats': stats})


def query2_dashboard_plotly(request):

    sort_order = request.GET.get('sort', 'default')
    data = OrderDetails.objects.values('product__type').annotate(total_quantity=Sum('quantity')).order_by('product__type')
    chart, stats = create_query2_chart(data, sort_order)
    if not chart:
        return render(request, 'query2_dashboard.html', {'error': "Дані для графіка відсутні."})
    return render(request, 'query2_dashboard.html', {'chart': chart, 'stats': stats})

def query2_dashboard_bokeh(request):
    sort_order = request.GET.get('sort', 'default')
    data = OrderDetails.objects.values('product__type').annotate(total_quantity=Sum('quantity')).order_by('product__type')
    script, div, stats = create_query2_bokeh_chart(data, sort_order)
    if not script or not div:
        return render(request, 'query2_dashboard_bokeh.html', {'error': "Дані для графіка відсутні."})
    return render(request, 'query2_dashboard_bokeh.html', {'script': script, 'div': div, 'stats': stats})

def query3_dashboard_plotly(request):
    sort_order = request.GET.get('sort', 'default')
    data = Product.objects.values('type').annotate(max_price=Max('price')).order_by('type')
    chart, stats = create_query3_chart(data, sort_order)
    if not chart:
        return render(request, 'query3_dashboard.html', {'error': "Дані для графіка відсутні."})
    return render(request, 'query3_dashboard.html', {'chart': chart, 'stats': stats})

def query3_dashboard_bokeh(request):
    sort_order = request.GET.get('sort', 'default')
    data = Product.objects.values('type').annotate(max_price=Max('price')).order_by('type')
    script, div, stats = create_query3_bokeh_chart(data, sort_order)
    if not script or not div:
        return render(request, 'query3_dashboard_bokeh.html', {'error': "Дані для графіка відсутні."})
    return render(request, 'query3_dashboard_bokeh.html', {'script': script, 'div': div, 'stats': stats})

def query4_dashboard_plotly(request):

    sort_order = request.GET.get('sort', 'default')
    data = OrderDetails.objects.values('order__id').annotate(min_quantity=Min('quantity')).order_by('order__id')  # Дані
    chart, stats = create_query4_chart(data, sort_order)
    if not chart:
        return render(request, 'query4_dashboard.html', {'error': "Дані для графіка відсутні."})
    return render(request, 'query4_dashboard.html', {'chart': chart, 'stats': stats, 'sort_order': sort_order})


def query4_dashboard_bokeh(request):
    sort_order = request.GET.get('sort', 'default')
    data = OrderDetails.objects.values('order__id').annotate(min_quantity=Min('quantity')).order_by('order__id')  # Дані
    script, div, stats = create_query4_bokeh_chart(data, sort_order)
    if not script or not div:
        return render(request, 'query4_dashboard_bokeh.html', {'error': "Дані для графіка відсутні."})
    return render(request, 'query4_dashboard_bokeh.html', {'script': script, 'div': div, 'stats': stats, 'sort_order': sort_order})

def query5_dashboard_plotly(request):
    sort_order = request.GET.get('sort', 'default')
    data = Order.objects.values('status').annotate(order_count=Count('id')).order_by('status')  # Дані
    chart, stats = create_query5_chart(data, sort_order)
    if not chart:
        return render(request, 'query5_dashboard.html', {'error': "Дані для графіка відсутні."})
    return render(request, 'query5_dashboard.html', {'chart': chart, 'stats': stats, 'sort_order': sort_order})

def query5_dashboard_bokeh(request):
    sort_order = request.GET.get('sort', 'default')
    data = Order.objects.values('status').annotate(order_count=Count('id')).order_by('status')  # Дані
    script, div, stats = create_query5_bokeh_chart(data, sort_order)
    if not script or not div:
        return render(request, 'query5_dashboard_bokeh.html', {'error': "Дані для графіка відсутні."})
    return render(request, 'query5_dashboard_bokeh.html', {'script': script, 'div': div, 'stats': stats, 'sort_order': sort_order})


def query6_dashboard_plotly(request):
    sort_order = request.GET.get('sort', 'default')
    data = OrderDetails.objects.values('product__type').annotate(avg_price=Avg('product__price')).order_by('product__type')
    chart, stats = create_query6_chart(data, sort_order)
    if not chart:
        return render(request, 'query6_dashboard.html', {'error': "Дані для графіка відсутні."})
    return render(request, 'query6_dashboard.html', {'chart': chart, 'stats': stats})



def query6_dashboard_bokeh(request):
    sort_order = request.GET.get('sort', 'default')
    data = OrderDetails.objects.values('product__type').annotate(avg_price=Avg('product__price')).order_by('product__type')
    script, div, stats = create_query6_bokeh_chart(data, sort_order)
    if not script or not div:
        return render(request, 'query6_dashboard_bokeh.html', {'error': "Дані для графіка відсутні."})
    return render(request, 'query6_dashboard_bokeh.html', {'script': script, 'div': div, 'stats': stats})


queryset = Product.objects.values('type').annotate(avg_price=Avg('price')).order_by('avg_price')

class ProductAveragePriceView(APIView):
    def get(self, request):
        data = Product.objects.values('type').annotate(avg_price=Avg('price')).order_by('avg_price')
        return Response(data)


from .dashboard import create_bar_chart, create_pie_chart, create_line_chart

def dashboard_view(request):
    data = list(Product.objects.values('type', 'price'))
    df = pd.DataFrame(data)

    bar_chart = create_bar_chart(df)
    pie_chart = create_pie_chart(df)
    line_chart = create_line_chart(df)

    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if min_price and max_price:
        df = df[(df['price'] >= float(min_price)) & (df['price'] <= float(max_price))]

    return render(request, 'dashboard.html', {
        'bar_chart': bar_chart,
        'pie_chart': pie_chart,
        'line_chart': line_chart,
    })


import pandas as pd
from rest_framework.response import Response

class ProductDataAnalysisView(APIView):
    def get(self, request):
        data = Product.objects.values('type', 'price')
        df = pd.DataFrame(data)

        analysis = {
            'mean_price': df['price'].mean(),
            'median_price': df['price'].median(),
            'min_price': df['price'].min(),
            'max_price': df['price'].max(),
        }
        return Response(analysis)

def analyze_data():
    data = list(Product.objects.values('type', 'price'))  # Отримання даних з моделі Product
    df = pd.DataFrame(data)
    stats = {
        'mean': df['price'].mean(),
        'median': df['price'].median(),
        'min': df['price'].min(),
        'max': df['price'].max(),
    }
    return df

from django.shortcuts import render

def dashboard_view(request):
    data = analyze_data()
    chart = create_bar_chart(data)
    return render(request, 'dashboard.html', {'chart': chart})


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetailsViewSet(viewsets.ModelViewSet):
    queryset = OrderDetails.objects.all()
    serializer_class = OrderDetailsSerializer

class OrderDetailsList(APIView):
    def get(self, request, format=None):
        order_details = OrderDetails.objects.all()
        serializer = OrderDetailsSerializer(order_details, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OrderDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderDetailsDetail(APIView):
    def get_object(self, pk):
        try:
            return OrderDetails.objects.get(pk=pk)
        except OrderDetails.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        order_detail = self.get_object(pk)
        serializer = OrderDetailsSerializer(order_detail)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        order_detail = self.get_object(pk)
        serializer = OrderDetailsSerializer(order_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        order_detail = self.get_object(pk)
        order_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


