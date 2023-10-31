from django.shortcuts import render
from rest_framework import generics
from .models import Country
from .serializers import CountrySerializer
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .forms import  CountryForm

class CountryList(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = CountrySerializer(queryset, many=True)
        print(serializer.data)  # Add this line
        return render(request, "country_list.html", {'countries': serializer.data})
class CountryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_field = 'slug'

    def retrieve(self, request, slug):
        country = get_object_or_404(Country, slug=slug)
        serializer = CountrySerializer(country)
        print(serializer.data)
        return render(request, 'country_detail.html', {'country': country})
    




class  CountryUpdate(UpdateView):
    model = Country
    form_class =  CountryForm
    template_name = 'country_update.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('country:country-list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class CountryDelete(DeleteView):
    model = Country
    template_name = 'country_delete.html'
    success_url = reverse_lazy('country:country-list')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['country'] = self.get_object()
        return context

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)
    


class CountryCreate(CreateView):
    model = Country
    template_name = 'country_add.html'
    fields = ['name', 'slug', 'flag', 'created_by']  # Add the fields you want to include in the form

    def get_success_url(self):
        return reverse_lazy('country:country-list')