from django.urls import path
from jewelry.views import (
    query1_dashboard_plotly, query1_dashboard_bokeh,
    query2_dashboard_plotly, query2_dashboard_bokeh,
    query3_dashboard_plotly, query3_dashboard_bokeh,
    query4_dashboard_plotly, query4_dashboard_bokeh,
    query5_dashboard_plotly, query5_dashboard_bokeh,
    query6_dashboard_plotly, query6_dashboard_bokeh,
    queries_dashboard
)
from jewelry.views import (
    TotalOrdersPerClientAPI,
    TopEmployeesByOrdersAPI,
    MostPopularProductTypeAPI,
    HighSpendingClientsAPI,
    MinProductsPerOrderAPI,
    AvgPricePerProductTypeAPI,
)

urlpatterns = [
    path('dash/query1/plotly/', query1_dashboard_plotly, name='query1_dashboard_plotly'),
    path('dash/query1/bokeh/', query1_dashboard_bokeh, name='query1_dashboard_bokeh'),
    path('dash/query2/plotly/', query2_dashboard_plotly, name='query2_dashboard_plotly'),
    path('dash/query2/bokeh/', query2_dashboard_bokeh, name='query2_dashboard_bokeh'),
    path('dash/query3/plotly/', query3_dashboard_plotly, name='query3_dashboard_plotly'),
    path('dash/query3/bokeh/', query3_dashboard_bokeh, name='query3_dashboard_bokeh'),
    path('dash/query4/plotly/', query4_dashboard_plotly, name='query4_dashboard_plotly'),
    path('dash/query4/bokeh/', query4_dashboard_bokeh, name='query4_dashboard_bokeh'),
    path('dash/query5/plotly/', query5_dashboard_plotly, name='query5_dashboard_plotly'),
    path('dash/query5/bokeh/', query5_dashboard_bokeh, name='query5_dashboard_bokeh'),
    path('dash/query6/plotly/', query6_dashboard_plotly, name='query6_dashboard_plotly'),
    path('dash/query6/bokeh/', query6_dashboard_bokeh, name='query6_dashboard_bokeh'),

    path('queries/', queries_dashboard, name='queries_dashboard'),


    path('total-orders-per-client/', TotalOrdersPerClientAPI.as_view(), name='total_orders_per_client'),
    path('top-employees-by-orders/', TopEmployeesByOrdersAPI.as_view(), name='top_employees_by_orders'),
    path('most-popular-product-type/', MostPopularProductTypeAPI.as_view(), name='most_popular_product_type'),
    path('high-spending-clients/', HighSpendingClientsAPI.as_view(), name='high_spending_clients'),
    path('min-products-per-order/', MinProductsPerOrderAPI.as_view(), name='min_products_per_order'),
    path('avg-price-per-product-type/', AvgPricePerProductTypeAPI.as_view(), name='avg_price_per_product_type'),

]
