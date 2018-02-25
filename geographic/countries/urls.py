from django.urls import path
from .views import HomeView, TagsView, CountryDetailView

app_name = 'countries'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('tags/', TagsView.as_view(), name='tags'),
    path('<str:code>/', CountryDetailView.as_view(), name='country_detail_code'),
]
