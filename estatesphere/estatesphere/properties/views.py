from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from estatesphere.properties.forms import PropertyCreateForm
from estatesphere.properties.models import RealEstateProperty


class PropertyAddView(CreateView):
    model = RealEstateProperty
    form_class = PropertyCreateForm
    template_name = 'properties/add-property.html'
    
    def form_valid(self, form):
        estate_property = form.save(commit=False)
        estate_property.user = self.request.user
        
        return super().form_valid(form)
        
    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.request.user.pk})


class PropertyEditView(UpdateView):
    model = RealEstateProperty
    form_class = PropertyCreateForm
    template_name = 'properties/edit-property.html'

    def get_success_url(self): #TODO make the redirect to property details
        return reverse_lazy('profile-details', kwargs={'pk': self.request.user.pk})


class PropertyDetailsView(DetailView):
    pass


class PropertyDeleteView(DeleteView):
    model = RealEstateProperty
    template_name = 'properties/delete-property.html'

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.request.user.pk})


