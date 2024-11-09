from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Query

# from my_packages.main import DoWebScraping
from my_packages.WebScraping import WebScrapingLinio

def index(request):
    return render(request, 'comparator/index.html')

def results(request):
    query_text = Query.objects.all().last()
    products_name, prices, products_brand, products_dealer, products_image, url_linio = WebScrapingLinio(query_text)
    products_name = list(products_name)
    prices = list(prices)
    products_brand = list(products_brand)
    products_dealer = list(products_dealer)
    products_image = list(products_image)
    data = list(zip(products_name, prices, products_brand, products_dealer, products_image))

    return render(request, 'comparator/results.html', {
        'query_text': query_text,
        'data_linio': data,
        'products_name': products_name,
        'url_linio': url_linio
    })

def search(request):
    query_name = request.POST['query_to_search']
    query = Query.objects.create(query_text=query_name)
    return HttpResponseRedirect(reverse('comparator:results'))
    # return redirect('results')



def get_name(request):
    if request.method == 'POST':
        form = Query(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = Query()
    print(form)
    return render(request, 'results.html', {'form': form})

# class FormView(generic.FormView):
    # name = forms.CharField(label="Query to search", max_length=200)

# class IndexView(generic.ListView):
#     template_name = 'comparator/index.html'
#     context_object_name = 'search_performed'