from django.shortcuts import render

from .models import Flat

def index(request):
    flats = Flat.objects.all()
    # get_flats()
    return render(request, 'parse/index.html', {'flats': flats})
