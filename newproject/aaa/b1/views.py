from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from b1.forms import RegisterUserForm, LoginUserForm
from b1.models import *
from django.contrib.auth import logout, login


def home_def(request):
    data = {
        'title':'Главная страница'
    }
    return render(request, 'b1/index.html', data)

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'b1/register.html'
    success_url = reverse_lazy('login')
    extra_context = {'title': 'Регистация'}

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_selected'] = 0
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
        context['cat_selected'] = 0
        return context

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')

# Create your views here.
