from django.shortcuts import render

from .get_parsing import *
from .models import Flat

def get_flats():
    main()


def index(request):
    flats = Flat.objects.all()
    get_flats()
    return render(request, 'parse/index.html', {'flats': flats})
