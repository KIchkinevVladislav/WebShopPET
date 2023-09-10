from django.urls import path

from api.views import ProductListView

app_name = 'api'

urlpatterns = [
    path('product-list/', ProductListView.as_view(), name='products_list'),
]