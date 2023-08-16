import os
from datetime import datetime

import telebot
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from producer_consumer_app.models import Order


class OrderListView(ListView, LoginRequiredMixin):
    model = Order
    template_name = "producer_consumer_app/order_list.html"
    context_object_name = "orders"

    def get_queryset(self):
        return Order.objects.filter(employee__id=self.request.user.id)


def delete_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        order_data = {
            "pk": order.pk,
            "task_id": order.task_id,
            "name": order.name,
            "employee": (
                f"{order.employee.first_name}_"
                f"{order.employee.position}"
            ),
        }

        message = (
            f"Задача №{order_data['pk']}-{order_data['task_id']} "
            f"під назвою {order_data['name']} була опрацьована "
            f"{order_data['employee']} у {datetime.now()}"
        )

        bot = telebot.TeleBot(os.getenv("TELEGRAM_BOT_TOKEN"))
        chat_id = os.getenv("TELEGRAM_CHAT_ID")
        bot.send_message(chat_id, message)

        order.delete()
        return redirect("order_list")
    return render(request, "producer_consumer_app/order_list.html")
