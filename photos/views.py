from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Image, Category, Location

#Create your views here.
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
    
    return render(request,'location.html') 