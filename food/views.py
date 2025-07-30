from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class IndexClassView(LoginRequiredMixin,ListView):
    model = Item 
    template_name = 'food/index.html'
    context_object_name = 'items'

class ItemDetailView(LoginRequiredMixin,DetailView):
    model = Item 
    template_name = 'food/detail.html'
    context_object_name = 'item'
    pk_url_kwarg = 'pk'

class ItemCreateView(LoginRequiredMixin,CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'food/item_form.html'
    success_url = reverse_lazy('food:index')

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['title'] = 'Add New Item'
        context['button_text'] = 'Add Item'
        return context

class ItemUpdateView(LoginRequiredMixin,UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'food/item_form.html'
    success_url = reverse_lazy('food:index')
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Item'
        context['button_text'] = 'Update Item'
        return context

class ItemDeleteView(LoginRequiredMixin,DeleteView):
    model = Item
    template_name = 'food/item_delete.html'
    success_url = reverse_lazy('food:index')
    pk_url_kwarg = 'id'