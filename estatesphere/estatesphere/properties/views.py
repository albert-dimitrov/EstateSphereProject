from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView


class PropertyAddView(CreateView):
    pass


class PropertyEditView(UpdateView):
    pass


class PropertyDetailsView(DetailView):
    pass


class PropertyDeleteView(DeleteView):
    pass


