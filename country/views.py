from django.views.generic import ListView,DetailView
from django.shortcuts import render
from .models import Country
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .forms import  CountryForm
from django.contrib.auth.mixins import LoginRequiredMixin
class CountryList(LoginRequiredMixin,ListView):
     model= Country
     template_name = 'country_list.html'
     context_object_name = 'countries'
   

class CountryDetail(LoginRequiredMixin,DetailView):
    model = Country
    template_name = 'country_detail.html'
    context_object_name = 'country'
    slug_url_kwarg = 'slug'
    slug_field = 'slug'

  




class  CountryUpdate(LoginRequiredMixin,UpdateView):
    model = Country
    form_class =  CountryForm
    template_name = 'country_update.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('country:countries')

    def form_valid(self, form):
        country = form.save(commit=False)
        country.updated_by = self.request.user
        country.save()
        return super().form_valid(form)

class CountryDelete(LoginRequiredMixin,DeleteView):
    model = Country
    template_name = 'country_delete.html'
    success_url = reverse_lazy('country:countries')
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
    


class CountryCreate(LoginRequiredMixin,CreateView):
    model = Country
    template_name = 'country_add.html'
    fields = ['name', 'slug', 'flag', 'created_by'] 

    def get_success_url(self):
        return reverse_lazy('country:countries')