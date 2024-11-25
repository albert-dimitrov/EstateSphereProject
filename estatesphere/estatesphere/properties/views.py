from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from estatesphere.common.forms import ReviewCreateForm
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

    def get_success_url(self):
        return reverse_lazy('property-details', kwargs={'pk': self.object.pk})


class PropertyDetailsView(DetailView):
    model = RealEstateProperty
    template_name = 'properties/details-property.html'
    context_object_name = 'property'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_has_review = self.object.reviews.filter(user=self.request.user).exists()

        context['review_form'] = ReviewCreateForm
        context['user_has_review'] = user_has_review

        return context


class PropertyDeleteView(DeleteView):
    model = RealEstateProperty
    template_name = 'properties/delete-property.html'

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.request.user.pk})


