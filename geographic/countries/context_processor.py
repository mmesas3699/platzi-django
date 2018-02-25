from django.urls import reverse

def countries_data(request):
    colombia = {
        'name': 'Colombia',
        'code': 'CO',
        'url': reverse('countries:country_detail_code', kwargs={'code': 'CO'})
    }
    usa = {
        'name': 'Estados Unidos',
        'code': 'USA',
        'url': reverse('countries:country_detail_code', kwargs={'code': 'USA'})
    }
    mexico = {
        'name': 'Mexico',
        'code': 'MX',
        'url': reverse('countries:country_detail_code', kwargs={'code': 'MX'})
    }
    countries = [colombia, usa, mexico]
        
    return {'countries': countries}
