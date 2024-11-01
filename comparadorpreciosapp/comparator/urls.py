from django.urls import path
from . import views

app_name = 'comparator'
urlpatterns = [
    path('', views.index, name='index'),
    path('results/', views.results, name='results'),
    path('search/', views.search, name='search')
]