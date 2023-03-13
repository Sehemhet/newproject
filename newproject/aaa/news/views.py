from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from .models import *

class post_list(ListView):
    paginate_by = 3
    model = Post
    extra_context = {'title': 'Новости'}

    def get_queryset(self):
        return Post.objects.filter(publish=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_selected'] = 0
        return context

class post_category(ListView):
    paginate_by = 3
    model = Post
    context_object_name = 'cats'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_selected'] = context['cats'][0].cat_id
        context['title'] = context['cats'][0].cat
        return context

    def get_queryset(self):
        return Post.objects.filter(cat__slug=self.kwargs['slug'], publish=True).select_related('cat')


class post_detail(DetailView):
    model = Post


class post_create(LoginRequiredMixin, CreateView):
    form_class = AddPostForm
    template_name = 'news/post_create.html'
    success_url = reverse_lazy('post_list')
    login_url = reverse_lazy('login')
    extra_context = {'title': 'Добавление статьи'}


# Create your views here.
