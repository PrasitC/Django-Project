from django.shortcuts import render
from rest_framework import generics
from .models import City
from .serializers import CitySerializer
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView , CreateView
from .forms import CityForm

class CityList(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer =  CitySerializer(queryset, many=True)
        print(serializer.data)  # Add this line
        return render(request, "city_list.html", {'cities': serializer.data})
    


class CityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class =  CitySerializer
    lookup_field = 'slug'

  
    def retrieve(self, request, slug):
      city = get_object_or_404(City, slug=slug)
      serializer = CitySerializer(city)
      print(serializer.data)
      return render(request, 'city_detail.html', {'city': city})
    







class CityUpdate(UpdateView):
    model = City
    form_class = CityForm
    template_name = 'city_update.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('city:city-list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class CityDelete(DeleteView):
    model = City
    template_name = 'city_delete.html'
    success_url = reverse_lazy('city:city-list')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city'] = self.get_object()
        return context

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)
    




class CityCreate(CreateView):
    model = City
    template_name = 'city_add.html'
    fields = ['name', 'slug', 'flag', 'created_by']  # Add the fields you want to include in the form

    def get_success_url(self):
        return reverse_lazy('city:city-list')