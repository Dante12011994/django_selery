from django.urls import path

from shop.apps import ShopConfig
from shop.views import ItemDetailView, ItemListView, buy

app_name = ShopConfig.name

urlpatterns = [
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item_view'),
    path('', ItemListView.as_view(), name='item'),
    path('buy/<int:pk>/', buy, name='buy_item')

]
