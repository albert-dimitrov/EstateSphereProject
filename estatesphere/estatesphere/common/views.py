from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from estatesphere.common.forms import SearchForm, ReviewCreateForm
from estatesphere.properties.models import RealEstateProperty
from estatesphere.common.models import Review


class HomePageView(ListView):
    model = RealEstateProperty
    template_name = 'common/home-page.html'
    context_object_name = 'all_properties'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['search_form'] = SearchForm(self.request.GET)

        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        location = self.request.GET.get('property_location')

        if location:
            queryset = queryset.filter(city__icontains=location)

        return queryset


def favourite_functionality(request, property_id):
    pass


class AddReviewView(CreateView):
    model = Review
    form_class = ReviewCreateForm

    def form_valid(self, form):
        property_id = self.kwargs.get('property_id')
        real_estate_property = get_object_or_404(RealEstateProperty, id=property_id)
        form.instance.user = self.request.user
        form.instance.estate_property = real_estate_property
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('property-details', kwargs={'pk': self.kwargs.get('property_id')})


class DeleteReviewView(DeleteView):
    pass


def about_us_page(request):
    pass


