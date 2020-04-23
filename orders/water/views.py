from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, Order, ProductOrder, User, Profile
from .serializers import ProductSerializer, OrdersListSerializer, OrderSerializer, CartSerializer, AdressSerializer
from datetime import datetime
from rest_framework.generics import get_object_or_404
from random import randint

class AuthSmsView (APIView):
    def get(self, request):
        phone = request.data.get('tel')
        profile = Profile.objects.get(phone=phone)
        if profile:
            code = randint(1000, 9999)
            # send sms
            request.session['code'] = str(code)
            return Response("sms sent")

    def post(self, request):
        phone = request.data.get('username')
        users_code = str(request.data.get('code'))
        my_code = request.session.get('code', None)
        if users_code == my_code:
            # create access token
            pass

class ProductView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({"products": serializer.data})


class OrderView(APIView):
    def get(self, request):
        orders_list = request.data.get('orders_list')
        serializer = OrdersListSerializer(data=orders_list)
        print('serializer: ', serializer)
        orders = Order.objects.filter(status=serializer.status, user_id=serializer.client_id)
        serializer2 = OrderSerializer(orders, many=True)
        print('serializer2: ', serializer2)
        return Response({"orders": serializer2.data})

    def put(self, request):
        order_id = request.data.get('order').get('id')
        saved_order = get_object_or_404(Order.objects.all(), pk=order_id)
        if not saved_order:
            return Response({"order not exist"})
        data = request.data.get('order')
        serializer = OrderSerializer(instance=saved_order, data=data, partial=True)
        print("serializer : ", serializer)
        if serializer.is_valid():
            saved_order2 = serializer.save()
        return Response(OrderSerializer(saved_order2).data)


class NewOrderView(APIView):
    def post(self, request):
        acc_tok = request.data.get('access_token')
        carts = request.data.get('cart')
        adress = request.data.get('adress')

        carts_serializer = CartSerializer(data=carts, many=True)
        addres_serializer = AdressSerializer(data=adress)

        order = Order()
        order.user = User.objects.get(id=1) # get by access token
        order.status = 'registered'
        order.date = datetime.now()
        order.place = addres_serializer.coords
        order.save()
        print('carts_serializer: ', carts_serializer)
        if carts_serializer.is_valid():
            print('valid')
            for cs in carts_serializer.data:
                print('cs: ',  cs)
                po = ProductOrder()
                po.order = order
                po.product = Product.objects.get(id=cs['product_id'])
                po.count = cs['count']
                po.save()
        return Response({"success": "order created"})


class ClientView(APIView):
    def get(self, request):
        token = request.data.get('access_token')
        # get user by token
        client = User.objects.get(pk=1)
        answer = {}
        answer['phone'] = client.profile.phone
        answer['name'] = client.profile.name
        return Response({"client": answer})

    def put(self, request):
        token = request.data.get('access_token')
        # get user by token
        client = User.objects.get(pk=1)
        new_phone = request.data.get('phone')
        new_name = request.data.get('name')
        client.profile.phone = new_phone
        client.profile.name = new_name
        client.profile.save()
        return Response({"access_token": token, "phone": client.profile.phone, "name": client.profile.name})
