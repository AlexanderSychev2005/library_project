from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import StudentOrder
from .forms import StudentOrderForm


# Create your views here.
class OrderListView(ListView):
    model = StudentOrder
    template_name = 'order/order_list.html'


class OrderDetailView(DetailView):
    model = StudentOrder
    template_name = 'order/order_detail.html'


class OrderCreateView(CreateView):
    model = StudentOrder
    form_class = StudentOrderForm
    template_name = 'order/order_create.html'
    success_url = reverse_lazy('order_list')


class OrderUpdateView(UpdateView):
    model = StudentOrder
    form_class = StudentOrderForm
    template_name = 'order/order_update.html'
    success_url = reverse_lazy('order_list')


class OrderDeleteView(View):
    def post(self, request, pk):
        order = get_object_or_404(StudentOrder, pk=pk)
        order.delete()
        return redirect('order_list')
