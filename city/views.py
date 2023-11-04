
from django.shortcuts import render
from .models import City
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView , CreateView
from .forms import CityForm
from django.contrib.auth.mixins import LoginRequiredMixin

class CityList(LoginRequiredMixin,ListView):
     model = City
     template_name = 'city_list.html'
     context_object_name = 'cities'
 

class CityDetail(LoginRequiredMixin,DetailView):
    model = City
    template_name = 'city_detail.html'
    context_object_name = 'city'
    slug_url_kwarg = 'slug'
    slug_field = 'slug'

   





class CityUpdate(LoginRequiredMixin ,UpdateView):
    model = City
    form_class = CityForm
    template_name = 'city_update.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('city:cities')

    def form_valid(self, form):
        city=form.save(commit=False)
        city.updated_by = self.request.user
        city.save()
        return super().form_valid(form)

class CityDelete(LoginRequiredMixin,DeleteView):
    model = City
    template_name = 'city_delete.html'
    success_url = reverse_lazy('city:cities')
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
    




class CityCreate(LoginRequiredMixin,CreateView):
    model = City
    template_name = 'city_add.html'
    fields = ['name', 'slug', 'flag', 'created_by','ref_country']  

    def get_success_url(self):
        return reverse_lazy('city:cities')