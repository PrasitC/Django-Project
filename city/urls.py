from django.urls import path
from .views import CityList,CityDetail,CityUpdate,CityDelete,CityCreate

app_name = 'city'

urlpatterns = [
    path('city/', CityList.as_view(), name='city-list'),
    path('city/<slug:slug>/', CityDetail.as_view(), name='city-detail'),
    path('city/<slug:slug>/update/', CityUpdate.as_view(), name='city-update'),
    path('city/<slug:slug>/delete/', CityDelete.as_view(), name='city-delete'),
    path('/city/add/', CityCreate.as_view(), name='city-add')
]
