from django.shortcuts import render
from django.views.generic import CreateView, ListView


class ImageAddView(CreateView):
    pass


class ImageDetailsView(ListView):
    pass


def image_delete(request, pk):
    pass
