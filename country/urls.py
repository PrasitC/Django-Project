from django.urls import path
from .views import CountryList,CountryDetail,CountryUpdate, CountryDelete, CountryCreate

app_name = 'country'

urlpatterns = [
    path('countries/', CountryList.as_view(), name='country-list'),
    path('countries/<slug:slug>/', CountryDetail.as_view(), name='country-detail'),
   path('countries/<slug:slug>/update/', CountryUpdate.as_view(), name='country-update'),
    path('countries/<slug:slug>/delete/', CountryDelete.as_view(), name='country-delete'),
     path('country/add/', CountryCreate.as_view(), name='country-add'),
]

