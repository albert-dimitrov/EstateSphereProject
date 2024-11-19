from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from estatesphere.common.forms import SearchForm
from estatesphere.properties.models import RealEstateProperty


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
    pass


class EditReviewView(UpdateView):
    pass


class DeleteReviewView(DeleteView):
    pass


def about_us_page(request):
    pass


