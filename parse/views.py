from django.shortcuts import render

def index(request):
    # flats = Flat.objects.all()
    flats = [1,2,3]
    # get_flats()
    return render(request, 'parse/index.html', {'flats': flats})
