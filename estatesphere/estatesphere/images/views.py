from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView


class ImageAddView(CreateView):
    pass


class ImageEditView(UpdateView):
    pass


class ImageDetailsView(DetailView):
    pass


def image_delete(request, pk):
    pass
