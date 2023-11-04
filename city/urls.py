from django.urls import path
from .views import CityList,CityDetail,CityUpdate,CityDelete,CityCreate


app_name = 'city'

urlpatterns = [
    path('', CityList.as_view(), name='cities'),
    path('add/', CityCreate.as_view(), name='city-add'),
    path('<slug:slug>/', CityDetail.as_view(), name='city-detail'),
    path('<slug:slug>/update/', CityUpdate.as_view(), name='city-update'),
    path('<slug:slug>/delete/', CityDelete.as_view(), name='city-delete'),
    
]
