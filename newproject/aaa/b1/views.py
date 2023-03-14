from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from b1.forms import RegisterUserForm, LoginUserForm
from b1.models import *
from django.contrib.auth import logout, login
from auto.models import Brands


def home_def(request):
    data = {
        'title':'Главная страница'
    }
    return TemplateResponse(request, 'b1/index.html', data)

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'b1/register.html'
    success_url = reverse_lazy('login')
    extra_context = {'title': 'Регистация'}

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'b1/login.html'
    extra_context = {'title': 'Логин'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')

class Search(ListView):
    model = Brands
    template_name = 'auto/brands_list.html'

    def get_queryset(self):
        return Brands.objects.filter(brand__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Марки'
        return context

# Create your views here.
