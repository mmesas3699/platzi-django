from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View #  Importa la clase View

# Create your views here.

class HomeView(View):
    # Estas clases solo aceptan los metodos GET, POST o DISPATCH
    # si se quiere que la vista se comporte de diferente forma
    # dependiendo del metodo debo definir cada medoto:
    # get(), post()
    # si quiero que sin importar el metodo se comporte de la misma forma
    # dispatch()

    def get(self, request, *args, **kwargs):
        return render(request, 'countries/home.html')

