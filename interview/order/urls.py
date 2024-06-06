
from django.urls import path
from interview.order.views import OrderListCreateView, OrderTagListCreateView, TagsByOrdersListView


urlpatterns = [
    path('tags/', OrderTagListCreateView.as_view(), name='order-detail'),
    path('<int:id>/tags/', TagsByOrdersListView.as_view(), name='order-tags'),
    path('', OrderListCreateView.as_view(), name='order-list'),

]