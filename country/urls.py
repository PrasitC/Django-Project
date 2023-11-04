from django.urls import path
from .views import CountryList,CountryDetail,CountryUpdate, CountryDelete, CountryCreate

app_name = 'country'

urlpatterns = [
    path('', CountryList.as_view(), name='countries'),
    path('add/', CountryCreate.as_view(), name='country-add'),
    path('<slug:slug>/', CountryDetail.as_view(), name='country-detail'),
    path('<slug:slug>/update/', CountryUpdate.as_view(), name='country-update'),
    path('<slug:slug>/delete/', CountryDelete.as_view(), name='country-delete'),
] 


