from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import TemplateView #  Importa la clase View

# Create your views here.

class ContinentsView(TemplateView):
    template_name = 'continents/home.html'

    def get_context_data(self, *args, **kwargs):
        """ Por medio de esta función se pasan datos al template"""
        america = {'name': 'America'}
        europa = {'name': 'Europa'}
        asia = {'name': 'Asia'}

        continents = [america, europa, asia]

        return {'continents': continents}
