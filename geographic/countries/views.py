from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,Http404
from django.views.generic import View
from django.views.generic import TemplateView  # Importa la clase View
from django.views.generic.list import ListView

from countries.models import Country
# Create your views here.


class HomeView(TemplateView):
    # Estas clases solo aceptan los metodos GET, POST o DISPATCH
    # si se quiere que la vista se comporte de diferente forma
    # dependiendo del metodo debo definir cada medoto:
    # get(), post()
    # si quiero que sin importar el metodo se comporte de la misma forma
    # dispatch()
    template_name = 'countries/home.html'


class TagsView(TemplateView):
    template_name = 'countries/tags.html'


class CountryDetailView(TemplateView):
    template_name = 'countries/country_detail.html'

    def get_context_data(self, *args, **kwargs):
        country = get_object_or_404(Country, code=kwargs['code'])

        return {'country': country}


class CountrySearchView(ListView):
    template_name = 'countries/search.html'

    def get_queryset(self):
        query = self.kwargs['query']
        return Country.objects.filter(name__contains=query)
