from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView

from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer

# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer


class TagsByOrdersListView(APIView):
    queryset = Order.objects.all()
    serializer_class = OrderTagSerializer

    def get(self, request: Request, *args, **kwargs) -> Response:
        order = self.queryset.get(id=kwargs['id'])

        serializer = self.serializer_class(order.tags.all(), many=True)

        return Response(serializer.data, status=200)
