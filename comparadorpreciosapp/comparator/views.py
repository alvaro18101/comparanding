from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic

def index(request):
    return HttpResponse('Hello World')

class IndexView(generic.ListView):
    template_name = 'comparator/index.html'
    context_object_name = 'search_performed'

# def search(request, query):
