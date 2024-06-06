from django.test import TestCase
from rest_framework.test import APITestCase

class TagsByOrderTestCase(APITestCase):
    def test_return_tags(self):
        order = Order.objects.create(
            start_date='2024-05-05',
            embargo_date='2024-07-05',
            inventory_id=1
        )
        order.tags.add(OrderTag(name='tag test'))
        order.tags.add(OrderTag(name='tag test2'))
        order.tags.add(OrderTag(name='tag test3'))
        res = self.client.get('/orders/1/tags/')
        self.assertEqual(len(response), 3)
