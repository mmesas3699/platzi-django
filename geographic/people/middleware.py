from django.http import Http404
 

# class SecretMiddleware:
#    def __init__(self, get_response):
#        self.get_response = get_response

#    def __call__(self, request):
        # Antes de la vista, todo lo que sigue se ejecuta antes de renderizar la vista: 

#        if not request.GET.get('secret'):
#            raise Http404()
#        if request.GET.get('secret') != 'platzi':
#            raise Http404()
#        response = self.get_response(request)
        
        # Despues de la vista
#        return response

class ABMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # antes de la vista
        if 'testab' not in request.session:
            request.session['testab'] = 'a'

        response = self.get_response(request)    
        
        return response