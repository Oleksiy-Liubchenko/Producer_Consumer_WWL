from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from producer_consumer_app.models import Order
from django.contrib.auth.mixins import LoginRequiredMixin


class OrderListView(ListView, LoginRequiredMixin):
    model = Order
    template_name = "producer_consumer_app/order_list.html"
    context_object_name = "orders"

    def get_queryset(self):
        return Order.objects.filter(employee__id=self.request.user.id)


def delete_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        order.delete()
        return redirect("order_list")
    return render(request, "producer_consumer_app/order_list.html")
