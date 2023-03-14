import form as form
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.forms import forms

from .forms import AddCarsForm
from .models import Cars, Brands

class brand_list(ListView):
    paginate_by = 12
    model = Brands

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Марки'
        return context

class model_list(ListView):
    paginate_by = 12
    model = Cars
    template_name = 'auto/models_list.html'
    allow_empty = False

    def get_queryset(self):
        return Cars.objects.filter(brand__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = str(context['object_list'][0].brand)
        return context

class car_detail(DetailView):
    model = Cars
    context_object_name = 'car'
    template_name = 'auto/car_detail.html'

class car_create(LoginRequiredMixin, CreateView):
    form_class = AddCarsForm
    template_name = 'auto/car_create.html'
    success_url = reverse_lazy('garage')
    login_url = reverse_lazy('login')
    extra_context = {'title': 'Добавление авто'}


# Create your views here.
