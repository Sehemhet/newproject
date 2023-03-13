from auto.models import Cars
from django.views.generic import ListView, DetailView

class garage(ListView):
    paginate_by = 16
    model = Cars
    template_name = 'garage/garage_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Гараж'
        return context

    def get_queryset(self):
        return Cars.objects.all()

class my_car(DetailView):
    model = Cars
    template_name = 'garage/garage_detail.html'

# Create your views here.
