from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import AddCarsForm
from .models import Cars, Brands


class brand_list(ListView):
    paginate_by = 12
    model = Cars
    extra_context = {'title': 'Марки'}
    template_name = 'auto/brands_list.html'
    # slug_url_kwarg = 'slug'

    def get_queryset(self):
        return Brands.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['cat_selected'] = 0
        return context

class model_list(ListView):
    paginate_by = 9
    model = Brands
    template_name = 'auto/models_list.html'
    # slug_url_kwarg = 'slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Cars.objects.filter(brand__slug=self.kwargs['slug_brand'])

class car_detail(DetailView):
    model = Cars
    context_object_name = 'car'
    template_name = 'auto/car_detail.html'
    extra_context = {'title': 'Автомобиль'}
    slug_url_kwarg = 'slug'  #то что принимается из строки
    slug_field = 'slug_car'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('slug_car')
        return get_object_or_404(Cars, slug=slug)


# class car_detail(DetailView):
#     model = Cars
#     context_object_name = 'car'
#     template_name = 'auto/car_detail.html'
#     extra_context = {'title': 'Автомобиль'}
#     slug_url_kwarg = 'car_slug'
#
#     def get_queryset(self):
#         brand = self.kwargs.get('brand_slug', '')
#         q = super().get_queryset()
#         return q.filter(brand__slug=brand).select_related('brand')

# def car_create(request):
#     return render(request, 'auto/car_create.html', {'title': 'добавление автомобиля'})

class car_create(CreateView):
    form_class = AddCarsForm
    template_name = 'auto/car_create.html'
    success_url = reverse_lazy('brand_list')
    login_url = reverse_lazy('home')
    raise_exception = True
    extra_context = {'title': 'Добавление авто'}


# Create your views here.
