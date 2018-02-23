

def countries_data(request):
    colombia = {'name': 'Colombia', 'code': 'CO'}
    usa = {'name': 'Estados Unidos', 'code': 'USA'}
    mexico = {'name': 'Mexico', 'code': 'MX'}
    countries = [colombia, usa, mexico]
        
    return {'countries': countries}
