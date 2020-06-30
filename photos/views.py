from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Image,Category,Location
from django_countries import countries



# Create your views here.
def home(request):
    images = Image.objects.all()
    return render(request, 'home.html', {"images":images})

def search(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search').lower()
        category = Category.find_category_id(search_term)
        searched_images = Image.search_image(category)
        message = f"{search_term}" 


        return render(request, 'search.html',{"message":message, "images":searched_images})
    else:
        message = "No results."
        return render(request, 'search.html',{"message":message})


def location(request):

    if 'country' in request.GET and request.GET['country']:
        location_object = request.GET.get('country')

        location = Location.find_location(location_object)

        images = Image.filter_by_location(location)
        country = dict(countries)[location_object]
        no_message = ''
        message = f'Location: {country}'  

        if not images:
            no_message = "No images for this location"
 
        return render(request,'location.html',{"images":images, "message":message, "no_message":no_message,})
    else:
        message = "Select A Country"
        return render(request,'location.html',{"message":message})


def copy_image(request,image_id):
    Image.copy_image_url(image_id)

    return redirect(home)