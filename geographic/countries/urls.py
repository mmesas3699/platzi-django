from django.urls import path
from countries.views import (
    HomeView,
    TagsView,
    CountryDetailView,
    CountrySearchView,
)


app_name = 'countries'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('tags/', TagsView.as_view(), name='tags'),
    path('<str:code>/', CountryDetailView.as_view(), name='country_detail_code'),
    path('search/<query>/', CountrySearchView.as_view(), name='country_search')
]
