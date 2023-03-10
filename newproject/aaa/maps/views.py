from django.shortcuts import render

def maps(request):
    return render(request, 'maps/maps.html', {'title':'карта'})

# Create your views here.
