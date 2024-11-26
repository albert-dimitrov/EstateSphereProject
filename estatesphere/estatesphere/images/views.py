from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView
from estatesphere.images.models import Image
from estatesphere.images.forms import MultiImageUploadForm
from estatesphere.properties.models import RealEstateProperty


def add_images_view(request, property_id):

    estate_property = get_object_or_404(RealEstateProperty, id=property_id)

    if request.method == 'POST':
        form = MultiImageUploadForm(request.POST, request.FILES)

        if form.is_valid():
            images = request.FILES.getlist('images')

            for img in images:

                Image.objects.create(
                    user=request.user,
                    estate_property=estate_property,
                    image=img
                )

            return redirect('property-details', pk=property_id)
    else:
        form = MultiImageUploadForm()

    return render(request, 'images/add-images.html', {'form': form, 'property': estate_property})


class ImageDetailsView(DetailView):
    model = RealEstateProperty
    template_name = 'images/property-images.html'
    context_object_name = 'property'


class DeleteImageView(DeleteView):
    model = Image

    def get_success_url(self):
        return reverse_lazy('property-details', kwargs={'pk': self.object.estate_property.pk})
