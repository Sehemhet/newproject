from django.shortcuts import render
from auto.models import Cars
from django.views.generic import ListView, DetailView

from auto.models import Brands


class garage(ListView):
    paginate_by = 9
    model = Brands
    context_object_name = 'model'
    template_name = 'auto/models_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_selected'] = 0
        context['title'] = 'Гараж'
        return context

    def get_queryset(self):
        return Cars.objects.all()


class my_car(DetailView):
    model = Cars
    context_object_name = 'car'
    template_name = 'auto/car_detail.html'
    extra_context = {'title': 'Автомобиль'}
    slug_url_kwarg = 'slug'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

# Create your views here.
