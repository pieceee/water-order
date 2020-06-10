from math import sqrt

import xlwt

from .models import Order, Product, ProductOrder, Profile


def clear_number(number):
    if 10 <= len(number) <= 12:
        return "+7" + number[-10:]
    else:
        raise Exception("number invalid")


def check_coord(n, e):
    return is_in(n, e)


def is_in(n, e):
    N, E = 51.6, 39.2
    delta = 0.3
    return sqrt(abs(N - n) * abs(N - n) + abs(E - e) * abs(E - e)) < 0.3


class ExcelCreator:
    def _init_(self):
        pass

    def get_table(self, orders):
        wb = xlwt.Workbook()
        ws = wb.add_sheet("Заказы")

        ws.write(0, 0, "Имя заказчика")
        ws.write(0, 1, "Телефон")
        ws.write(0, 2, "Товары")
        ws.write(0, 3, "Дата заказа")
        ws.write(0, 4, "Место")
        ws.write(0, 5, "Статус")
        ws.write(0, 6, "Комментарий")
        i = 1
        for order in orders:
            ws.write(i, 0, order.user.name)
            ws.write(i, 1, order.user.phone)
            ws.write(i, 2, self.build_products_line(order))
            ws.write(i, 3, str(order.date))
            ws.write(i, 4, order.address)
            ws.write(i, 5, order.status)
            ws.write(i, 6, order.comment)
            i += 1
        wb.save("orders.xls")
        return "orders.xls"

    def build_products_line(self, order):
        product_orders = ProductOrder.objects.filter(order_id=order.pk)
        line = ""
        for po in product_orders:
            line += po.product.name + " - " + str(po.count) + " штук"
        return line
