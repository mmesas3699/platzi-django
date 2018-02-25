from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import TemplateView #  Importa la clase View

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
        code = kwargs['code']
        
        return {'code': code}
