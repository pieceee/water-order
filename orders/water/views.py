from datetime import datetime, timedelta
from random import randint
from wsgiref.util import FileWrapper

import coreapi
import jwt
import xlwt
from django.http import HttpResponse
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema
from rest_framework.views import APIView

from .models import Order, Product, ProductOrder, Profile
from .serializers import (AdressSerializer, CartSerializer, OrderSerializer,
                          OrdersListSerializer, ProductSerializer)
from .smsc_api import *
from .Utils import ExcelCreator, check_coord, clear_number


class OrderViewSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ["post", "put"]:
            extra_fields = [
                # coreapi.Field('desc', required=True,
                #               location="body",
                #               type="string"),
                coreapi.Field("body", location="body")
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields


JWT_SECRET = "secret"
JWT_ALGORITHM = "HS256"
JWT_EXP_DELTA_MINUTES = 180


class AuthSmsView(APIView):
    schema = OrderViewSchema()

    def post(self, request):
        """ Отправка смс
            Пример  {'phone': '+79009317249', 'name': 'Alexander'}
            Поле name опциональное, требуется, если номер не зарегистрирован в системе"""
        number = clear_number(request.data.get("phone"))
        name = request.data.get("name")
        if not number:
            return Response(
                {"Error": "field 'phone' don't exist in request"}, status="400"
            )
        try:
            profile = Profile.objects.get(phone=number)
        except:
            # return Response({"Error": "number not found"}, status="400")
            profile = Profile()
            profile.name = name
            profile.phone = number
            profile.save()
        if profile:
            code = randint(1000, 9999)
            smsc = SMSC()
            message = "Код подтверждения {}".format(code)
            if float(smsc.get_sms_cost(number, message)[0]) > 3:
                print("high cost sms to number {}".format(number))
                return Response({"Error": "send message error"}, status="400")
            else:
                result = smsc.send_sms(number, message)
                if len(result) == 4:
                    id_message, count, cost, balance = result
                    print("sent sms-code: ", code)
                    request.session["code"] = str(code)
                    return Response({"Success": "sms sent"}, status="200")
                else:
                    id_message, error = result
                    print("error code {}".format(error))
                    return Response({"Error": "send message error"}, status="400")


class ConfirmAuthView(APIView):
    schema = OrderViewSchema()

    def post(self, request):
        """Возврващает токен и роль пользователя
         Пример { "phone": "+79009317249", "code": "7996"}
         """
        # print(request.data)
        try:
            phone = clear_number(request.data.get("phone"))
            users_code = request.data.get("code")
        except:
            return Response({"Error": "invalid_number"}, status="400")
        if not phone or not users_code:
            return Response(
                {"Error": "field 'phone' or 'code' don't exist in request"},
                status="400",
            )
        my_code = request.session.get("code", None)
        profile = Profile.objects.get(phone=phone)  # check number
        if users_code == my_code:
            payload = {
                "user_id": profile.pk,
                "exp": datetime.utcnow() + timedelta(minutes=JWT_EXP_DELTA_MINUTES),
            }
            jwt_token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)
            return Response(
                {"access_token": jwt_token.decode("utf-8"), "userrole": profile.role},
                status="200",
            )
        return Response({"Error": "invalid code"}, status="400")


class OrderView(APIView):
    schema = OrderViewSchema()

    def post(self, request):
        """ Возвращает список заказов
        Поля status и client_id могут быть пустыми
        Пример: {
  "status": "confirmed",
  "client_id": ""
}"""
        # acc_tok = request.data.get('access_token')
        acc_tok = request.headers.get("authorization", None)
        try:
            payload = jwt.decode(acc_tok, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        except (jwt.DecodeError, jwt.ExpiredSignatureError):
            return Response({"Error": "Token is invalid"}, status=400)
        # if User.objects.get(id=payload['user_id']).profile.role == 'customer':
        status = request.data.get("status")
        client_id = request.data.get("client_id")
        if status and client_id:
            orders = Order.objects.filter(status=status, user_id=client_id)
        elif status:
            orders = Order.objects.filter(status=status)
        elif client_id:
            orders = Order.objects.filter(status=status)
        else:
            orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response({"orders": serializer.data}, status=200)

    def put(self, request):
        """
Изменяет статус заказа
Пример {
  "status": "confirmed",
            "id": 30
}
    """
        # acc_tok = request.data.get('access_token')
        acc_tok = request.headers.get("authorization", None)
        try:
            payload = jwt.decode(acc_tok, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        except (jwt.DecodeError, jwt.ExpiredSignatureError):
            return Response({"Error": "Token is invalid"}, status=400)
        try:
            order_id = request.data.get("id")
            saved_order = Order.objects.get(pk=order_id)
        except:
            return Response({"Error": "order not exist"}, status=400)
        new_status = request.data.get("status")
        saved_order.status = new_status
        saved_order.save()
        serializer = OrderSerializer(saved_order)
        return Response({"Order": serializer.data}, status=200)


class NewOrderView(APIView):
    schema = OrderViewSchema()

    def post(self, request):
        """
           Создание заказа
           Пример {
"cart": [
{
"product_id": "1",
"count": 2
},
{
"product_id": "2",
"count": 5
}
],
"address": { "coords": "51.64 39.26", "place": "revolycii 65", "comment": "lalala"}
}
           """
        acc_tok = request.data.get("access_token")
        acc_tok = request.headers.get("authorization", None)
        try:
            payload = jwt.decode(acc_tok, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        except (jwt.DecodeError, jwt.ExpiredSignatureError):
            return Response({"Error": "Token is invalid"}, status=400)
        carts = request.data.get("cart")
        address = request.data.get("address")
        carts_serializer = CartSerializer(data=carts, many=True)
        address_serializer = AdressSerializer(data=address)
        if carts_serializer.is_valid():
            if len(carts_serializer.data) == 0:
                return Response({"Error": "0 products in order"}, status=400)
        n, e = map(float, address_serializer.coords.split())
        if not check_coord(n, e):
            return Response({"Error": "coordinates out of Voronezh"}, status=400)
        order = Order()
        order.user = Profile.objects.get(id=payload["user_id"])
        # order.user = Profile.objects.get(id=1)
        order.status = "registered"
        order.date = datetime.now()
        order.place = address_serializer.coords
        order.address = address_serializer.place
        order.comment = address_serializer.comment
        order.save()
        if carts_serializer.is_valid():
            for cs in carts_serializer.data:
                po = ProductOrder()
                po.order = order
                po.product = Product.objects.get(id=cs["product_id"])
                po.count = cs["count"]
                po.save()
        return Response({"Success": "order created"}, status=200)


class ClientView(APIView):
    schema = OrderViewSchema()

    def get(self, request):
        """
         Возвращает информацию о клиенте по его токену
         Отправляется пустой запрос
         Пример {}
        """
        # acc_tok = request.data.get('access_token')
        acc_tok = request.headers.get("authorization", None)
        try:
            payload = jwt.decode(acc_tok, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        except (jwt.DecodeError, jwt.ExpiredSignatureError):
            return Response({"Error": "Token is invalid"}, status=400)
        client = Profile.objects.get(id=payload["user_id"])
        # client = Profile.objects.get(id=1)
        answer = {"phone": client.phone, "name": client.name}
        return Response({"Client": answer}, status=200)

    def put(self, request):
        """Изменяет информацию о клиенте
        Пример {
 "phone": "+79009317249",
 "name": "Alexander"
}"""
        acc_tok = request.headers.get("authorization", None)
        try:
            payload = jwt.decode(acc_tok, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        except (jwt.DecodeError, jwt.ExpiredSignatureError):
            return Response({"Error": "Token is invalid"}, status=400)
        client = Profile.objects.get(id=payload["user_id"])
        # client = Profile.objects.get(id=1)
        try:
            new_phone = clear_number(request.data.get("phone"))
            new_name = request.data.get("name")
        except:
            return Response({"Error": "invalid number"}, status=400)
        client.phone = new_phone
        client.name = new_name
        client.save()
        return Response(
            {"Client": {"phone": client.phone, "name": client.name}}, status=200
        )


class ReportView(APIView):
    schema = OrderViewSchema()

    def get(self, request):
        """
         Возвращает файл excel со всеми заказами
        """
        acc_tok = request.data.get("access_token")
        acc_tok = request.headers.get("authorization", None)
        try:
            payload = jwt.decode(acc_tok, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        except (jwt.DecodeError, jwt.ExpiredSignatureError):
            return Response({"Error": "Token is invalid"}, status=400)
        client = Profile.objects.get(id=payload["user_id"])
        if client.role != "manager":
            return Response({"Error": "Customer has not acccess"}, status=400)
        excel = ExcelCreator()
        file_name = excel.get_table(orders=Order.objects.all())
        f = open(file_name, "rb")
        response = HttpResponse(FileWrapper(f), content_type="application/xls")
        response["Content-Disposition"] = 'attachment; filename="%s"' % "orders.xls"
        return response
