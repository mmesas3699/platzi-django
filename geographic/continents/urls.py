from django.urls import path
from continents.views import ContinentsView

app_name = 'continents'

urlpatterns = [
    path('', ContinentsView.as_view(), name='continents'),
]
